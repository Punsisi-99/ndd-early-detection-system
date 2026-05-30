import { useEffect,  useState } from "react";
import { useNavigate } from "react-router-dom";

import API from "../../services/api";



function History() {

    const navigate = useNavigate();

    const [records, setRecords] = useState([]);

    const [search, setSearch] = useState("");

    const [loading, setLoading] = useState(true);
    
    useEffect(() => {

        const token = localStorage.getItem("token");

        if (!token) {
            alert("Admin Login Required");

            navigate("/admin/login");

            return;
        }

        fetchHistory();
    }, []);

    const fetchHistory = async () => {

        try {

            const response = await API.get(
                "/predictions",
                    {
                    headers:{
                        Authorization: 
                            `Bearer ${localStorage.getItem("token")}`
                    }
                }
            );
            
            setRecords(response.data);
        }

        catch (error) {

            console.error(error);

            alert("Failed to load history. Please try again.");
        }

        finally {
            setLoading(false);
        }
    };

    const filteredRecords = records.filter((item) =>
    
        item.name
            ?.toLowerCase()
            .includes(search.toLowerCase())
        );

    return (
        <div className="history-container">

            <div className="history-card">

                <h1>Prediction History</h1>

                <input
                    type="text"
                    placeholder="Search by name..."
                    value={search}
                    onChange={(e) => setSearch(e.target.value)
                    }
                    className="search-box"
                />

                {loading ?(
                    <p>Loading Records...</p>
                ) : (

                <table>

                    <thead>

                        <tr>

                            <th>Name</th>
                            <th>Age</th>
                            <th>Gender</th>
                            <th>Diagnosis</th>
                            <th>Risk Factors</th>
                            <th>Date</th>
                        </tr>
                    </thead>

                    <tbody>

                        {filteredRecords.map((item) => (

                            <tr key={item.id}>

                                <td>{item.name}</td>

                                <td>{item.age}</td>

                                <td>{item.gender}</td>

                                <td
                                    className={item.diagnosis === "Healthy"
                                        ? "healthy"
                                        : "risk"
                                    }
                                >
                                    {item.diagnosis}
                                </td>

                                <td>
                                    {item.risk_factors || "N/A"}
                                </td>

                                <td>
                                    {new Date(
                                        item.created_at
                                    ).toLocaleDateString()}
                                </td>
                            </tr>
                        ))}
                    </tbody>
                </table>
                )}
            </div>
        </div>
    );
}

export default History;