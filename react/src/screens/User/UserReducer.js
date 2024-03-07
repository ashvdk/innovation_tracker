import { createSlice } from "@reduxjs/toolkit";


const userReducer = createSlice({
    name: "user",
    initialState: {
        isLoading: true,
        data: null,
        error: null
    },
    reducers: {
        getData: (state) => {
            return {
                data: {
                    name: "Ashwin",
                    email: "ashwinvdrk@gmail.com"
                }
            }
        }
    }
}) 

export const { getData } = userReducer.actions

export default userReducer.reducer;