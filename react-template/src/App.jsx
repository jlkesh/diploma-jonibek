import React, {useState, useEffect} from 'react';
import Register from "./components/Register";

const App = () => {
    const [message, setMessage] = useState("");

    const getWelcomeMessage = async () => {
        const requestsOptions = {
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            },
        };
        const response = await fetch("/articles/", requestsOptions)
        const data = await response.json()
        console.log(data)
        if (!response.ok) {
            console.log("something messed up")
        } else {
            setMessage(data.message);
        }
    };
    useEffect(() => {
        getWelcomeMessage();
    }, [])


    return (
        <h2>
            {message}
            <Register/>
        </h2>
        // <div className="App">
        //     <div className="App-header">
        //         <h2>Welcome to React</h2>
        //     </div>
        //     <p className="App-intro">
        //         To get started, edit <code>src/App.js</code> and save to reload.
        //     </p>
        // </div>
    );

}

export default App;
