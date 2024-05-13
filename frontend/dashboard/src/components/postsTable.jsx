import Table from "@mui/material/Table";
import TableBody from "@mui/material/TableBody";
import TableCell from "@mui/material/TableCell";
import TableContainer from "@mui/material/TableContainer";
import TableHead from "@mui/material/TableHead";
import TableRow from "@mui/material/TableRow";
import Paper from "@mui/material/Paper";
import { useTheme } from "@mui/material";

const PostsTable = ({ posts }) => {
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
                width: "94%",
                textAlign: "center",
              }}
            >
              Post Text
            </TableCell>
            <TableCell
              align="center"
              sx={{
                backgroundColor: theme.palette.primary.main,
                fontWeight: "bold",
                width: "2%",
              }}
            >
              Likes
            </TableCell>
            <TableCell
              align="center"
              sx={{
                backgroundColor: theme.palette.primary.main,
                fontWeight: "bold",
                width: "2%",
              }}
            >
              Comments
            </TableCell>
            <TableCell
              align="center"
              sx={{
                backgroundColor: theme.palette.primary.main,
                fontWeight: "bold",
                width: "2%",
              }}
            >
              Link
            </TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {posts.map((row) => (
            <TableRow key={row.name}>
              <TableCell
                component="th"
                scope="row"
                sx={{
                  backgroundColor: theme.palette.primary.main,
                  color: "#ffffff",
                }}
              >
                {row.title_text}
              </TableCell>
              <TableCell
                align="center"
                sx={{
                  backgroundColor: theme.palette.primary.main,
                  color: "#ffffff",
                  fontWeight: "bold",
                }}
              >
                {row.like_count}
              </TableCell>
              <TableCell
                align="center"
                sx={{
                  backgroundColor: theme.palette.primary.main,
                  color: "#ffffff",
                  fontWeight: "bold",
                }}
              >
                {row.comment_count}
              </TableCell>
              <TableCell
                align="center"
                sx={{
                  backgroundColor: theme.palette.primary.main,
                  color: "#ffffff",
                }}
              >
                <a
                  href={`http://instagram.com/p/${row.code}`}
                  target={"_blank"}
                  style={{ color: "#ffffff" }}
                  rel="noreferrer"
                >
                  {row.code}
                </a>
              </TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

export default PostsTable;
