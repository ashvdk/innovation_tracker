import { combineReducers } from "redux";
import userReducer from "./screens/User/UserReducer.js";

const rootReducer = combineReducers({
    userReducer: userReducer
})

export default rootReducer
