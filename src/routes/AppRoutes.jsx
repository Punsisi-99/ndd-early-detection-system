import { Routes, Route } from "react-router-dom";

import Signin from "../pages/midwife/Signin";
import Prediction from "../pages/midwife/Prediction";
import Results from "../pages/midwife/Results";
import AdminLogin from "../pages/admin/AdminLogin";
import  History from "../pages/admin/History";


function AppRoutes() {
    return (
        
            <Routes>

                {/* Midwife Routes */}

                <Route path="/" element={<Signin />} />      
                <Route path="/predict" element={<Prediction />} />
                <Route path="/results" element={<Results />} />

                {/* Admin Routes */}
                <Route path="/admin/login" element={<AdminLogin />} />
                <Route path="/admin/history" element={<History />} />
            </Routes>
    );
}

export default AppRoutes;