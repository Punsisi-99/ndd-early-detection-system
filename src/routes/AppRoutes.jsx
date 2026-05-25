import { BrowserRouter, Routes, Route } from "react-router-dom";

import Signin from "../pages/midwife/Signin";
import Prediction from "../pages/midwife/Prediction";
import Results from "../pages/midwife/Results";
import  History from "../pages/admin/History";

function AppRoutes() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Signin />} />      
                <Route path="/predict" element={<Prediction />} />
                <Route path="/results" element={<Results />} />
                <Route path="/admin/history" element={<History />} />
            </Routes>
        </BrowserRouter>
    );
}

export default AppRoutes;