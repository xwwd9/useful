import React, {Component}from "react"
import {BackTop, HomeLeft, HomeRight, HomeWraper} from "./style";
import Topic from "./components/Topic";
import List from "./components/List";
import Recomm from "./components/Recomm";
import Writer from "./components/Writer";

import {connect} from "react-redux";
import {changeToTop, getHomeInfo} from "./store/actionCreators";

class Home extends Component{


    componentDidMount(){
        this.props.changeHomeData()
        this.bindEvents();
    }

    componentWillUnmount() {
        window.removeEventListener('scroll', this.props.changeToTop);
    }

    bindEvents = () => {
        window.addEventListener('scroll', this.props.changeToTop);
    }
    handleToTop = () => {
        window.scrollTo(0, 0)
    }

    render(){
        return <HomeWraper>
            <HomeLeft>
                <img alt="" className="banner-img" src="//upload.jianshu.io/admin_banners/web_images/4660/224da83c76e01d5deff07e163615921233af5c82.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/1250/h/540" />
                <Topic/>
                <List/>
            </HomeLeft>
            <HomeRight>
                <Recomm/>
                <Writer/>
            </HomeRight>
            {
                this.props.showToTop?<BackTop onClick={this.handleToTop}>顶部</BackTop>:null
            }
        </HomeWraper>
    }
}



const mapState = (state) => ({
    showToTop: state.getIn(["home", "showToTop"])
});

const mapDisPatch = (dispatch) => ({
    changeHomeData(){
        const action = getHomeInfo();
        dispatch(action)
    },
    changeToTop() {
        // const action = ''
        console.log(document.documentElement.scrollTop);
        if(document.documentElement.scrollTop>600){
            const action = changeToTop(true);
            dispatch(action)
        }
        else{
            const action = changeToTop(false);
            dispatch(action)
        }
        // dispatch(action)
    }
});

export default connect(mapState, mapDisPatch)(Home)