import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { useTheme } from "@mui/material";

const BasicTable = (data) => {
  const theme = useTheme();
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minHeight: 340 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell
              sx={{
                backgroundColor: theme.palette.primary.main,
                fontWeight: "bold",
              }}
            >
              Hashtags
            </TableCell>
            <TableCell
              align="center"
              sx={{
                backgroundColor: theme.palette.primary.main,
                fontWeight: "bold",
              }}
            >
              Amount
            </TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {data.data.map((row) => (
            <TableRow key={row.name}>
              <TableCell
                component="th"
                scope="row"
                sx={{
                  backgroundColor: theme.palette.primary.main,
                  color: "#ffffff",
                }}
              >
                {row.name}
              </TableCell>
              <TableCell
                align="center"
                sx={{
                  backgroundColor: theme.palette.primary.main,
                  color: "#ffffff",
                }}
              >
                {row.amount}
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default BasicTable;
