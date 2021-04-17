import AppBarComponent from "./AppBar";
import {makeStyles, Typography} from "@material-ui/core";
import React, {useContext} from "react";
import ResultContext from "../context/resultContext";
import imag1 from '../assets/pie-chart-temp.png';
import imag2 from '../assets/bar-graph-temp.png';
import Rating from '@material-ui/lab/Rating';
import {
  Button,
  TextField,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper, Backdrop, CircularProgress,
} from "@material-ui/core";

const useStyles = makeStyles((theme ) => ({
  container: {
    display: 'flex',
    flexDirection: 'column',
    width: '60vw',
    marginTop: theme.spacing(4),
    alignSelf: 'center',
    marginLeft:'20vw'
  },
  resultBox: {
    marginTop: theme.spacing(4),
    marginBottom:theme.spacing(4),
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
  },
  table: {
    minWidth: 650,
  },
  tableContainer: {
    marginTop: theme.spacing(4),
    marginBottom:theme.spacing(4)
  },
  backdrop: {
    zIndex: theme.zIndex.drawer + 1,
    color: '#fff',
  },
  tableHeading: {}
}))

const Result = () => {

  const styles = useStyles();

  const resultContext = useContext(ResultContext);
  let key: Array<any>=[];
  let value: Array<any> = [];
  if(resultContext.result) {
    key = Object.keys(resultContext.result.ratings);
    value = Object.values(resultContext.result.ratings)
  }

  return (
    <div>
      <AppBarComponent />
      <div className={styles.container}>
        <Typography variant="h5" color={'primary'} align={'center'}>
          RESULT:
        </Typography>

        <Typography variant="h6" color={'secondary'} align={'left'}>
          TEXT SUMMARY:
        </Typography>
        
        <div className={styles.resultBox}>
          <Typography variant={'inherit'} color={'textPrimary'}>
            {resultContext.result.summary}
          </Typography>
        </div>

        <div>
          <Typography variant="h6" color={'secondary'} align={'left'}>
            FINAL RATING:
          </Typography>
          <Rating name="half-rating-read" defaultValue={resultContext.result.final_rating} precision={0.1} readOnly />
        </div>
        <Typography variant="h6" color={'secondary'} align={'left'}>
            ASPECTS RATING:
          </Typography>
        <div className={styles.tableContainer}>
            <TableContainer component={Paper}>
              <Table className={styles.table} aria-label="simple table">
                <TableHead>
                  <TableRow className={styles.tableHeading}>
                    <TableCell>S.No</TableCell>
                    <TableCell>Aspect</TableCell>
                    <TableCell>Rating</TableCell>
                  
                  </TableRow>
                </TableHead>
                <TableBody>
                  {key.map((item, index) => {
                    return (
                    <TableRow key={index}>
                      <TableCell>{index}</TableCell>
                      <TableCell>{item}</TableCell>
                      <TableCell><Rating name="half-rating-read" defaultValue={value[index]} precision={0.1} readOnly /></TableCell>
                    </TableRow>
                  )})}
                </TableBody>
              </Table>
            </TableContainer>
          </div>
          

        <Typography variant="h6" color={'secondary'} align={'left'}>
          GRAPHICAL SUMMARY:
        </Typography>
        


        <div>
          <img src={imag1} className={styles.image} />
          <img src={imag2} className={styles.image} />
        </div>
      </div>
    </div>
  )
}

export default Result;