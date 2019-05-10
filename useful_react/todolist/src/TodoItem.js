import React, { Component } from "react";
import PropTypes from 'prop-types';

class TodoItem extends Component {

    constructor(props) {
        super(props);

    }


    shouldComponentUpdate(nextProps, nextState){
        if(nextProps.content !== this.props.content){
            return true
        }
        else{
            return false
        }
    }

    render() {
        console.log("child render")
        const { content, } = this.props
        return <div >{content}</div>
    }
}

// 做类型校验
// index : PropTypes.number.isRequired  要求index是必须传的，数字类型
// 
TodoItem.propTypes = {
    content: PropTypes.string
}
// 设置默认值，如果父主键没有穿的话用这个值
TodoItem.defaultProps = {
    test: ""
}

export default TodoItem;