import React from 'react';
import {Globalstyle} from "./style";
import Header from "./common/header";
import {Provider} from "react-redux";
import store from "./store"

import {BrowserRouter, Route} from "react-router-dom"
import Home from "./pages/home";
import Detail from "./pages/detail";



function App() {
    return (
        <Provider store={store}>
            <div className="App">
                <Globalstyle/>
                <Header/>
                <BrowserRouter>
                    <Route path='/'  exact component={Home}></Route>
                    <Route path='/detail' exact component={Detail}></Route>
                </BrowserRouter>
                <a>pgy</a>
            </div>
        </Provider>
    );
}

export default App;
