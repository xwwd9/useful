import React, { Component, Fragment } from 'react';
import "./style.css"
import { CSSTransition } from 'react-transition-group';
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
                {/* <div className={isShow ? "show" : "hide"}>hello</div> */}
                <CSSTransition
                    in={this.state.isShow}
                    timeout={3000}
                    classNames="fade"
                    // mountOnEnter
                    // unmountOnExit
                    // appear
                    onEnter={(el) => {
                        el.style.color = 'red'
                        console.log("1111")
                    }}
                    onExited={(el) => {
                        console.log("exited")
                    }}
                    onExit={(el) => {
                        console.log("alskdjfaksldjf")
                    }}
                >
                    <div>???</div>
                </CSSTransition>
                <button onClick={this.changeShow}>{isShow ? "show" : "hide"}</button>


            </Fragment>
        )
    }


}

// import { useState } from 'react';
// function App() {
//     const [inProp, setInProp] = useState(false);
//     return (
//       <div>

//         <CSSTransition in={inProp} timeout={200} classNames="my-node"
//         >
//           <div>
//             {"I'll receive my-node-* classes"}
//           </div>
//         </CSSTransition>
//         <button type="button" onClick={() => setInProp(true)}>
//           Click to Enter
//         </button>
//       </div>
//     );
//   }

export default App;
