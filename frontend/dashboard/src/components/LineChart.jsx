import * as React from "react";
import { LineChart } from "@mui/x-charts/LineChart";

const Chart = ({ reports }) => {
  return (
    <LineChart
      xAxis={[
        {
          scaleType: "point",
          data: reports.dates,
          label: "Dates",
        },
      ]}
      series={[
        {
          data: reports.instagram,
          label: "Instagram",
          color: "#EF3DCB",
          //   area: true,
        },
        {
          data: reports.redit,
          label: "Reddit",
          color: "#ED5945",
          //   area: true,
        },
        {
          data: reports.twitter,
          label: "Tiwtter",
          color: "#03A7F2",
          //   area: true,
        },
        {
          data: reports.facebook,
          label: "Facebook",
          color: "#2176FF",
          //   area: true,
        },
      ]}
      sx={{
        ".MuiMarkElement-root": {
          display: "none",
        },
      }}
    />
  );
};

export default Chart;
