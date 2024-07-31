import { useState, useContext, createContext, useEffect } from 'react'

import axiosInstance from '../../axios';

/*
    * Axios responses have this format
    * response.data 
    * response.status
    * response.headers 
*/

const AuthContext = createContext();

export function useAuth() {
    return useContext(AuthContext);
}

export function AuthProvider(props) {
    const [ authUser, setAuthUser ] = useState(null);
    const [ isLoggedIn, setIsLoggedIn ] = useState(false);
    const [ authLoading, setAuthLoading ] = useState(true);

    async function logout() {

        try {

            setAuthLoading(true);

            const response = await axiosInstance.post('/logout');
            setAuthUser(null);
            setIsLoggedIn(false);

            setAuthLoading(false);

            return response;

        }
        catch (error) {

            setAuthLoading(true);

            setAuthUser(null);
            setIsLoggedIn(false);

            setAuthLoading(false);

            if (error.response) {
                return error.response;
            }
            else if (error.request) {
                return error.request;
            }
            else {
                return error.message;
            }

        }
    }

    async function login(values) {
        try {

            setAuthLoading(true);

            const response = await axiosInstance.post('/login', values);
            setAuthUser(response.data);
            setIsLoggedIn(true);

            setAuthLoading(false);

            return response;
        }
        catch (error) {

            setAuthLoading(true);

            setAuthUser(null);
            setIsLoggedIn(false);

            setAuthLoading(false);

            throw error;

        }
    }

    async function checkAuth() {
        try {

            setAuthLoading(true);

            const response = await axiosInstance.get('/user');
            setAuthUser(response.data);
            setIsLoggedIn(true);

            setAuthLoading(false);

        }
        catch (error) {

            setAuthLoading(true);

            setAuthUser(null);
            setIsLoggedIn(false);

            setAuthLoading(false);

        }

    }

    const value = {
        checkAuth,
        login,
        logout,
        authUser,
        setAuthUser,
        isLoggedIn,
        setIsLoggedIn,
        authLoading,
        setAuthLoading,
    };

    return (
        <AuthContext.Provider value={value}>
            {props.children}
        </AuthContext.Provider>
    )
}
