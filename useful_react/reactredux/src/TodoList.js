import React, {Component, Fragment} from 'react'

import {connect} from "react-redux"
import {Input, Button, List} from "antd";
import {
    addTodoItem,
    delTodItem,
    getInputChangeAction
} from "./store/actionCreator";

import store from "./store";

class TodoList extends Component {


    render() {
        return <Fragment>
            <div>
                <Input
                    style={{width: 300}}
                    placeholder="Basic usage"
                    value={this.props.inputValue}
                    onChange={this.props.handleInputChange}
                />
                <Button
                    style={{marginLeft: 10}}
                    type="primary"
                    onClick={this.props.handleClick}
                >
                    点击
                </Button>
            </div>

            <List
                style={{marginTop: 20, width: 500}}
                bordered
                dataSource={this.props.list}
                renderItem={(item, index) => (
                    <List.Item
                        // onClick={(index) => this.handleDel(index)}
                        // onClick={this.handleDel.bind(this, index)}
                        onClick={() => this.props.handleDel(index)}
                    >
                        {item}
                    </List.Item>
                )}
            />
        </Fragment>
    }

}


const mapStateToProps = (state) => {
    // 接收一个state 返回一个对象
    return {
        inputValue: state.inputValue,
        list: state.list,
    }
};


const mapDispatchToProps = (dispatch) => {
    return {
        handleInputChange(e) {
            console.log(e, "askdjfaskljdf");
            const action = getInputChangeAction(e.target.value);
            dispatch(action)
        },
        handleClick() {
            const action = addTodoItem();
            dispatch(action)
        },
        handleDel(index) {
            // console.log(index, a, typeof a, "index");
            const action = delTodItem(index);
            store.dispatch(action)
        }
    }
};


// export default TodoList;
export default connect(mapStateToProps, mapDispatchToProps)(TodoList);
