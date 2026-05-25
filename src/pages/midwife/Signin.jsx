import { useState } from "react";
import { useNavigate } from "react-router-dom";

function Signin() {
    const navigate = useNavigate();
    
    const [email, setEmail] = useState("");

    const handleLogin = (e) => {
        e.preventDefault();

        //temporary login logic, replace with actual authentication
        if (email) {
            navigate("/predict");
        }
    };

    return(
        <div className="signin-container">
            <div className="signin-card">

                <h1>
                    NDD Early Detection Screening System
                </h1>

                <p className="subtitle">
                    Sign in to your account
                </p>

                <form onSubmit ={handleLogin}>

                    <label>Email:</label>

                    <input 
                        type = "email"
                        placeholder="Enter your email"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                        required
                    />

                    <button type="submit">Sign In</button>

                </form>

            </div>
        </div>

    );
}

export default Signin;