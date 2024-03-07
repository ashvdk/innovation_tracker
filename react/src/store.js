
import { configureStore } from '@reduxjs/toolkit';
import rootReducer from './rootReducer'; // Create this file

const store = configureStore({
    reducer: rootReducer
});

export default store;