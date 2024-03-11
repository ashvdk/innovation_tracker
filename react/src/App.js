import logo from './logo.svg';
import './App.css';
import User from './screens/User/User';
// import { Drawer, FloatButton, Select, Space, Tabs } from 'antd';
import Dashboard from './screens/Dashboard/Dashboard';
import Orders from './screens/Orders/Orders';
import { useState } from 'react';
import Filter from './components/Filter/Filter';
import PlaceOrders from './screens/PlaceOrders/PlaceOrders';
import axios from 'axios';
import { url } from './url';
import { Drawer, FloatButton, Tabs } from 'antd';
import Company from './screens/Overview/Company';

function App() {
  const [open, setOpen] = useState(false);
  const [tabKey, setTabKey] = useState(1)

  //dashboard
  const [isLoadingDashboard, setIsLoadingDashboard] = useState(true)
  const [totalNumberOfOrders, setTotalNumberOfOrders] = useState(0)
  const [totalSales, setTotalSales] = useState(0)
  const onChange = (key) => {
    setTabKey(key);
  };
  const showDrawer = () => {
    setOpen(true);
  };

  const onClose = () => {
    setOpen(false);
  };
  const getDashboardDetails = async (all_states = [], all_cities = []) => {
    const response = await axios.post(url.dashboard, {
      states: all_states,
      cities: all_cities
    })
    setIsLoadingDashboard(false);
    setTotalNumberOfOrders(response.data.data.no_of_orders)
    setTotalSales(response.data.data.total_sales)
    // setIsLoading(false)
    // SetTotalNumberOfOrders(response.data.data.no_of_orders)
    // console.log(response)
  }
  const items = [
    {
      key: '1',
      label: 'Dashboard',
      children: <Dashboard getDashboardDetails={getDashboardDetails}  isLoadingDashboard={isLoadingDashboard} totalNumberOfOrders={totalNumberOfOrders} totalSales={totalSales}/>,
    },
    {
      key: '2',
      label: 'Orders',
      children: <Orders />,
    },
    {
      key: '3',
      label: 'Place Orders',
      children: <PlaceOrders />,
    },
    {
      key: '4',
      label: 'Company',
      children: <Company />,
    }
  ];
  
  return (
    <div>
      <div>Hi</div>
      <Tabs defaultActiveKey={tabKey} items={items} onChange={onChange} />;
      {/* <FloatButton onClick={showDrawer} />
      <Drawer title="Filter" placement="right" onClose={onClose} open={open}>
        <Filter tabKey={tabKey} callTheFilters={tabKey == 1 ? getDashboardDetails : () => console.log("Call for orders")}/>
      </Drawer> */}
    </div>
  );
}

export default App;
