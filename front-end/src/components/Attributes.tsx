import AppBarComponent from "./AppBar";
import {Backdrop, Button, CircularProgress, colors, makeStyles, Theme, Typography} from "@material-ui/core";
import React, {useContext, useEffect, useState} from "react";
import attributeContext from "../context/attributeContext";
import {BuildTwoTone} from "@material-ui/icons";
import {useHistory} from "react-router-dom";
import axios from 'axios';
import ResultContext from "../context/resultContext";

const useStyles = makeStyles((theme: Theme) => ({
  container: {
    display: 'flex',
    justifyContent: 'center',
    flexDirection: 'column',
    alignSelf: 'center',
    width: '80vw',
    marginTop: theme.spacing(3),
  },
  attrBox: {
    display: 'flex',
    marginTop: theme.spacing(3),
    flexWrap: 'wrap',
    justifyContent: 'center',
  },
  attrItem: {
    width: '30%',
    padding: theme.spacing(2),
    borderRadius: theme.spacing(1),
    justifyContent: 'center',
    margin: theme.spacing(2),
    backgroundColor: '#66cfff',
  },
  attrItemSelected: {
    width: '30%',
    padding: theme.spacing(2),
    borderRadius: theme.spacing(1),
    justifyContent: 'center',
    margin: theme.spacing(2),
    backgroundColor: '#91ff35',
  },
  btnBox: {
    marginTop: theme.spacing(20),
  },
  backdrop: {
    zIndex: theme.zIndex.drawer + 1,
    color: '#fff',
  },
}));

const Attributes = () => {

  const styles = useStyles();
  const history = useHistory();

  const [selected, setSelected] = useState<Array<boolean>>([]);
  const [loading, setLoading] = useState<boolean>(false);

  const resultContext = useContext(ResultContext);

  const setAttributes = () => {
    setLoading(true);
    console.log('Inside set Attributes');
    let aspects: Array<string>= [];
    selected.forEach((item, index) => {
      if(item) {
        aspects.push(attrContext.attrs[index]);
      }
    })

    const config = {
      method: 'POST',
      url: 'http://localhost:5000/get-summary',
      data: {
        aspects,
        file_name: 'temp',
      }
    }
    // axios(config).then((res) => {
    //   console.log(res);
    //   history.push('/result');
    //   setLoading(false);
    // }).catch(err => {
    //   console.log(err);
    //   setLoading(false);
    // });

    axios.post('http://localhost:5000/get-summary', {
      aspects: aspects,
      file_name: "temp",
    }).then(res => {
      console.log(res);
      resultContext.setResult(res.data);
      history.push('/result');
      setLoading(false);
    }).catch(err => {
      console.log(err);
      setLoading(false);
    });

    // setTimeout(() => {
    //   console.log('Data in API => ', config.data);
    //   history.push('/result');
    // }, 1000);
  }

  const attrContext = useContext(attributeContext);

  const colorChange = (index: number) => {
    let color = [...selected];
    color[index] = !color[index];
    setSelected(color);
  }

  useEffect(() => {
    let size = attrContext.attrs.length;
    let temp = [];
    for (let i = 0; i < size; i++)
      temp.push(false);
    setSelected(temp);
  }, [attrContext.attrs])

  console.log(attrContext.attrs);
  return (
    <>
      <AppBarComponent/>
      <div className={styles.container}>
        <Typography variant="h6" color={'primary'}>
          Please select one or more attributes
        </Typography>
        <div className={styles.attrBox}>
          {attrContext.attrs.map((item, index) => (
            <div className={!selected[index] ? styles.attrItem : styles.attrItemSelected} onClick={() => {
              colorChange(index);
            }}>{item}</div>
          ))}
        </div>
        <div className={styles.btnBox}>
          <Button
            variant="contained"
            color="secondary"
            onClick={setAttributes}>
            SUBMIT
          </Button>
        </div>
      </div>
      <Backdrop className={styles.backdrop} open={loading} >
        <CircularProgress color="secondary" />
      </Backdrop>
    </>
  )
}

export default Attributes;