import React, {PureComponent} from "react"
import {connect} from "react-redux";
import {Redirect} from "react-router-dom";

class Write extends PureComponent {


    render() {
        console.log(this.props.login)
        if (this.props.login) {

           return <div>写文章</div>
        }
        else{
            return <Redirect to="/login"></Redirect>
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



})


export default connect(mapState, mapDispatch)(Write)





