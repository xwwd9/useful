import React, {Component}from "react"
import {Content, DetailHeader, DetailWrapper} from "./style";

import {connect} from "react-redux";
import {getDetailContent} from "./store/actionCreators";

class Detail extends Component{



    render(){
        console.log(this.props.content);
        return <DetailWrapper>
            <DetailHeader>
                {
                    this.props.title
                }
            </DetailHeader>
            <Content dangerouslySetInnerHTML={{__html:this.props.content }}  >
            </Content>
        </DetailWrapper>
    }

    componentWillMount() {
        this.props.getDetialContent()
    }
}


const mapState = (state) => {
    return {
        title:state.getIn(["detail", "title"]),
        content:state.getIn(["detail", "content"]),
    }
};


const mapDispatch = (dispatch) => ({
    getDetialContent(){
        const action = getDetailContent();
        dispatch(action)
    }
})


export default connect(mapState, mapDispatch)(Detail)