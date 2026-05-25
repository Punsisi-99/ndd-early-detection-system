import { useLocation } from "react-router-dom";

function Results() {

    const location = useLocation();

    const data = location.state;

    if(!data) {
        return <h2>No results Found</h2>;
    }

    return (

        <div className="results-container">

            <div className="results-card">

                <h1>Prediction Results</h1>

                <h2>
                    Diagnosis: {data.diagnosis}
                </h2>

                {
                    data.diagnosis === "Healthy" ? (
                        <p className="healthy-message">
                            The child is safe, no symptoms in NDD
                        </p>

                    ) : (
                        <>
                            <h3>Main Symptoms Identified</h3>

                            {
                                data.main_reasons && data.main_reasons.length > 0 ? (

                                    <ul>
                                        {data.main_reasons.slice(0,3).map((item, index) => (

                                            <li key={index}>

                                                {item.symptom
                                                .replaceAll("_", " ")
                                                .charAt(0)
                                                .toUpperCase() +
                                                item.symptom
                                                .replaceAll("_", " ")
                                                .slice(1)
                                                }

                                            </li>

                                        ))}

                                    </ul>

                                ) : null
                            }
                        </>
                    )
                }
            </div>
        </div>
    );
}

export default Results;