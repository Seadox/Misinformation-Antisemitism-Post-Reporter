import { Box, Typography } from "@mui/material";

const StatBox = ({ title, value, img }) => {
  return (
    <Box
      width="100%"
      m="0 30px"
      display="flex"
      flexDirection="row"
      alignItems="center"
      justifyContent="center"
    >
      {img}

      <Box>
        <Typography variant="subtitle2" fontWeight={"bold"}>
          {title}
        </Typography>
        <Typography variant="h6" fontWeight={"bold"} color={"#FF0055"}>
          {value}
        </Typography>
      </Box>
    </Box>
  );
};

export default StatBox;
