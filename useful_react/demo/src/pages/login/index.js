import React, {PureComponent} from "react"
import {connect} from "react-redux";
import {LoginBox, LoginButton, LoginInput, LoginWrapper} from "./style";

class Login extends PureComponent {


    render() {
        return <LoginWrapper>
            <LoginBox>
                <LoginInput placeholder="user" ref = {(input) => {this.account = input}}></LoginInput>
                <LoginInput placeholder="password" type="password"  ref = {(input) => {this.password = input}}></LoginInput>
                <LoginButton onClick={() => this.props.login(this.account, this.password)}>登录</LoginButton>
            </LoginBox>
        </LoginWrapper>
    }

    componentWillMount() {
    }
}


const mapState = (state) => {
    return {}
};


const mapDispatch = (dispatch) => ({

    login(account, password){
        console.log(account, password)
    }

})


export default connect(mapState, mapDispatch)(Login)