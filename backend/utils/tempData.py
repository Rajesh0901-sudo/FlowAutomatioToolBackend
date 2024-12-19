// src/AddEnvConfig.js
import React, { useState } from 'react';
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
    <form onSubmit={handleSubmit}>
      <h2>Add Environment Configuration</h2>
      <label>
        Environment Name:
        <input type="text" value={envName} onChange={(e) => setEnvName(e.target.value)} required />
      </label>
      <label>
        DB User Name:
        <input type="text" name="db_user_name" value={configurations.db_user_name} onChange={handleChange} required />
      </label>
      <label>
        DB Password:
        <input type="password" name="db_password" value={configurations.db_password} onChange={handleChange} required />
      </label>
      <label>
        DB Host:
        <input type="text" name="db_host" value={configurations.db_host} onChange={handleChange} required />
      </label>
      <label>
        Service Name:
        <input type="text" name="service_name" value={configurations.service_name} onChange={handleChange} required />
      </label>
      <label>
        New Service Name:
        <input type="text" name="new_service_name" value={configurations.new_service_name} onChange={handleChange} required />
      </label>
      <button type="submit">Add Environment</button>
    </form>
  );
};

export default AddEnvConfig;

// src/AddCustomerDetails.js
import React, { useState } from 'react';
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
    <form onSubmit={handleSubmit}>
      <h2>Add Customer Details</h2>
      <label>
        Individual ID:
        <input type="text" name="individualId" value={customerDetails.individualId} onChange={handleChange} required />
      </label>
      <label>
        Customer Bill Spec ID:
        <input type="text" name="customerBillSpecId" value={customerDetails.customerBillSpecId} onChange={handleChange} required />
      </label>
      <label>
        Customer Address ID:
        <input type="text" name="customerAddressId" value={customerDetails.customerAddressId} onChange={handleChange} required />
      </label>
      <label>
        Customer Account ID:
        <input type="text" name="customerAccountId" value={customerDetails.customerAccountId} onChange={handleChange} required />
      </label>
      <label>
        Name:
        <input type="text" name="name" value={customerDetails.name} onChange={handleChange} required />
      </label>
      <label>
        ID:
        <input type="text" name="ID" value={customerDetails.ID} onChange={handleChange} required />
      </label>
      <button type="submit">Add Customer</button>
    </form>
  );
};

export default AddCustomerDetails;

// src/RunQuery.js
import React, { useState } from 'react';
import axios from 'axios';

const RunQuery = () => {
  const [queryDetails, setQueryDetails] = useState({
    env_name: '',
    db_name: '',
    flow_name: ''
  });

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post('http://localhost:5000/run_query_api', queryDetails);
      alert(response.data.message);
    } catch (error) {
      alert(error.response.data.error);
    }
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setQueryDetails((prevDetails) => ({
      ...prevDetails,
      [name]: value
    }));
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Run Query</h2>
      <label>
        Environment Name:
        <input type="text" name="env_name" value={queryDetails.env_name} onChange={handleChange} required />
      </label>
      <label>
        DB Name:
        <input type="text" name="db_name" value={queryDetails.db_name} onChange={handleChange} required />
      </label>
      <label>
        Flow Name:
        <input type="text" name="flow_name" value={queryDetails.flow_name} onChange={handleChange} required />
      </label>
      <button type="submit">Run Query</button>
    </form>
  );
};

export default RunQuery;


// src/App.js
import React from 'react';
import AddEnvConfig from './AddEnvConfig';
import AddCustomerDetails from './AddCustomerDetails';
import RunQuery from './RunQuery';

const App = () => {
  return (
    <div>
      <h1>Flow Automation Tool</h1>
      <AddEnvConfig />
      <AddCustomerDetails />
      <RunQuery />
    </div>
  );
};

export default App;