import { useAuth } from '../AuthProvider/AuthProvider'
import { useEffect } from 'react'
import { Navigate, Outlet, Route } from 'react-router-dom'

import { CircularProgress } from '@mui/material';

export const UnauthRoutes = () => {
    const { authLoading, isLoggedIn, checkAuth } = useAuth();

    useEffect(() => {
        checkAuth();
    }, []);

    if (authLoading) {
        return (<CircularProgress />)
    }
    else {
        return (isLoggedIn ? <Navigate to='/'/> : <Outlet/>)
    }
}

export const UnauthRoute = ({children, ...rest}) => {
    const { authLoading, isLoggedIn, checkAuth } = useAuth();

    useEffect(() => {
        checkAuth();
    }, []);

    if (authLoading) {
        return (<CircularProgress />)
    }
    else {
        return(
            <Route {...rest}>
                { isLoggedIn ? <Redirect to="/" /> : children }
            </Route>
        )
    }
}
