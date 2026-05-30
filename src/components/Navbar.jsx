import { Link } from "react-router-dom";

import "../styles/navbar.css";

function Navbar() {

    return (

        <nav className="navbar">

            <div className="logo">
                NDD Early Detection
            </div>

            <div className="nav-links">

                <Link to="/">Login</Link>
                <Link to="/predict">Prediction</Link>

            </div>

        </nav>
    );
}

export default Navbar;