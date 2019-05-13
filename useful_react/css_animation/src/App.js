import React, { Component, Fragment } from 'react';
import "./style.css"

class App extends Component {
    constructor(props) {
        super(props)
        this.state = {
            isShow: false
        }
    }

    changeShow = () => {

        console.log(this.state.isShow)
        this.setState((preState) => {
            return { isShow: !preState.isShow }
        })
    }

    render() {
        const { isShow } = this.state
        return (
            <Fragment>
                <div className={isShow ? "show" : "hide"}>hello</div>
                <button onClick={this.changeShow}>点击</button>
            </Fragment>
        )
    }


}




export default App;
