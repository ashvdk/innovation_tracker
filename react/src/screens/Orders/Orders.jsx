import axios from 'axios';
import React, { useState, useEffect } from 'react'
import { url } from '../../url';
import { Table } from 'antd';

function Orders() {
  const [isLoading, setIsLoading] = useState(true);
  const [data, setData] = useState(null);
  useEffect(() => {
    getOrders();
  }, [])
  const getOrders = async () => {
    const response = await axios.post(url.orders);
    setIsLoading(false)
    setData(response.data.data)
    console.log(response)
  }
  if(isLoading){
    return <div>...Loading</div>
  }
  let columns = [

    {
      title: "Product Name",
      dataIndex: "product",
      key: "product",
    },
    {
      title: "Quantity Ordered",
      dataIndex: "quantity_ordered",
      key: "quantity_ordered",
    },
    {
      title: "Price",
      dataIndex: "price_each",
      key: "price_each",
    },
    {
      title: "Ordered Date",
      dataIndex: "order_date",
      key: "order_date",
    },
    {
      title: "Purchase Address",
      dataIndex: "purchase_address",
      key: "purchase_address",
    }
  ]
  return <Table columns={columns} dataSource={data ? data : []} bordered={true} size='medium'/>
}

export default Orders