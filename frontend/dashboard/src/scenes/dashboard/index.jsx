import { Box, useTheme } from "@mui/material";
import stat from "../../icons/stat.svg";
import post from "../../icons/post.svg";
import check from "../../icons/check.svg";
import Table from "../../components/table";
import UsersTable from "../../components/usersTable";
import StatBox from "../../components/StatBox";
import Chart from "../../components/LineChart";

const tableData = [
  { name: "freepalestine", amount: 100 },
  { name: "freepalestine", amount: 100 },
  { name: "freepalestine", amount: 100 },
  { name: "freepalestine", amount: 100 },
  { name: "freepalestine", amount: 100 },
];
const usersData = [
  {
    name: "enpassant",
    posts: 100,
    active: true,
    verified: false,
    platform: "instagram",
  },
  {
    name: "user2",
    posts: 12,
    active: true,
    verified: false,
    platform: "instagram",
  },
  {
    name: "user3",
    posts: 56,
    active: true,
    verified: false,
    platform: "instagram",
  },
  {
    name: "user4",
    posts: 21,
    active: true,
    verified: false,
    platform: "instagram",
  },
  {
    name: "user5",
    posts: 45,
    active: true,
    verified: false,
    platform: "instagram",
  },
];

const reports = {
  dates: [
    "11.02.24",
    "12.02.24",
    "13.02.24",
    "14.02.24",
    "15.02.24",
    "16.02.24",
    "17.02.24",
  ],
  instagram: [18, 3, 10, 5, 2, 3, 4],
  redit: [30, 10, 15, 17, 2, 20, 45],
  twitter: [26, 7, 16, 19, 0, 7, 9],
  facebook: [50, 20, 30, 35, 5, 40, 90],
};

const Dashboard = () => {
  const theme = useTheme();

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
          gridColumn="span 4"
          backgroundColor={theme.palette.primary.main}
          display="flex"
          alignItems="center"
          justifyContent="center"
          color={"#fff"}
        >
          <StatBox
            title="Total Posts"
            value="100"
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
          gridColumn="span 4"
          backgroundColor={theme.palette.primary.main}
          display="flex"
          alignItems="center"
          justifyContent="center"
        >
          <StatBox
            title="Trained"
            value="100"
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
                  src={post}
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
          gridColumn="span 4"
          backgroundColor={theme.palette.primary.main}
          display="flex"
          alignItems="center"
          justifyContent="center"
        >
          <StatBox
            title="Reported Posts"
            value="100"
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
        <Box
          gridColumn="span 6"
          gridRow="span 3"
          alignItems="center"
          justifyContent="center"
        >
          <Table data={tableData} />
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
