import React, {Component}from "react"
import {HomeLeft, HomeRight, HomeWraper} from "./style";



class Home extends Component{
    render(){
        return <HomeWraper>
            <HomeLeft>
                <img className="banner-img" src="//upload.jianshu.io/admin_banners/web_images/4660/224da83c76e01d5deff07e163615921233af5c82.jpg?imageMogr2/auto-orient/strip|imageView2/1/w/1250/h/540" />
                dd
            </HomeLeft>
            <HomeRight>right</HomeRight>
            home
        </HomeWraper>
    }
}


export default Home