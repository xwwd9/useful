import React, {Component} from "react"
import {TopicItem, TopicWraper} from "./style";

import {connect} from "react-redux";


class Topic extends Component {
    render() {
        return <TopicWraper>
            {
                this.props.topics.map((value, index) => {
                    return <TopicItem index={index}>
                        <img className="topic-pic" src={value.get("url")} />
                        {value.get("title")}
                    </TopicItem>
                })
            }
        </TopicWraper>
    }
}


const mapStateToProps = (state) =>({
    topics:state.get("home").get("topics")
});

export default connect(mapStateToProps, null)(Topic)