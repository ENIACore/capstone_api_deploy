import React from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter } from "react-router-dom";
import App from './App'
import './styles/index.css'
import { themeOptions } from './styles/theme'
import { ThemeProvider, createTheme, responsiveFontSizes } from '@mui/material/styles';

import { AuthProvider } from './components/AuthProvider/AuthProvider';

let theme = createTheme(themeOptions);
theme = responsiveFontSizes(theme);

ReactDOM.createRoot(document.getElementById('root')).render(
    <BrowserRouter>
        <AuthProvider>
        <ThemeProvider theme={theme}>
            <App />
        </ThemeProvider>
        </AuthProvider>
    </BrowserRouter>,
)
