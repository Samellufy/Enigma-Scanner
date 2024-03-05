import React from 'react';
import ReactDOM from 'react-dom/client';
import App from './App';
import './index.css'
import Store from './app/Store';
import { Provider} from 'react-redux';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <Provider store={Store}>
    <App />
    </Provider>
  </React.StrictMode>
);

