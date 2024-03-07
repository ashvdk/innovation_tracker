import React, { useEffect } from 'react'
import PropTypes from 'prop-types'
import { useDispatch, useSelector } from 'react-redux'
import store from '../../store'
import { getData } from './UserReducer.js'
import axios from 'axios'

const User = () => {
    const {data, isLoading, error} = useSelector(store => store.userReducer)
    const dispatch = useDispatch()
    useEffect(() => {
        dispatch(getData())
        getDashboard()
    }, [])
    const getDashboard = async () => {
        const response = await axios.post('http://127.0.0.1:8000/orders');
        console.log(response)
    }
    return ( 
        <>
            {data ? <>
                <div>User</div>
                <div>{data.name}</div>
                <div>{data.email}</div>
            </> : ""}
        </>
    )
}


export default User