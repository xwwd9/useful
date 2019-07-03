import React, {Component}from "react"
import {Content, DetailHeader, DetailWrapper} from "./style";



class Detail extends Component{
    render(){
        return <DetailWrapper>
            <DetailHeader>老板丢给我60万行的Excel数据，幸亏我会Python，不然就惨了</DetailHeader>
            <Content>
                <img src="//upload-images.jianshu.io/upload_images/16980865-09b408a36a19a0cb.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/592/format/webp" />
            </Content>
        </DetailWrapper>
    }
}


export default Detail