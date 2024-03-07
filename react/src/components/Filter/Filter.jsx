import React, { useEffect, useState } from 'react'
import { Button, Divider, Drawer, FloatButton, Select, Space, Tabs } from 'antd';
import axios from 'axios';
import { url } from '../../url';
const options = [];

for (let i = 10; i < 36; i++) {
  options.push({
    label: i.toString(36) + i,
    value: i.toString(36) + i,
  });
}
function Filter({ tabKey, callTheFilters }) {
    const [isLoading, setIsLoading] = useState(true);
    const [state, setState] = useState([]);
    const [stateValues, setstateValues] = useState([])
    const [city, setCity] = useState([]);
    const [cityValues, setCityValues] = useState([])
    useEffect(() => {
        //dispatch(getData())
        getFilters()
    }, [])
    useEffect(() => {
        setCity([])
    }, [stateValues])
    
    const getFilters = async (all_states = [], all_cities = []) => {
        const response = await axios.post(url.filters, {
            state: all_states,
            cities: all_cities
        });
        setIsLoading(false)
        setState([...response.data.data.state])
        setCity([...response.data.data.city])
        console.log(response.data.data)
    }
    const handleChange = (value) => {
        console.log(`selected ${value}`);
    };
    const getFilterBasedOnState = async () => {
        console.log(stateValues)
        setIsLoading(true)
        getFilters(stateValues)
        //console.log(response)
    }
    const getFilterBasedOnCity = async () => {
        console.log(cityValues);
        console.log(stateValues)
        setIsLoading(true)
        getFilters(stateValues, cityValues)
    }
    const applyFilters = () => {
        console.log("Apply the filters")
        console.log(tabKey)
        console.log(stateValues)
        console.log(cityValues)
        console.log(callTheFilters)
        callTheFilters(stateValues, cityValues)
    }
    if(isLoading){
        return <div>...Loading</div>
    }
    return (
        <Space style={{ width: '100%' }} direction="vertical">
            <div>State:</div>
            <Select
                mode="multiple"
                allowClear
                style={{ width: '100%' }}
                placeholder="Please select"
                //defaultValue={['a10', 'c12']}
                value={stateValues}
                onChange={(value) => setstateValues(value)}
                options={state}
                dropdownRender={(menu) => (
                    <>
                        {menu}
                        <Divider style={{ margin: '8px 0' }} />
                        <Space style={{ padding: '0 8px 4px' }}>
                            {/* <Input
                            placeholder="Please enter item"
                            ref={inputRef}
                            value={name}
                            onChange={onNameChange}
                            /> */}
                            <Button type="text" onClick={getFilterBasedOnState}>
                                Apply
                            </Button>
                        </Space>
                    </>
                )}
            />
            <br />
            <div>City:</div>
            <Select
                mode="multiple"
                allowClear
                style={{ width: '100%' }}
                placeholder="Please select"
                //defaultValue={['a10', 'c12']}
                onChange={(value) => setCityValues(value)}
                options={city}
                // dropdownRender={(menu) => (
                //     <>
                //         {menu}
                //         <Divider style={{ margin: '8px 0' }} />
                //         <Space style={{ padding: '0 8px 4px' }}>
                //             {/* <Input
                //             placeholder="Please enter item"
                //             ref={inputRef}
                //             value={name}
                //             onChange={onNameChange}
                //             /> */}
                //             <Button type="text" onClick={getFilterBasedOnCity}>
                //                 Apply
                //             </Button>
                //         </Space>
                //     </>
                // )}
            />
            <Button type="primary" block onClick={applyFilters}>
                Apply
            </Button>
        </Space>
    )
}

export default Filter