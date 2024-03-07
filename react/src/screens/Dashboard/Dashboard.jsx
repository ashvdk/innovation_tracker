import axios from 'axios'
import React, { useEffect, useState } from 'react'
import { url } from '../../url'
import './Dashboard.css'

function Dashboard({getDashboardDetails, isLoadingDashboard = true, totalNumberOfOrders = 0, totalSales = 0}) {
  useEffect(() => {
    getDashboardDetails()
  }, [])
  // states: ['CA', 'GA'],
  // cities: ['Fresno', 'Los Angeles', 'San Diego', 'San Francisco', 'San Jose']
  
  if(isLoadingDashboard){
    return <div>...Loading</div>
  }
  return (
    <div style={{display: "flex"}}>
      <div class="card">
        <p class="total-orders">Total Orders</p>
        <div>{totalNumberOfOrders}</div>
      </div>
      <div style={{width: "10px"}}></div>
      <div class="card">
        <p class="total-orders">Total Sales</p>
        <div>{totalSales}</div>
      </div>
    </div>
  )
}

export default Dashboard