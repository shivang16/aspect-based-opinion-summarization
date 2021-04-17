import AppBarComponent from "./AppBar";
import {makeStyles, Typography} from "@material-ui/core";
import React, {useContext} from "react";
import ResultContext from "../context/resultContext";
import imag1 from '../assets/pie-chart-temp.png';
import imag2 from '../assets/bar-graph-temp.png';

const useStyles = makeStyles((theme ) => ({
  container: {
    display: 'flex',
    flexDirection: 'column',
    width: '60vw',
    marginTop: theme.spacing(4),
    alignSelf: 'center',
  },
  resultBox: {
    marginTop: theme.spacing(4),
    borderRadius: theme.spacing(1),
    backgroundColor: '#ededed',
    padding: theme.spacing(2),
    // minHeight: '60vh',
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    paddingVertical: '2vh',
  },
  image: {
    width: '50%',
    height: '50%',
  }
}))

const Result = () => {

  const styles = useStyles();

  const resultContext = useContext(ResultContext);

  return (
    <>
      <AppBarComponent />
      <div className={styles.container}>
        <Typography variant="h5" color={'primary'} align={'center'}>
          RESULT:
        </Typography>

        <Typography variant="h6" color={'secondary'} align={'left'}>
          Summary:
        </Typography>
        
        <div className={styles.resultBox}>
          <Typography variant={'inherit'} color={'textPrimary'}>
            {resultContext.result.summary}
          </Typography>
        </div>

        <Typography variant="h6" color={'secondary'} align={'left'}>
          Graphical Summary:
        </Typography>
        

        <div>
          <img src={imag1} className={styles.image} />
          <img src={imag2} className={styles.image} />
        </div>
      </div>
    </>
  )
}

export default Result;