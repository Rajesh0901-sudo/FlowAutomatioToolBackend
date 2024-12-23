import React from 'react';
import { Container, CssBaseline } from '@mui/material';
import Header from './Header';
import Footer from './Footer';

const Layout = ({ children }) => {
  return (
    <>
      <CssBaseline />
      <Header />
      <Container>
        {children}
      </Container>
      <Footer />
    </>
  );
};

export default Layout;
import React from 'react';
import { AppBar, Toolbar, Typography } from '@mui/material';

const Header = () => {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6">
          Flow Automation Tool
        </Typography>
      </Toolbar>
    </AppBar>
  );
};

export default Header;
import React from 'react';
import { Box, Typography } from '@mui/material';

const Footer = () => {
  return (
    <Box mt={5} mb={3} textAlign="center">
      <Typography variant="body2" color="textSecondary">
        &copy; {new Date().getFullYear()} Flow Automation Tool. All rights reserved.
      </Typography>
    </Box>
  );
};

export default Footer;
import React, { useState } from 'react';
import { TextField, Button, Typography, Box } from '@mui/material';
import axios from 'axios';

const AddEnvConfig = () => {
  const [envName, setEnvName] = useState('');
  const [configurations, setConfigurations] = useState({
    db_user_name: '',
    db_password: '',
    db_host: '',
    service_name: '',
    new_service_name: ''
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/add_env', {
        env_name: envName,
        configurations
      });
      alert(response.data.message);
    } catch (error) {
      alert(error.response.data.error);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setConfigurations((prevConfig) => ({
      ...prevConfig,
      [name]: value
    }));
  };

  return (
    <Box mt={3}>
      <Typography variant="h5">Add Environment Configuration</Typography>
      <form onSubmit={handleSubmit}>
        <TextField
          label="Environment Name"
          value={envName}
          onChange={(e) => setEnvName(e.target.value)}
          required
          fullWidth
          margin="normal"
        />
        <TextField
          label="DB User Name"
          name="db_user_name"
          value={configurations.db_user_name}
          onChange={handleChange}
          required
          fullWidth
          margin="normal"
        />
        <TextField
          label="DB Password"
          name="db_password"
          type="password"
          value={configurations.db_password}
          onChange={handleChange}
          required
          fullWidth
          margin="normal"
        />
        <TextField
          label="DB Host"
          name="db_host"
          value={configurations.db_host}
          onChange={handleChange}
          required
          fullWidth
          margin="normal"
        />
        <TextField
          label="Service Name"
          name="service_name"
          value={configurations.service_name}
          onChange={handleChange}
          required
          fullWidth
          margin="normal"
        />
        <TextField
          label="New Service Name"
          name="new_service_name"
          value={configurations.new_service_name}
          onChange={handleChange}
          required
          fullWidth
          margin="normal"
        />
        <Button type="submit" variant="contained" color="primary" fullWidth>
          Add Environment
        </Button>
      </form>
    </Box>
  );
};

export default AddEnvConfig;

import React, { useState } from 'react';
import { TextField, Button, Typography, Box } from '@mui/material';
import axios from 'axios';

const AddCustomerDetails = () => {
  const [customerDetails, setCustomerDetails] = useState({
    individualId: '',
    customerBillSpecId: '',
    customerAddressId: '',
    customerAccountId: '',
    name: '',
    ID: ''
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/add_customer', {
        CreateCustomerResponse: customerDetails
      });
      alert(response.data.message);
    } catch (error) {
      alert(error.response.data.error);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setCustomerDetails((prevDetails) => ({
      ...prevDetails,
      [name]: value
    }));
  };

  return (
    <Box mt={3}>
      <Typography variant="h5">Add Customer Details</Typography>
      <form onSubmit={handleSubmit}>
        <TextField
          label="Individual ID"
          name="individualId"
          value={customerDetails.individualId}
          onChange={handleChange}
          required
          fullWidth
          margin="normal"
        />
        <TextField
          label="Customer Bill Spec ID"
          name="customerBillSpecId"
          value={customerDetails.customerBillSpecId}
          onChange={handleChange}
          required
          fullWidth
          margin="normal"
        />
        <TextField
          label="Customer Address ID"
          name="customerAddressId"
          value={customerDetails.customerAddressId}
          onChange={handleChange}
          required
          fullWidth
          margin="normal"
        />
        <TextField
          label="Customer Account ID"
          name="customerAccountId"
          value={customerDetails.customerAccountId}
          onChange={handleChange}
          required
          fullWidth
          margin="normal"
        />
        <TextField
          label="Name"
          name="name"
          value={customerDetails.name}
          onChange={handleChange}
          required
          fullWidth
          margin="normal"
        />
        <TextField
          label="ID"
          name="ID"
          value={customerDetails.ID}
          onChange={handleChange}
          required
          fullWidth
          margin="normal"
        />
        <Button type="submit" variant="contained" color="primary" fullWidth>
          Add Customer
        </Button>
      </form>
    </Box>
  );
};

export default AddCustomerDetails;

import React, { useState } from 'react';
import { TextField, Button, Typography, Box } from '@mui/material';
import { useDispatch } from 'react-redux';
import { runQuery } from '../redux/actions/queryActions';

const RunQuery = () => {
  const [queryDetails, setQueryDetails] = useState({
    env_name: '',
    db_name: '',
    flow_name: ''
  });

  const dispatch = useDispatch();

  const handleSubmit = async (e) => {
    e.preventDefault();
    dispatch(runQuery(queryDetails));
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setQueryDetails((prevDetails) => ({
      ...prevDetails,
      [name]: value
    }));
  };

  return (
    <Box mt={3}>
      <Typography variant="h5">Run Query</Typography>
      <form onSubmit={handleSubmit}>
        <TextField
          label="Environment Name"
          name="env_name"
          value={queryDetails.env_name}
          onChange={handleChange}
          required
          fullWidth
          margin="normal"
        />
        <TextField
          label="DB Name"
          name="db_name"
          value={queryDetails.db_name}
          onChange={handleChange}
          required
          fullWidth
          margin="normal"
        />
        <TextField
          label="Flow Name"
          name="flow_name"
          value={queryDetails.flow_name}
          onChange={handleChange}
          required
          fullWidth
          margin="normal"
        />
        <Button type="submit" variant="contained" color="primary" fullWidth>
          Run Query
        </Button>
      </form>
    </Box>
  );
};

export default RunQuery;

import React, { useState } from 'react';
import { TextField, Button, Typography, Box } from '@mui/material';
import { useDispatch } from 'react-redux';
import { runQuery } from '../redux/actions/queryActions';

const RunQuery = () => {
  const [queryDetails, setQueryDetails] = useState({
    env_name: '',
    db_name: '',
    flow_name: ''
  });

  const dispatch = useDispatch();

  const handleSubmit = async (e) => {
    e.preventDefault();
    dispatch(runQuery(queryDetails));
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setQueryDetails((prevDetails) => ({
      ...prevDetails,
      [name]: value
    }));
  };

  return (
    <Box mt={3}>
      <Typography variant="h5">Run Query</Typography>
      <form onSubmit={handleSubmit}>
        <TextField
          label="Environment Name"
          name="env_name"
          value={queryDetails.env_name}
          onChange={handleChange}
          required
          fullWidth
          margin="normal"
        />
        <TextField
          label="DB Name"
          name="db_name"
          value={queryDetails.db_name}
          onChange={handleChange}
          required
          fullWidth
          margin="normal"
        />
        <TextField
          label="Flow Name"
          name="flow_name"
          value={queryDetails.flow_name}
          onChange={handleChange}
          required
          fullWidth
          margin="normal"
        />
        <Button type="submit" variant="contained" color="primary" fullWidth>
          Run Query
        </Button>
      </form>
    </Box>
  );
};

export default RunQuery;

import { createStore, applyMiddleware } from 'redux';
import thunk from 'redux-thunk';
import rootReducer from './reducers/rootReducer';

const store = createStore(rootReducer, applyMiddleware(thunk));

export default store;

import { combineReducers } from 'redux';
import queryReducer from './queryReducer';

const rootReducer = combineReducers({
  query: queryReducer,
});

export default rootReducer;

const initialState = {
  status: '',
  error: null,
};

const queryReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'QUERY_START':
      return { ...state, status: 'running', error: null };
    case 'QUERY_SUCCESS':
      return { ...state, status: 'success', error: null };
    case 'QUERY_FAILURE':
      return { ...state, status: 'failure', error: action.payload };
    default:
      return state;
  }
};

export default queryReducer;

import axios from 'axios';

export const runQuery = (queryDetails) => async (dispatch) => {
  dispatch({ type: 'QUERY_START' });
  try {
    const response = await axios.post('http://localhost:5000/run_query_api', queryDetails);
    dispatch({ type: 'QUERY_SUCCESS' });
    alert(response.data.message);
  } catch (error) {
    dispatch({ type: 'QUERY_FAILURE', payload: error.response.data.error });
    alert(error.response.data.error);
  }
};

import React from 'react';
import { useSelector } from 'react-redux';
import { Typography, Box } from '@mui/material';

const QueryStatus = () => {
  const { status, error } = useSelector((state) => state.query);

  return (
    <Box mt={3}>
      <Typography variant="h6">Query Status</Typography>
      <Typography variant="body1">Status: {status}</Typography>
      {error && <Typography variant="body1" color="error">Error: {error}</Typography>}
    </Box>
  );
};

export default QueryStatus;

import React from 'react';
import { Provider } from 'react-redux';
import store from './redux/store';
import Layout from './components/Layout';
import AddEnvConfig from './components/AddEnvConfig';
import AddCustomerDetails from './components/AddCustomerDetails';
import RunQuery from './components/RunQuery';
import QueryStatus from './components/QueryStatus';

const App = () => {
  return (
    <Provider store={store}>
      <Layout>
        <AddEnvConfig />
        <AddCustomerDetails />
        <RunQuery />
        <QueryStatus />
      </Layout>
    </Provider>
  );
};

export default App;

import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById('root')
);

reportWebVitals();