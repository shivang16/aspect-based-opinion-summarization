import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import {ThemeProvider} from '@material-ui/core'
import theme from "./theme/theme";
import DataContext from './context/testDataContext';

ReactDOM.render(
  <React.StrictMode>
    <ThemeProvider theme={theme}>
        <App/>
    </ThemeProvider>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals