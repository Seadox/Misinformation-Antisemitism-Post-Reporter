# Misinformation & Antisemitism Post Identifier

<p align="center">
  <img src="./icon.png">
</p>

Our project utilizes machine learning to swiftly detect harmful content, such as antisemitic posts, in real-time. By analyzing language patterns and sentiments, we aim to counter emerging threats and foster a safer online environment. Our system continuously learns and adapts to ensure up-to-date defense against evolving trends, promoting responsible communication practices and accurate insights. Our ultimate goal is to contribute to a more informed and healthier digital space, minimizing the impact of antisemitism.

# Features

- Instagram Hashtag Feeds Scraping: Collects data from Instagram hashtag feeds.
- NLP Analysis: Analyzes post text using Natural Language Processing techniques.
- OCR for Image Text Extraction: Extracts text from images using Optical Character Recognition.
- Dashboard: Provides a visual representation of project progress, including graphs of antisemitic post trends, word clouds of popular hashtags, and a subpage for viewing suspected antisemitic posts.

## Run

To run the project locally, follow these steps:

1. Add Instagram username and password to **/backend/scraper/main.py**
2. Add database username and password to **/backend/API server/main.py**

### Run locally

Server

```bash
cd backend/API\ server
python main.py
```

Scraper

```bash
cd backend/scraper
python main.py
```

Dashboard

```bash
cd frontend/dashboard
npm install
npm start
```

## Libraries Used

- [FastAPI](https://github.com/tiangolo/fastapi)
- [SQLAlchemy](https://github.com/sqlalchemy/sqlalchemy)
- [Instagram Private API](https://github.com/ping/instagram_private_api)
- [easyocr](https://github.com/JaidedAI/EasyOCR)
- [scikit-learn](https://github.com/scikit-learn/scikit-learn)
- [MUI](https://github.com/mui/material-ui)
- [react-wordcloud](https://github.com/chrisrzhou/react-wordcloud)

## Demo

![dashboard.jpeg](/demos/dashboard.jpg)

## Authors

- [@Seadox](https://www.github.com/seadox)
- [@BenSarks](https://github.com/BenSarks)
