import React, {useContext, useState} from "react";
import {
  Button,
  makeStyles,
  TextField,
  Table,
  TableBody,
  TableCell,
  TableContainer,
  TableHead,
  TableRow,
  Paper, Backdrop, CircularProgress,
} from "@material-ui/core";
import AppBar from "./AppBar";
import {DataItem} from "../types/types";
import {useHistory} from 'react-router-dom';
import axios from 'axios';
import dataContext from "../context/testDataContext";
import attributeContext from "../context/attributeContext";


const useStyles = makeStyles((theme) => ({
  container: {
    display: "flex",
    justifyContent: 'center',
    width: '100vw',
  },
  root: {
    width: '80vw',
    marginTop: theme.spacing(1),
  },
  input: {
    width: '40%',
    margin: theme.spacing(2),
  },
  btnBox: {
    margin: theme.spacing(2),
  },
  table: {
    minWidth: 650,
  },
  tableContainer: {
    marginTop: theme.spacing(4),
  },
  backdrop: {
    zIndex: theme.zIndex.drawer + 1,
    color: '#fff',
  },
  tableHeading: {}
}));

const Home = () => {
  const styles = useStyles();

  const appContext = useContext(dataContext);
  const attrContext = useContext(attributeContext);

  const [header, setHeader] = useState<string>('');
  const [text, setText] = useState<string>('');
  const [rating, setRating] = useState<number>(0);
  const [votes, setVotes] = useState<number>(0);
  const [loading, setLoading] = useState<boolean>(false);
  const [data, setData] = useState<Array<DataItem>>([]);

  const history = useHistory()

  const addData = () => {
    const prevData = [...appContext.appData];
    const item: DataItem = {
      header,
      text,
      rating,
      upvotes:votes
    };
    prevData.push(item);
    // setData(prevData);
    appContext.setAppData(prevData);
  }

  const uploadData = () => {
    setLoading(true);
    const config = {
      method: 'POST',
      url: 'http://localhost:5000/get-aspects',
      data: {
        reviews: data,
        file_name: "temp",
      }
    }

    axios.post('http://localhost:5000/get-aspects', {
      reviews: appContext.appData,
      file_name: "temp",
    }).then(res => {
      console.log(res);
      const attrs:Array<string> = Object.values(res.data);
      // console.log("attr-----------------------",attrs)
      attrContext.setAttrs(attrs);
      history.push('/attr');
      setLoading(false);
    }).catch(err => {
      console.log(err);
      setLoading(false);
    });


    // axios(config).then((res) => {
    //   console.log(res);
    //   const attrs = Object.values(res);
    //   attrContext.setAttrs(attrs);
    //   history.push('/attr');
    //   setLoading(false);
    // }).catch(err => {
    //   console.log(err);
    //   setLoading(false);
    // });

    // attrContext.setAttrs(['ABCD', 'DJSFK', 'SDFHJKDSH', 'SDHJFHDS', 'SDJFKJDSK']);
    // setTimeout(() => {
    //   setLoading(false);
    //   history.push('/attr');
    // }, 2000);

  }

  return (
    <div>
      <AppBar/>
      <div className={styles.container}>
        <div className={styles.root}>
          <div>
            <TextField
              variant="outlined"
              className={styles.input}
              label="Header"
              value={header}
              onChange={(event) => setHeader(event.target.value)}
            />
            <TextField
              variant="outlined"
              className={styles.input}
              label="Text"
              value={text}
              onChange={(event) => setText(event.target.value)}
            />
            <TextField
              variant="outlined"
              className={styles.input}
              type={'number'}
              label="Rating"
              value={rating}
              onChange={(event) => setRating(parseFloat(event.target.value))}
            />
            <TextField
              variant="outlined"
              className={styles.input}
              label="UpVotes"
              type={'number'}
              value={votes}
              onChange={(event) => setVotes(parseFloat(event.target.value))}
            />
          </div>
          <div className={styles.btnBox}>
            <Button variant="contained" color="primary" onClick={() => {
              addData()
            }}>
              Add Data
            </Button>
          </div>
          <div className={styles.tableContainer}>
            <TableContainer component={Paper}>
              <Table className={styles.table} aria-label="simple table">
                <TableHead>
                  <TableRow className={styles.tableHeading}>
                    <TableCell>S.No</TableCell>
                    <TableCell>Header</TableCell>
                    <TableCell>Text</TableCell>
                    <TableCell>Rating</TableCell>
                    <TableCell>UpVotes</TableCell>
                  </TableRow>
                </TableHead>
                <TableBody>
                  {appContext.appData.map((item, index) => (
                    <TableRow key={index}>
                      <TableCell>{index}</TableCell>
                      <TableCell>{item.header}</TableCell>
                      <TableCell>{item.text}</TableCell>
                      <TableCell>{item.rating}</TableCell>
                      <TableCell>{item.upvotes}</TableCell>
                    </TableRow>
                  ))}
                </TableBody>
              </Table>
            </TableContainer>
          </div>
          <div className={styles.btnBox}>
            <Button
              variant="contained"
              color="secondary"
              onClick={uploadData}>
              SUBMIT
            </Button>
          </div>
        </div>
        <div>
          <Backdrop className={styles.backdrop} open={loading} >
            <CircularProgress color="secondary" />
          </Backdrop>
        </div>
      </div>

    </div>
  )
}

export default Home;