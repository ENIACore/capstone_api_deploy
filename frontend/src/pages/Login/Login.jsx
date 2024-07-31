import React, { useEffect } from 'react';
import { useNavigate } from "react-router-dom";

//MUI component imports
import { Container, Box, Avatar, Typography, Button, Link, Paper, Alert } from '@mui/material';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined'; 
import { useTheme } from '@mui/material/styles';

//Form schema/validator imports
import * as Yup from 'yup';

//Form handler imports
import { Formik, Form } from 'formik';

//Auth import
import { useAuth } from '../../components/AuthProvider/AuthProvider';

//Custom formik form elements
import TextFieldWrapper from '../../components/TextFieldWrapper/TextFieldWrapper';

const validationSchema = Yup.object({
    email: Yup.string('Enter your email').email('Enter a valid email').required('Email is required'),
    password: Yup.string('Enter your password').min(8, 'Password should be of minimum 8 characters length').required('Password is required'),
});

const initialValues = {
    email: '',
    password: '',
};

function Login() {
    const theme = useTheme();
    const navigate = useNavigate();

    const { login, isLoggedIn, checkAuth } = useAuth();

    //Use this instead of UnauthRoute because form affects IsLoggedIn, so this prevents page reload on form submission
    useEffect(() => {
        checkAuth();
        if (isLoggedIn) {
            navigate('/');
        }
    }, [isLoggedIn]);

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
        <Paper elevation={4} sx={{ p: 4, borderRadius: 8, }}>
            <Box display="flex" alignItems="center" flexDirection="column">
                <Avatar sx={{ bgcolor: 'secondary.main' }}>
                    <LockOutlinedIcon />
                </Avatar>
                <Typography component="h1" variant="h5" sx={{ mt: 2 }}>
                    Sign in
                </Typography>

                <Formik
                    initialValues={{...initialValues}}
                    validationSchema={validationSchema}
                    onSubmit={async (values, {setStatus}) => {
                        try {
                            await login(values);
                            navigate('/');
                        }
                        catch (error) {

                            if (error.response) {
                                setStatus({message: error.response.data['message']});
                            }
                            else {
                                setStatus({message: 'Error sending request to server'});
                            }
                        }
                    }}
                >
                {({ status }) => (
                <Form>
                    { (status && status.message) ? <Alert severity="error">{status.message}</Alert> : null }
                    <Box sx={{ mt: 2, mb: 2 }}>
                        <TextFieldWrapper
                            required
                            id="email"
                            name="email"
                            label="Email"
                            sx={{ mb: 2 }}
                        />
                        <TextFieldWrapper
                            required
                            id="password"
                            name="password"
                            label="Password"
                            type="password"
                            sx={{ mb: 2 }}
                        />
                    </Box>
                    <Button color="primary" variant="contained" fullWidth type="submit" sx={{ mb: 2 }}>
                        Submit
                    </Button>
                </Form>
                )}
                </Formik>

                <Link href="/register" variant="body2">
                    Don't have an account? Sign Up
                </Link>

            </Box>
        </Paper>
        </Container>
    );

}

export default Login;
