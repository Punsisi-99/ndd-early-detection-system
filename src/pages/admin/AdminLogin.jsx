import { useState } from "react";
import { useNavigate } from "react-router-dom";
import API from "../../services/api";

function AdminLogin() {
    
    const navigate = useNavigate();

    const [username,  setUsername] = useState("");

    const [password, setPassword] = useState("");

    const [loading, setLoading] = useState(false);

    const handleLogin = async (e) => {

        e.preventDefault();

        setLoading(true);

        try {

            const  formData = new FormData();

            formData.append("username", username);

            formData.append("password", password);

            const response = await API.post("/login", formData);

            localStorage.setItem("token", response.data.access_token);

            alert("Admin login successfull!");

            navigate("/admin/history");
        }

        catch (error) {
            console.error(error);

            alert("invalid Admin Credentials");
        }

        finally {

            setLoading(false);
        }
    };

    return (

        <div className="signin-container">

            <div className="signin-card">

                <h1>Admin Login</h1>

                <p className="subtitle">
                    Authorized access only
                </p>

                <form onSubmit={handleLogin}>

                    <label>Username:

                    <input
                        type="text"
                        placeholder="Enter username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)
                        }
                        required
                    />
            
                    </label>

                    <label>Password:</label>

                    <input
                        type="password"
                        placeholder="Enter password"
                        value={password}
                        onChange={(e) =>
                            setPassword(e.target.value)
                        }
                        required
                    />

                    <button type="submit"
                            disabled={loading}
                    >
                        
                        {loading
                            ? "Logging in..."
                            : "Login"
                        }

                    </button>

                </form>
            </div>
        </div>
    );
}

export default AdminLogin;