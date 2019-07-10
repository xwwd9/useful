import React, {PureComponent} from "react"
import {connect} from "react-redux";
import {LoginBox, LoginButton, LoginInput, LoginWrapper} from "./style";
import {mylogin} from "./store/actionCreators";
import {Redirect} from "react-router-dom";

class Login extends PureComponent {


    render() {
        console.log(this.props.login)
        if (!this.props.login) {

            return <LoginWrapper>
                <LoginBox>
                    <LoginInput placeholder="user"
                                ref={(input) => {
                                    this.account = input
                                }}></LoginInput>
                    <LoginInput placeholder="password"
                                type="password"
                                ref={(input) => {
                                    this.password = input
                                }}></LoginInput>
                    <LoginButton onClick={() => this.props.mylogin(this.account, this.password)}>登录</LoginButton>
                </LoginBox>
            </LoginWrapper>
        }
        else{
            return <Redirect to="/"></Redirect>
        }

    }

    componentWillMount() {
    }
}


const mapState = (state) => {
    return {
        login: state.getIn(["login", "login"])
    }
};


const mapDispatch = (dispatch) => ({

    mylogin(account, password) {
        dispatch(mylogin(account.value, password.value))
        console.log(account.value, password.value)
    }

})


export default connect(mapState, mapDispatch)(Login)





