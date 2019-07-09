import React, {PureComponent} from "react"
import {connect} from "react-redux";
import {LoginBox, LoginButton, LoginInput, LoginWrapper} from "./style";

class Login extends PureComponent {


    render() {
        return <LoginWrapper>
            <LoginBox>
                login
                <LoginInput placeholder="user"></LoginInput>
                <LoginInput placeholder="password"></LoginInput>
                <LoginButton>登录</LoginButton>
            </LoginBox>
        </LoginWrapper>
    }

    componentWillMount() {
    }
}


const mapState = (state) => {
    return {}
};


const mapDispatch = (dispatch) => ({})


export default connect(mapState, mapDispatch)(Login)