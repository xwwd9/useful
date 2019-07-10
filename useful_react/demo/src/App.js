import React from 'react';
import {Globalstyle} from "./style";
import Header from "./common/header";
import {Provider} from "react-redux";
import store from "./store"

import {BrowserRouter, Route} from "react-router-dom"
import Home from "./pages/home";
import Detail from "./pages/detail";

import Login from "./pages/login";

import Write from "./pages/write";


function App() {
    return (
        <Provider store={store}>
            <div className="App">
                <Globalstyle/>

                <BrowserRouter>
                    <Header/>
                    <Route path="/write" exact component={Write}></Route>
                    <Route path='/'  exact component={Home}></Route>
                    <Route path='/detail' exact component={Detail}></Route>
                    <Route path='/login' exact component={Login}></Route>
                </BrowserRouter>
                <a>pgy</a>
            </div>
        </Provider>
    );
}

export default App;
