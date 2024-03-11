import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { url } from '../../url'
import { Drawer, FloatButton } from 'antd'
import Filter from './Filters/Filter'

const Company = () => {
    const [open, setOpen] = useState(false)
    useEffect(() => {
        getCompanyAnalysisOverview()
    }, [])
    const getCompanyAnalysisOverview = async () => {
        try{
            // const response = await axios.post(url.companyOverview.main)
            // console.log(response.data)
        }
        catch(err){
            console.log("Error occured")
        }
        
    }
    const showDrawer = () => setOpen(prevValue => !prevValue)
    return (
        <div>
            Company
            <FloatButton onClick={showDrawer} />
            <Drawer title="Filters" placement="right" onClose={showDrawer} open={open}>
                <Filter />
            </Drawer>
        </div>
    )
}

export default Company