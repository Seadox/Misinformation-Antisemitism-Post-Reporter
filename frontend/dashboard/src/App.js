import { CssBaseline, ThemeProvider, createTheme } from "@mui/material";
import { Route, Routes } from "react-router-dom";
import Dashboard from "./scenes/dashboard";
import Posts from "./scenes/posts";

const darkTheme = createTheme({
  palette: {
    mode: "dark",
    primary: {
      main: "#262936",
    },
    background: {
      default: "#14161D",
      paper: "#14161D",
    },
    typography: {
      fontFamily: '"Nunito Sans", sans-serif',
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={darkTheme}>
      <CssBaseline />
      <div className="App">
        <div className="content">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/posts" element={<Posts />} />
          </Routes>
        </div>
      </div>
    </ThemeProvider>
  );
}

export default App;
