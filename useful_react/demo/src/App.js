import React from 'react';
import {Globalstyle} from "./style";
import Header from "./common/header";
import {Provider} from "react-redux";
import store from "./store"


function App() {
    return (
        <Provider store={store}>
            <div className="App">
                <Globalstyle/>
                <Header/>

                <a>pgy</a>
            </div>
        </Provider>
    );
}

export default App;
