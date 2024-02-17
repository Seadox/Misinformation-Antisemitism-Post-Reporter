import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { useTheme } from "@mui/material";

const UsersTable = ({ users }) => {
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
              User
            </TableCell>
            <TableCell
              align="center"
              sx={{
                backgroundColor: theme.palette.primary.main,
                fontWeight: "bold",
              }}
            >
              Platform
            </TableCell>
            <TableCell
              align="center"
              sx={{
                backgroundColor: theme.palette.primary.main,
                fontWeight: "bold",
              }}
            >
              Total reported posts
            </TableCell>
            <TableCell
              align="center"
              sx={{
                backgroundColor: theme.palette.primary.main,
                fontWeight: "bold",
              }}
            >
              Is active
            </TableCell>
            <TableCell
              align="center"
              sx={{
                backgroundColor: theme.palette.primary.main,
                fontWeight: "bold",
              }}
            >
              Is verified
            </TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {users.map((row) => (
            <TableRow key={row.name}>
              <TableCell
                component="th"
                scope="row"
                sx={{
                  backgroundColor: theme.palette.primary.main,
                  color: "#ffffff",
                }}
              >
                <a
                  href={`http://instagram.com/${row.name}`}
                  target={"_blank"}
                  style={{ color: "#ffffff", textDecoration: "none" }}
                  rel="noreferrer"
                >
                  {row.name}
                </a>
              </TableCell>
              <TableCell
                align="center"
                sx={{
                  backgroundColor: theme.palette.primary.main,
                  color: "#ffffff",
                }}
              >
                {row.platform}
              </TableCell>
              <TableCell
                align="center"
                sx={{
                  backgroundColor: theme.palette.primary.main,
                  color: "#ffffff",
                }}
              >
                {row.posts}
              </TableCell>
              <TableCell
                align="center"
                sx={{
                  backgroundColor: theme.palette.primary.main,
                  color: "#ffffff",
                }}
              >
                {row.active ? "Yes" : "No"}
              </TableCell>
              <TableCell
                align="center"
                sx={{
                  backgroundColor: theme.palette.primary.main,
                  color: "#ffffff",
                }}
              >
                {row.verified ? "Yes" : "No"}
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default UsersTable;
