import React, {useContext, useState} from "react";
import {UserContext} from "../context/UserContext";
import ErrorMessage from "./ErrorMessage";

const Register = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [confirmPassword, setConfirmPassword] = useState("");
    const [errorMessage, setErrorMessage] = useState("")
    const [, setToken] = useContext(UserContext)
    const submitRegistration = async () => {
        const requestOptions =
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({username: username, password: password})
            };
        const response = await fetch('/users/create', requestOptions)
        const data = await response.json();
        if (!response.ok) {
            setErrorMessage(data.detail)
        } else {
            setToken(data.access_token);
        }
    };

    const handleSubmit = (e) => {
            e.preventDefault();
            if (password === confirmPassword && password.length > 5) {
                submitRegistration();
            } else {
                setErrorMessage("Ensure that the passwords match and greater than 5 characters");
            }
        }
    ;
    return (
        <div className="column">
            <form className="box" onSubmit={handleSubmit}>
                <h1 className="title has-text-centered">Register</h1>
                <div className="field">
                    <label className="label">Username</label>
                    <div className="control">
                        <input type="text"
                               placeholder="Enter Your username"
                               value={username}
                               onChange={(e) => setUsername(e.target.value)}
                               className="input"
                               required
                        />
                    </div>
                </div>
                <div className="field">
                    <label className="label">Password</label>
                    <div className="control">
                        <input type="password"
                               placeholder="Enter Your Password"
                               value={password}
                               onChange={(e) => setPassword(e.target.value)}
                               className="input"
                               required
                        />

                    </div>
                </div>
                <div className="field">
                    <label className="label">Confirm Password</label>
                    <div className="control">
                        <input type="password"
                               placeholder="Enter Your Repeat Password"
                               value={confirmPassword}
                               onChange={(e) => setConfirmPassword(e.target.value)}
                               className="input"
                               required
                        />

                    </div>
                </div>
                <ErrorMessage message={errorMessage}/>
                <br/>
                <button className="button is-primary" type="submit">Register</button>
            </form>
        </div>
    )
};

export default Register;