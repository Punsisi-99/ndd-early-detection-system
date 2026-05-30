import { useLocation, useNavigate } from "react-router-dom";

function Results() {

    const location = useLocation();

    const navigate = useNavigate();

    const data = location.state;

    const isHealthy =
    data.diagnosis?.toLowerCase() === "healthy";

    if(!data) {
        return <h2>No results Found</h2>;
    }

    return (

        <div className="results-container">

            <div className="results-card">

                <div className="results-icon">
                    {isHealthy ? "✅" : "⚠️"}
                </div>

                <h1>Prediction Results</h1>

                <h2 className={
                        isHealthy
                            ? "healthy-text"
                                : "risk-text"
                    }
                >
                    Diagnosis: {data.diagnosis}
                </h2>

                {isHealthy ? (

                    <p className="safe-message">

                        The child is safe.
                        No significant NDD symptoms detected.

                    </p>

                ) : (
                        <>

                            <h3>Main Symptoms Identified</h3>

                        <ul>

                            {data.main_reasons
                            ?.slice(0, 3)
                            .map((item, index) => (

                                <li key={index}>

                                    • {" "}
                                    {item.symptom
                                    ?.replaceAll("_", " ")
                                    .charAt(0)
                                    .toUpperCase() +
                                    item.symptom
                                        ?.replaceAll("_", " ")
                                        .slice(1)}

                                </li>

                            ))}

                        </ul>

                    </>

                )}

                <button
                className="back-btn"
                onClick={() => navigate("/predict")}
                >
                Back to Prediction
                </button>

            </div>

        </div>
    );
}

export default Results;