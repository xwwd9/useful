import React, {Component} from "react"
import {ListInfo, ListItem, LoadMore} from "./style";

import {Link} from "react-router-dom";

import {connect} from "react-redux"
import {getMoreList} from "../store/actionCreators";

class List extends Component {

    render() {
        const {artists} = this.props;
        // console.log(artists[0].url);
        return (
            <div>
                {
                    artists.map((value, index) => {
                        return (
                            <Link to="/detail"
                                  key={value.get("id")}>
                                <ListItem>
                                    <img alt=""
                                         className="list-pic"
                                         src={value.get("url")}/>
                                    <ListInfo>
                                        <h3 className="title">{value.get("title")}</h3>
                                        <p className="desc">{value.get("desc")}</p>
                                    </ListInfo>
                                </ListItem>
                            </Link>
                        )


                    })
                }
                <LoadMore onClick={this.props.getMoreList}>更多文字</LoadMore>
            </div>
        )
    }
}

const mapStateToProps = (state) => ({
    artists: state.get("home").get("artists")
});

const mapDispatch = (dispatch) => ({
    getMoreList() {
        const action = getMoreList()
        dispatch(action)
    }
})

export default connect(mapStateToProps, mapDispatch)(List)