import { useAuth } from '../AuthProvider/AuthProvider'
import { useEffect } from 'react'
import { Navigate, Outlet, Route } from 'react-router-dom'

import { CircularProgress } from '@mui/material';

export const PrivateRoutes = () => {
    const { authLoading, isLoggedIn, checkAuth } = useAuth();

    useEffect(() => {
        checkAuth();
    }, []);

    if (authLoading) {
        return (<CircularProgress />)
    }
    else {
        return (isLoggedIn ? <Outlet/> : <Navigate to='/login'/>)
    }
}

export const PrivateRoute = ({children, ...rest}) => {
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
                { isLoggedIn ? children : <Redirect to="/login" /> }
            </Route>
        )
    }
}
