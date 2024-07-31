import React from 'react';
import { useTheme } from '@mui/material/styles';
import { useNavigate } from "react-router-dom";

//MUI component imports
import { Container, Box, Button } from '@mui/material';

import { useAuth } from '../../components/AuthProvider/AuthProvider';

function Landing() {
    const theme = useTheme();
    const navigate = useNavigate();

    const { logout } = useAuth();


    const logoutRedirect = () => {
        logout();
        return navigate('/login');
    }

    const loginPage = () => {

        return navigate('/login');
    }

    const registerPage = () => {

        return navigate('/register');
    }

    const mapPage = () => {

        return navigate('/map');
    }

    return (
        // Container centers login card
        <Container component="main" maxWidth="xs"> 
        <Box 
            component="img" 
            alt="Logo"
            sx={{
                height: 175,
                width: 175,
                mb: 0,
            }}
            src="logo_no_bg.png"
        />
        <p>Kyles Page</p>
        <Button color="primary" variant="contained" fullWidth onClick={logoutRedirect} sx={{ mb: 2 }}>
            Logout
        </Button>
        <Button color="primary" variant="contained" fullWidth onClick={loginPage} sx={{ mb: 2 }}>
            Sign in page
        </Button>
        <Button color="primary" variant="contained" fullWidth onClick={mapPage} sx={{ mb: 2 }}>
            Map
        </Button>
        <Button color="primary" variant="contained" fullWidth onClick={registerPage} sx={{ mb: 2 }}>
            Register page
        </Button>
        </Container>
    );

}

export default Landing;
