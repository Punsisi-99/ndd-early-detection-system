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

                            <th>ID</th>
                            <th>Name</th>
                            <th>Age</th>
                            <th>Gender</th>
                            <th>Family History</th>
                            <th>Inattention</th>
                            <th>Easily Distracted</th>
                            <th>Poor Response</th>
                            <th>Social Difficulty</th>
                            <th>Communication Issues</th>
                            <th>Poor Task Engagement</th>
                            <th>Excessive Talking</th>
                            <th>Hyperactivity</th>
                            <th>Risk Taking</th>
                            <th>Forgetfulness</th>
                            <th>Impulsivity</th>
                            <th>Aggressive</th>
                            <th>Lack of Empathy</th>
                            <th>Pretend Play</th>
                            <th>Eye Contact</th>
                            <th>Deficits Pointing</th>
                            <th>Repetitive Movements</th>
                            <th>Response to Name</th>
                            <th>Diagnosis</th>
                            <th>Prediction Code</th>
                            <th>Main Reasons</th>
                            <th>Date</th>
                        </tr>
                    </thead>

                    <tbody>

                        {filteredRecords.map((item) => (

                            <tr key={item.id}>

                                <td>{item.id}</td>
                                <td>{item.name}</td>
                                <td>{item.age}</td>
                                <td>{item.gender}</td>
                                <td>{item.family_history}</td>
                                <td>{item.inattention}</td>
                                <td>{item.easily_distracted}</td>
                                <td>{item.poor_response}</td>
                                <td>{item.social_interaction_difficulty}</td>
                                <td>{item.communication_issues}</td>
                                <td>{item.poor_task_engagement}</td>
                                <td>{item.excessive_talking}</td>
                                <td>{item.hyperactivity}</td>
                                <td>{item.risk_taking_behavior}</td>
                                <td>{item.forgetfulness}</td>
                                <td>{item.impulsivity}</td>
                                <td>{item.aggressive}</td>
                                <td>{item.lack_of_empathy}</td>
                                <td>{item.pretend_play}</td>
                                <td>{item.eye_contact_or_joint_attention}</td>
                                <td>{item.deficits_pointing}</td>
                                <td>{item.restrictive_repetitive_movements}</td>
                                <td>{item.response_to_name}</td>

                                <td
                                    className={item.diagnosis === "Healthy"
                                        ? "healthy"
                                        : "risk"
                                    }
                                >
                                    {item.diagnosis}
                                </td>

                                <td>{item.prediction_code}</td>

                                <td>
                                    {item.main_reasons || "N/A"}
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