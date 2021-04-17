import React, {useState} from 'react';
import './App.css';

import {BrowserRouter, Switch, Route} from 'react-router-dom';
import Home from "./components/Home";
import DataContext from "./context/testDataContext";
import {ThemeProvider} from "@material-ui/core";
import {DataItem} from "./types/types";
import Attributes from "./components/Attributes";
import AttrContext from './context/attributeContext';
import ResultContext from "./context/resultContext";
import Result from "./components/Result";

function App() {

  const [data, setData] = useState<Array<DataItem>>([]);
  const [attributes, setAttributes] = useState<Array<string>>([]);
  const [result, setResult] = useState<any>({});

  const dataHandler = (data: Array<DataItem>) => {
    setData(data);
  }

  const attrHandler = (attrs: Array<string>) => {
    setAttributes(attrs);
  }

  const resultHandler = (result: any) => {
    setResult(result);
  }

  return (
    <>
      <DataContext.Provider value={{
        appData: data,
        setAppData: dataHandler
      }}>
        <AttrContext.Provider value={{
          attrs: attributes,
          setAttrs: attrHandler
        }}>
          <ResultContext.Provider value={{
            result: result,
            setResult: resultHandler
          }}>

            <div className="App">
              <header className="App-header">
                <BrowserRouter>
                  <Switch>
                    <Route path={'/attr'}>
                      <Attributes/>
                    </Route>
                    <Route path={'/result'}>
                      <Result />
                    </Route>
                    <Route path={'/'}>
                      <Home/>
                    </Route>
                  </Switch>
                </BrowserRouter>
              </header>
            </div>

          </ResultContext.Provider>
        </AttrContext.Provider>
      </DataContext.Provider>
    </>
  );
}

export default App;
