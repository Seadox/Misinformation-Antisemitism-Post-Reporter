import { CssBaseline, ThemeProvider, createTheme } from "@mui/material";
import Dashboard from "./scenes/dashboard";

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
          <Dashboard />
        </div>
      </div>
    </ThemeProvider>
  );
}

export default App;
