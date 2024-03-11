import { Button, Select } from 'antd'
import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { url } from '../../../url'

function Filter() {
    const [filterToChange, setFilterToChange] = useState(["country", "company", "segment", "product", "variant", "color"])
    const [payload, setPayload] = useState({})
    const [filters, setFilters] = useState([
        {
            title: "Country",
            key: "country",
            options: []
        },
        {
            title: "Company",
            key: "company",
            options: []
        },
        {
            title: "Segment",
            key: "segment",
            options: []
        },
        {
            title: "Product",
            key: "product",
            options: []
        },
        {
            title: "Variant",
            key: "variant",
            options: []
        },
        {
            title: "Color",
            key: "color",
            options: []
        }
    ])
    useEffect(() => {
        getCompanyOverviewFilters()
    }, [])
    const getCompanyOverviewFilters = async (payload = {}) => {
        try {
            const response = await axios.post(url.companyOverview.filters, payload)
            console.log(response.data)
            const { country, company, segment, products, variants, colors } = response.data
            let arr = [country, company, segment, products, variants, colors]
            let tempFilters = [...filters]
            filterToChange.forEach((key, index) => {
                tempFilters[index] = {...tempFilters[index], options: [...arr[index]]}
            })
            // tempFilters[0] = {...tempFilters[0], options: [...country]}
            // tempFilters[1] = {...tempFilters[1], options: [...company]}
            // tempFilters[2] = {...tempFilters[2], options: [...segment]}
            // tempFilters[3] = {...tempFilters[3], options: [...products]}
            // tempFilters[4] = {...tempFilters[4], options: [...variants]}
            // tempFilters[5] = {...tempFilters[5], options: [...colors]}
            setFilters([
                ...tempFilters
            ])
        }
        catch(err){
            console.log("error")
        }
    }
    const getDataForFilter = async (key, value) => {
        if(key == "country"){
            await getCompanyOverviewFilters({
                ...payload,
                "country": value
            })
            setPayload({
                ...payload,
                "country": value
            })
            setFilterToChange(["company", "segment", "product", "variant", "color"])
        }
        else if(key == "company"){
            await getCompanyOverviewFilters({
                ...payload,
                "company": value
            })
            setPayload({
                ...payload,
                "company": value
            })
            setFilterToChange(["company", "segment", "product", "variant", "color"])
        }
    }
    return (
        <div>
            {filters.map((filter) => {
                return (
                    <div style={{marginBottom: "25px"}}>
                        <div>{filter.title}</div>
                        <Select 
                            mode="" 
                            showSearch
                            style={{ width: '100%' }}
                            placeholder="Please select"
                            options={filter.options}
                            onChange={e => getDataForFilter(filter.key, e)}
                        />
                    </div>
                    
                )
            })}
            <div style={{display: "flex"}}>
                <div style={{flex: 1, }}>
                    <Button type="primary"  style={{width: "100%"}} danger>
                        Reset
                    </Button>
                </div>
                <div style={{width: "10px"}}></div>
                <div style={{flex: 1}}>
                    <Button type="primary" style={{width: "100%"}}>Apply</Button>
                </div>
            </div>
        </div>
    )
}

export default Filter