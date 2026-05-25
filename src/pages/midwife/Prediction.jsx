import API from "../../services/api";
import { useNavigate } from "react-router-dom";
import { useState } from "react";


function Prediction() {
    
    const navigate = useNavigate();
    
    const [formData, setFormData] = useState({
        name: "",
        age_months: "",
        gender: "",

        family_history: "no",
        inattention: "no",
        easily_distracted: "no",
        poor_response: "no",
        social_interaction_difficulty: "no",
        communication_issues: "no",
        poor_task_engagement: "no",
        excessive_talking: "no",
        hyperactivity: "no",
        risk_taking_behavior: "no",
        forgetfulness: "no",
        impulsivity: "no",
        aggressive: "no",
        lack_of_empathy: "no",
        pretend_play: "no",
        eye_contact_or_joint_attention: "no",
        deficits_pointing: "no",
        restrictive_repetitive_movements: "no",
        response_to_name: "no",
    });

    const handleChange = (e) => {

        const { name, value } = e.target;

        setFormData({
            ...formData,
            [name]:
                name === "age_months"
                ? Number(value)
                : value
        });
    };

    const handleSubmit = async (e) => {

        e.preventDefault();

        try {
            const response = await API.post(
                "/predict",
                formData
            );

            console.log(response.data);  //navigate to result page with prediction result

            navigate("/results", {
                state: response.data
            });
        }
        catch (error) {
            console.error(error);

            alert("Prediction failed. Please try again.");
        }
    };

    const symptoms = [
       "family_history",
        "inattention",
        "easily_distracted",
        "poor_response",
        "social_interaction_difficulty",
        "communication_issues",
        "poor_task_engagement",
        "excessive_talking",
        "hyperactivity",
        "risk_taking_behavior",
        "forgetfulness",
        "impulsivity",
        "aggressive",
        "lack_of_empathy",
        "pretend_play",
        "eye_contact_or_joint_attention",
        "deficits_pointing",
        "restrictive_repetitive_movements",
        "response_to_name"
    ];

    return (
        <div className="prediction-container">
            <div className="prediction-card">

                <h1>NDD Prediction Symptom Analysis</h1>

                <form onSubmit={handleSubmit}>

                    {/* Child Name */}
                    <div className="form-group">
                        <label>Name of the Child</label>

                        <input
                            type="text"
                            name="name"
                            placeholder="Enter child name"
                            onChange={handleChange}
                            required
                        />
                    </div>

                    {/* Age in Months */}
                    <div className="form-group">
                        <label>Age (in Months)</label>

                        <input
                            type="number"
                            name="age_months"
                            placeholder="Enter age in months"
                            onChange={handleChange}
                            required
                        />
                    </div>

                    {/* Gender */}
                    <div className="form-group">
                        <label>Gender</label>

                        <select
                            name="gender"
                            value={formData.gender}
                            onChange={handleChange}
                            required
                        >
                            <option value="">Select gender</option>
                            <option value="male">Male</option>
                            <option value="female">Female</option>

                        </select>
                    </div>

                    {/* Symptoms */}

                    <h2>Symptom Assessements</h2>

                    {symptoms.map((symptom) => (

                        <div className="form-group" key={symptom}>

                            <label>
                                {symptom
                                .replaceAll("_", " ")
                                .charAt(0)
                                .toUpperCase() +
                                symptom.replaceAll("_", " ").slice(1)
                                }
                            </label>

                            <select
                                name={symptom}
                                value={formData[symptom]}
                                onChange={handleChange}
                                required
                            >
                                 
                                <option value="no">No</option>
                                <option value="yes">Yes</option>
                            </select>
                        </div>
                    ))}

                    <button type="submit">Predict Result</button>
                </form>
            </div>
        </div>
    );
}

export default Prediction;