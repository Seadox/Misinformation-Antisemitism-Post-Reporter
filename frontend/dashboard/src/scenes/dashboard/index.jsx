import { Box, useTheme } from "@mui/material";
import stat from "../../icons/stat.svg";
import check from "../../icons/check.svg";
import UsersTable from "../../components/usersTable";
import StatBox from "../../components/StatBox";
import Chart from "../../components/LineChart";
import WordCloud from "../../components/WordCloud";

import { useEffect, useState } from "react";

const Dashboard = () => {
  const theme = useTheme();

  const [totalPosts, setTotalPosts] = useState({
    total_posts: 0,
    antisemitic_posts: 0,
  });
  const [wordCloudData, setWordCloudData] = useState([]);
  const [usersData, setUsersData] = useState([]);
  const [reports, setReports] = useState({
    dates: [],
    instagram: [],
    redit: [],
    twitter: [],
    facebook: [],
  });

  useEffect(() => {
    const fetchData = async () => {
      fetch("http://127.0.0.1:8000/dashboard")
        .then((response) => response.json())
        .then((json) => {
          setReports(json.weekly_report);
          setTotalPosts(json.total_posts_number);
          setUsersData(json.all_users);
        });
    };

    // fetchData();
    const interval = setInterval(fetchData, 1000);

    return () => {
      clearInterval(interval);
    };
  }, []);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/all_hashtags")
      .then((response) => response.json())
      .then((json) => {
        setWordCloudData(json);
      });
  }, []);

  return (
    <Box m="20px">
      <Box
        display={"grid"}
        gridTemplateColumns="repeat(12, 1fr)"
        gridAutoRows="100px"
        gap="20px"
      >
        {/* row 1*/}
        <Box
          gridColumn="span 6"
          backgroundColor={theme.palette.primary.main}
          display="flex"
          alignItems="center"
          justifyContent="center"
          color={"#fff"}
        >
          <StatBox
            title="Total Posts"
            value={totalPosts.total_posts}
            img={
              <div
                style={{
                  borderRadius: "50%",
                  backgroundColor: "#414455",
                  width: 56,
                  height: 56,
                  alignItems: "center",
                  justifyContent: "center",
                  display: "flex",
                  marginRight: "8px",
                }}
              >
                <img
                  src={stat}
                  alt="stat"
                  width={32}
                  height={32}
                  backgroundColor="#fff"
                />
              </div>
            }
          />
        </Box>
        <Box
          gridColumn="span 6"
          backgroundColor={theme.palette.primary.main}
          display="flex"
          alignItems="center"
          justifyContent="center"
          onClick={() => {
            window.location.href = "/posts";
          }}
        >
          <StatBox
            title="Antisemitic Posts"
            value={totalPosts.antisemitic_posts}
            img={
              <div
                style={{
                  borderRadius: "50%",
                  background:
                    "linear-gradient(90deg, rgb(68, 129, 235) 0%, rgb(4, 190, 254) 100%)",
                  width: 56,
                  height: 56,
                  alignItems: "center",
                  justifyContent: "center",
                  display: "flex",
                  marginRight: "8px",
                }}
              >
                <img
                  src={check}
                  alt="stat"
                  width={32}
                  height={32}
                  backgroundColor="#fff"
                />
              </div>
            }
          />
        </Box>
        {/* row 2*/}
        <Box
          gridColumn="span 12"
          gridRow="span 3"
          backgroundColor={theme.palette.primary.main}
          display="flex"
          alignItems="center"
          justifyContent="center"
        >
          <Chart reports={reports} />
        </Box>
        {/* row 3*/}
        <Box
          gridColumn="span 6"
          gridRow="span 3"
          alignItems="center"
          justifyContent="center"
        >
          <WordCloud data={wordCloudData} />
        </Box>
        <Box
          gridColumn="span 6"
          gridRow="span 3"
          alignItems="center"
          justifyContent="center"
        >
          <UsersTable users={usersData} />
        </Box>
      </Box>
    </Box>
  );
};

export default Dashboard;
