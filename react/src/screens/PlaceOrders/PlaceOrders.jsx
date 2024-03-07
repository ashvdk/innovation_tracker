import { Button, Select, Table } from 'antd';
import axios from 'axios';
import React, { useEffect, useState } from 'react'
import { url } from '../../url';
const options = [];

for (let i = 10; i < 36; i++) {
  options.push({
    label: i.toString(36) + i,
    value: i.toString(36) + i,
  });
}
let columns = [
    {
      title: "Product Name",
      dataIndex: "product",
      key: "product",
    },
    {
      title: "Price",
      dataIndex: "price",
      key: "price",
    },
    {
      title: "Quantity",
      dataIndex: "quantity_ordered",
      key: "quantity_ordered",
    },
    {
      title: "Ordered Date",
      dataIndex: "order_date",
      key: "order_date"
    },
  ]
function getRandomNumberBetween1And5() {
  // Generate a random number between 0 and 1, then scale it to be between 1 and 5.
  const randomNumber = Math.floor(Math.random() * 5) + 1;
  return randomNumber;
}
function getRandomDateTime() {
  // Define the start and end dates
  const startDate = new Date('2020-01-01');
  const endDate = new Date('2023-09-30');

  // Calculate the time range in milliseconds
  const timeRange = endDate.getTime() - startDate.getTime();

  // Generate a random time within the time range
  const randomTime = Math.random() * timeRange;

  // Create a new Date object with the random time
  const randomDateTime = new Date(startDate.getTime() + randomTime);

  return randomDateTime;
}

function PlaceOrders() {
  const [isLoading, setIsLoading] = useState(true)
  const [allProducts, setAllProducts] = useState([])
  const [selectedProducts, setSelectedProducts] = useState([])
  const [finalProduct, setFinalProduct] = useState([])
  const [street, setStreet] = useState([])
  const [selectedStreet, setSelectedStreet] = useState(null)
  const [state, setState] = useState([])
  const [city, setCity] = useState([])
  const [selectedCity, setSelectedCity] = useState(null)
  const [selectedState, setSelectedState] = useState(null);
  useEffect(() => {
    getDetails()
  }, [])
  useEffect(() => {
    if(state.length > 0 && !selectedState){
      let selectedStateTemp = state[0].value;
      console.log(selectedStateTemp)
      setSelectedState(selectedStateTemp)
    }
    
  }, [state])
  useEffect(() => {
    let products = [];
    let order_date = getRandomDateTime().toLocaleDateString()
    selectedProducts.forEach((product) => {
      let product_1 = allProducts.filter((tempProduct) => tempProduct.id == product)[0]
      product_1["order_date"] = order_date;
      product_1["quantity_ordered"] = getRandomNumberBetween1And5();
      products.push(product_1)
      //console.log(product_1)
    })
    if(products.length > 0){
      setFinalProduct(products)
    }
  }, [selectedProducts])
  
  const placeNOrder = async () => {
    const response = await axios.post(url.create_order, {
      products: finalProduct,
      street: selectedStreet,
      city: selectedCity,
      state: selectedState
    })
    console.log(finalProduct)
    console.log(selectedStreet)
    console.log(selectedCity)
    console.log(selectedState)
    console.log(response.data)
  }
  const getDetails = async () => {
    const response = await axios.get(url.details)
    console.log(response)
    setIsLoading(false)
    setAllProducts(response.data.data.products)
    setStreet(response.data.data.address)
    setCity(response.data.data.city)
    setState(response.data.data.state)
  }
  const getSelectedProducts = () => {
    let products = [];
    let order_date = getRandomDateTime().toLocaleDateString()
    selectedProducts.forEach((product) => {
      let product_1 = allProducts.filter((tempProduct) => tempProduct.id == product)[0]
      product_1["order_date"] = order_date;
      product_1["quantity_ordered"] = getRandomNumberBetween1And5();
      products.push(product_1)
      //console.log(product_1)
    })
    if(products.length > 0){
      setFinalProduct(products)
    }
    //setFinalProduct(products)
    console.log(products)
    return products;
  }
    //i need products, state and city
  if(isLoading){
    return <div>...Loading</div>
  }
  return (
    <div>
      <div>Products:</div>
      <Select
        mode="multiple"
        allowClear
        style={{ width: '100%' }}
        placeholder="Please select"
        //defaultValue={['a10', 'c12']}
        // value={stateValues}
        onChange={(value) => setSelectedProducts(value)}
        options={allProducts.map((product) => ({
          label: product.product,
          value: product.id
        }))}
      />
      <br />
      <br />
      <Table columns={columns} dataSource={finalProduct} bordered={true} size='medium'/>
      <br />
      <br />
      <div style={{display: "flex"}}>
          <div style={{flex: 1}}>
              <div>State:</div>
              <Select
                  style={{ width: '100%' }}
                  placeholder="Please select"
                  //defaultValue={['a10', 'c12']}
                  // value={stateValues}
                  onChange={(value) => setSelectedState(value)}
                  options={state}
              />
          </div>
          <div style={{flex: 1}}>
              <div>City:</div>
              <Select
                  style={{ width: '100%' }}
                  placeholder="Please select"
                  //defaultValue={['a10', 'c12']}
                  // value={stateValues}
                  onChange={(value) => setSelectedCity(value)}
                  options={selectedState ? city[selectedState] : []}
              />
          </div>
          <div style={{flex: 1}}>
              <div>Street:</div>
              <Select
                  style={{ width: '100%' }}
                  placeholder="Please select"
                  //defaultValue={['a10', 'c12']}
                  // value={stateValues}
                  onChange={(value) => setSelectedStreet(value)}
                  options={street}
              />
          </div>
      </div>
      <br />
      <br />
      <div>
          <Button type="primary" block onClick={placeNOrder}>
              Order
          </Button>
      </div>
    </div>
  )
}

export default PlaceOrders