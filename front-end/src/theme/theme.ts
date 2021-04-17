import { createMuiTheme } from "@material-ui/core/styles";
import { blue } from "@material-ui/core/colors";

const theme = createMuiTheme({
  palette: {
    primary: blue,
  },
  typography: {
    fontFamily: ['"Roboto"'].join(",")
  },
  breakpoints: {
    values: {
      xs: 576,
      sm: 600,
      md: 960,
      lg: 1280,
      xl: 1920
    }
  }
});

export default theme;