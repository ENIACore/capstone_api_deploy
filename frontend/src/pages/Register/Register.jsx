import React, { useEffect } from 'react';
import { useTheme } from '@mui/material/styles';
import { useNavigate } from "react-router-dom";

//MUI component imports
import { Container, Box, Avatar, Typography, Button, Paper, Alert } from '@mui/material';
import AppRegistrationIcon from '@mui/icons-material/AppRegistration';

//Auth import
import { useAuth } from '../../components/AuthProvider/AuthProvider';

//Form schema/validator imports
import * as Yup from 'yup';

//Form handler imports
import { Formik, Form } from 'formik';

//Custom formik form elements
import TextFieldWrapper from '../../components/TextFieldWrapper/TextFieldWrapper';

import axiosInstance from '../../axios';

const validationSchema = Yup.object({
    email: Yup.string('Enter your email').email('Enter a valid email').required('Email is required'),
    username: Yup.string('Enter your username').min(4, 'Username should be of minimum 4 characters length').required('Username is required'),
    first_name: Yup.string('Enter your first name').required('First name is required'),
    last_name: Yup.string('Enter your last name').required('Last name is required'),
    password: Yup.string('Enter your password').min(8, 'Password should be of minimum 8 characters length').required('Password is required'),
    confirm_password: Yup.string().oneOf([Yup.ref('password'), null], 'Passwords must match')
});

const initialValues = {
    email: '',
    username: '',
    first_name: '',
    last_name: '',
    password: '',
    confirm_password: '',
};

function Register() {
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
        <Container component="main" maxWidth="sm"> 
        <Box 
            component="img" 
            alt="Logo"
            sx={{
                height: 100,
                width: 200,
                mb: 0,
            }}
            src="logo_no_bg.png"
        />
        <Paper elevation={4} sx={{ p: 4, }}>
            <Box display="flex" alignItems="center" flexDirection="column">

                <Avatar sx={{ bgcolor: 'secondary.main' }}>
                    <AppRegistrationIcon />
                </Avatar>

                <Typography component="h1" variant="h5" sx={{ mt: 2 }}>
                    Register
                </Typography>

                <Formik
                    initialValues={{...initialValues}}
                    validationSchema={validationSchema}
                    onSubmit={async (values, {setStatus, setErrors}) => {
                        try {
                            const response = await axiosInstance.post('/users/', values);
                            navigate('/');
                        }
                        catch (error) {

                            if (error.response) {
                                setErrors(error.response.data);
                            }
                            else {
                                setStatus({message: 'Error sending request to server'});
                            }
                        }
                    }}
                >
                {({ status }) => (
                <Form>

                    <Box sx={{ mt: 2, mb: 2 }}>
                        { (status && status.message) ? <Alert severity="error" sx={{ mb: 2 }}>{status.message}</Alert> : null }
                        <TextFieldWrapper
                            required
                            id="email"
                            name="email"
                            label="Email"
                            sx={{ mb: 2 }}
                        />
                        <TextFieldWrapper
                            required
                            id="username"
                            name="username"
                            label="Username"
                            sx={{ mb: 2 }}
                        />
                        <TextFieldWrapper
                            required
                            id="first_name"
                            name="first_name"
                            label="First Name"
                            sx={{ mb: 2 }}
                        />
                        <TextFieldWrapper
                            required
                            id="last_name"
                            name="last_name"
                            label="Last Name"
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
                        <TextFieldWrapper
                            required
                            id="confirm_password"
                            name="confirm_password"
                            label="Confirm Password"
                            type="password"
                            sx={{ mb: 2 }}
                        />
                        <Button color="primary" variant="contained" fullWidth type="submit" sx={{ mb: 2 }}>
                            Submit
                        </Button>
                    </Box>

                </Form>
                )}
                </Formik>
            </Box>
        </Paper>
        </Container>
    );

}

export default Register;
