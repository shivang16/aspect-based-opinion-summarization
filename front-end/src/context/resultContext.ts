import React, {createContext} from 'react';
// import {DataItem} from "../types/types";

interface resultContext {
  result: any;
  setResult: (obj: any) => void;

}

const ResultContext = createContext<resultContext>({
  result: {},
  setResult: () => {}
});

export default ResultContext;