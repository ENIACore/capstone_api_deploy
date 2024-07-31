//Router imports
import { Routes, Route } from "react-router-dom"

//Component imports
import BackgroundMap from './components/BackgroundMap/BackgroundMap'
import Login from './pages/Login/Login'
import Register from './pages/Register/Register'
import Landing from './pages/Landing/Landing'
import { PrivateRoutes } from './components/PrivateRoute/PrivateRoute'

//Css imports
import './styles/App.css'

function App() {
    const location = { lat: 30.5446, lng: -87.2120 };
    const mapId = import.meta.env.VITE_GOOGLE_MAPS_MAP_ID
    const apiKey = import.meta.env.VITE_GOOGLE_MAPS_API_KEY

    return (
        <Routes>
        { /* <Route path='/' element={ <BackgroundMap location={location} /> } /> */ }
            <Route element={<PrivateRoutes/>}>
                <Route path='/' element={ <Landing /> } />
                <Route path='/map' element={ <BackgroundMap location={location} map_id={mapId} api_key={apiKey} /> } />
            </Route>
            
            <Route path='/register' element={ <Register /> } />
            <Route path='/login' element={ <Login /> } />

        </Routes>
    );

}

export default App;
