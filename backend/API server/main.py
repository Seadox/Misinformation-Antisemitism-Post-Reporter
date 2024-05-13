from sqlalchemy import create_engine, Table, Column, Integer, String, Date, Boolean, DateTime, ForeignKey, text, select, desc, event
from sqlalchemy.orm import relationship, sessionmaker, DeclarativeBase, Session, declarative_base
from datetime import datetime
from pydantic import BaseModel
from fastapi import FastAPI, Depends
import sqlalchemy as db
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from datetime import timedelta
from nlp import My_NLP

DB_USER = ""  # Add your database username
DB_PASSWORD = ""  # Add your database password


engine = db.create_engine(
    f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@127.0.0.1:3306/misinformation_antisemitism_post_identifier", echo=True)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=False,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

Base = declarative_base()
Base.metadata.bind = engine
Session = sessionmaker(autoflush=False, bind=engine)
session = Session()

my_nlp = My_NLP()


class Data(BaseModel):
    post_author: str
    post_text: str
    post_id: str
    source: str
    extra_data_link: str = None
    media_type: str = None
    hashtags: list[str] = None
    like_count: str
    comment_count: str
    post_link: str


class Info(BaseModel):
    total_posts: int
    antisemitic_posts: int


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True,
                unique=True, nullable=False)
    name = Column(String(255), unique=True, nullable=False)
    social_platform = Column(String(255), nullable=False)
    is_active = Column(Boolean, nullable=False)
    is_verified = Column(Boolean, nullable=False)
    processed_posts = Column(Integer, nullable=False)
    antisemitic_posts = Column(Integer, nullable=False)
    posts = relationship("Posts")

    def __init__(self, name, social_platform, antisemitic_posts):
        self.name = name
        self.social_platform = social_platform
        self.is_active = True
        self.is_verified = False
        self.processed_posts = 1
        self.antisemitic_posts = antisemitic_posts

    def __repr__(self):
        return f"<User(user_name='{self.name}', social_platform='{self.social_platform}', is_active={self.is_active})>"


class Hashtags(Base):
    __tablename__ = "Hashtags"
    id = Column(Integer, primary_key=True, unique=True, nullable=False)
    text = Column(String(255), unique=True, nullable=False)
    count = Column(Integer, nullable=False)

    def __init__(self, text):
        self.text = text
        self.count = 1

    def __repr__(self):
        return f"<Hashtags(hashtag='{self.text}', hashtag='{self.count}')>"


class Posts(Base):
    __tablename__ = "posts"
    id = Column(String(255), primary_key=True, unique=True)
    code = Column(String(255), nullable=False)
    comment_count = Column(Integer, nullable=False)
    media_type = Column(String(255), nullable=False)
    media_url = Column(String(510), nullable=True)
    title_text = Column(String(2200))
    like_count = Column(Integer, nullable=False)
    user_name = Column(String(255), ForeignKey(
        'users.name'), nullable=False)
    nlp_description = Column(Integer)
    nlp_content = Column(Integer)
    ocr_text = Column(String(255))
    timestamp = Column(DateTime, default=datetime.now, nullable=False)

    user = relationship("User", back_populates="posts")

    def __init__(self, id, code, comment_count, media_type, media_url, title_text, like_count, user_name, nlp_description, nlp_content, ocr_text):
        self.id = id
        self.code = code
        self.comment_count = comment_count
        self.media_type = media_type
        self.media_url = media_url
        self.title_text = title_text
        self.like_count = like_count
        self.user_name = user_name
        self.nlp_description = nlp_description
        self.nlp_content = nlp_content
        self.ocr_text = ocr_text

    def __repr__(self):
        return f"<Post(id={self.id}, user_name='{self.user_name}')>"


class DailyReports(Base):
    __tablename__ = "daily_reports"
    date = Column(Date, primary_key=True)
    total_posts = Column(Integer)
    antisemitic_posts = Column(Integer)

    def __init__(self, date, total_posts=0, antisemitic_posts=0):
        self.date = date
        self.total_posts = total_posts
        self.antisemitic_posts = antisemitic_posts


def update_daily_reports(mapper, connection, target):
    date = target.timestamp.date()
    Session = sessionmaker(bind=engine)
    with Session() as session:
        daily_report = session.query(DailyReports).filter_by(date=date).first()
        if daily_report:
            daily_report.total_posts += 1
            if (target.nlp_description or target.nlp_content):
                daily_report.antisemitic_posts += 1
        else:
            new_report = DailyReports(date=date, total_posts=1, antisemitic_posts=(
                target.nlp_description or target.nlp_content))
            session.add(new_report)
        session.commit()


event.listen(Posts, 'after_insert', update_daily_reports)

Base.metadata.create_all(engine)


def add_hashtags(hashtags: list[str]):
    for hashtag in hashtags:
        existing_hashtag = session.query(Hashtags).filter(
            Hashtags.text == hashtag).first()
        if existing_hashtag:
            existing_hashtag.count += 1
        else:
            new_hashtag = Hashtags(hashtag)
            session.add(new_hashtag)
    session.commit()


def add_user(username: str, social_platform: str, nlpResult: int, nlpResultOCR: int):
    existing_user = session.query(User).filter(
        User.name == username).first()
    if existing_user:
        existing_user.processed_posts += 1
        if (nlpResult or nlpResultOCR):
            existing_user.antisemitic_posts += 1
    else:
        new_user = User(name=username, social_platform=social_platform,
                        antisemitic_posts=(nlpResult or nlpResultOCR))
        session.add(new_user)
    session.commit()


@app.post("/scraper")
async def add_post(data: list[Data]):
    print(f"Data: {data}")

    for post in data:
        ocr_text = None
        nlp_res = 0
        nlp_ocr_res = 0

        # try:
        #     if d.media_type == "image":
        #         ocr_text = MyOCR.get_text(d.extra_data_link)
        # except Exception as e:
        #     pass

        try:
            if post.post_text:
                nlp_res = my_nlp.getPredict(post.post_text)
        except Exception as e:
            pass

        try:
            if ocr_text:
                nlp_ocr_res = my_nlp.getPredict(ocr_text)
        except Exception as e:
            pass

        try:

            add_user(post.post_author, post.source, nlp_res, 0)
            new_post = Posts(
                id=post.post_id,
                comment_count=post.comment_count,
                media_type=post.media_type,
                media_url=post.extra_data_link,
                title_text=post.post_text,
                like_count=post.like_count,
                code=post.post_link,
                user_name=post.post_author,
                nlp_description=0,
                nlp_content=nlp_res,
                ocr_text=0
            )
            session.add(new_post)
            session.commit()
            add_hashtags(post.hashtags)
        except Exception as e:
            session.rollback()
            print(f"Error:scraper {e}")
        finally:
            session.close()


def get_all_users():
    Session = sessionmaker(bind=engine)
    with Session() as session:
        users = session.query(User).limit(7).all()
    session.commit()

    sorted_users = sorted(users, key=lambda x: x.processed_posts, reverse=True)
    return sorted_users


def get_all_posts():
    Session = sessionmaker(bind=engine)
    with Session() as session:
        posts = session.query(Posts).all()
    session.commit()
    return posts


@app.get("/all_hashtags")
async def get_all_hashtags():
    Session = sessionmaker(bind=engine)
    with Session() as session:
        hashtags = session.query(Hashtags).all()
    session.commit()

    new_hashtags = []
    for hashtag in hashtags:
        new_hashtags.append({'text': hashtag.text, 'value': hashtag.count})

    return new_hashtags


def get_top_antisemitic_users():
    Session = sessionmaker(bind=engine)
    with Session() as session:
        users = session.query(User).order_by(
            desc(User.antisemitic_posts)).limit(10).all()
    session.commit()
    return users


def get_total_posts_numbers():
    Session = sessionmaker(bind=engine)
    with Session() as session:
        users = session.query(User).all()
    session.commit()

    total_posts = 0
    antisemitic_posts = 0

    for user in users:
        total_posts += user.processed_posts
        antisemitic_posts += user.antisemitic_posts

    info = Info(total_posts=total_posts, antisemitic_posts=antisemitic_posts)
    return info


def show_weekly_report():
    Session = sessionmaker(bind=engine)
    with Session() as session:
        report = session.query(DailyReports).order_by(
            desc(DailyReports.date)).limit(7).all()
    session.commit()

    dates = []
    instagram = []
    redit = []
    twitter = []
    facebook = []

    sorted_report = sorted(report, key=lambda x: x.date)

    for daily_report in sorted_report:
        dates.append(daily_report.date.strftime("%d-%m-%Y"))
        instagram.append(daily_report.antisemitic_posts)
        redit.append(0)
        twitter.append(0)
        facebook.append(0)

        # Check if the first date is a week before the last date
        if len(dates) > 0:
            first_date = datetime.strptime(dates[0], "%d-%m-%Y")
            last_date = datetime.strptime(dates[-1], "%d-%m-%Y")
            delta = last_date - first_date

            # If the difference is less than 7, add fake dates
            if delta.days < 7-len(dates):
                for i in range(delta.days + 1, 7-len(dates)):
                    fake_date = (last_date - timedelta(days=i)
                                 ).strftime("%d-%m-%Y")
                    dates.insert(0, fake_date)
                    instagram.insert(0, 0)
                    redit.insert(0, 0)
                    twitter.insert(0, 0)
                    facebook.insert(0, 0)

    return {"dates": dates, "instagram": instagram, "redit": redit, "twitter": twitter, "facebook": facebook}


@app.get("/posts")
async def get_posts():
    Session = sessionmaker(bind=engine)
    with Session() as session:
        posts = session.query(Posts).filter(
            Posts.nlp_content == 1).order_by(desc(Posts.timestamp)).limit(10).all()
    session.commit()

    return posts


@app.get("/top_hashtags")
async def get_top_hashtags():
    Session = sessionmaker(bind=engine)
    with Session() as session:
        hashtags = session.query(Hashtags).order_by(
            desc(Hashtags.count)).limit(5).all()
    session.commit()
    hashtags_list = []
    for hashtag in hashtags:
        hashtags_list.append(hashtag.text)
    return hashtags_list


@app.get("/dashboard")
async def dashboard():
    weekly_report = show_weekly_report()
    total_posts_number = get_total_posts_numbers()
    top_antisemitic_users = get_top_antisemitic_users()
    all_users = get_all_users()

    return {
        "weekly_report": weekly_report,
        "total_posts_number": total_posts_number,
        "top_antisemitic_users": top_antisemitic_users,
        "all_users": all_users
    }


@app.get("/")
async def root():
    return {"status", "running"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
