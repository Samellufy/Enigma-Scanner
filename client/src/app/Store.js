import { configureStore } from "@reduxjs/toolkit";
import userReducer from "../features/user/userSlice";

export default configureStore({
    reducer: {
        user: userReducer // Use the reducer directly
    },
    middleware: (getDefaultMiddleware) =>
        getDefaultMiddleware({
            serializableCheck: false,
        }),
});
