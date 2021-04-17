import Toolbar from "@material-ui/core/Toolbar";
import IconButton from "@material-ui/core/IconButton";
import MenuIcon from "@material-ui/icons/Menu";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import {Link} from "react-router-dom";
import React from "react";
import {AppBar, makeStyles} from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  root: {
    width: '100%',
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
}));

const AppBarComponent = () => {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar>
          <IconButton edge="start" className={classes.menuButton} color="inherit" aria-label="menu">
            <MenuIcon/>
          </IconButton>
          <Typography variant="h5" className={classes.title}>
            Opinion Summarization
          </Typography>
          <Button color="inherit">
            <Link to={'/'}>Home</Link>
          </Button>
        </Toolbar>
      </AppBar>
    </div>
  )
};

export default AppBarComponent;