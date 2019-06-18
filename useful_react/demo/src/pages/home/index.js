import React, {Component}from "react"
import {HomeLeft, HomeRight, HomeWraper} from "./style";
import Topic from "./components/Topic";
import List from "./components/List";
import Recomm from "./components/Recomm";
import Writer from "./components/Writer";



class Home extends Component{
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
        </HomeWraper>
    }
}


export default Home