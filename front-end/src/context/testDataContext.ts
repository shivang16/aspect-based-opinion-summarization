import React, {createContext} from 'react';
import {DataItem} from "../types/types";

interface dataContext {
  appData: Array<DataItem>;
  setAppData: (obj: Array<DataItem>) => void;
}

const dataContext = createContext<dataContext>({
  appData: [],
  setAppData: () => {}
});

export default dataContext;