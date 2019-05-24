import React, { Component, Fragment } from 'react';
import { Input, Button, List } from 'antd';
import { ADD_LIST, DEL_ITEM, CHANGE_INPUT_VALUE } from "./store/actionTypes"
import store from "./store"
import { getInputChangeAction, addTodoItem, delTodItem } from './store/actionCreator';

class TodoList extends Component {
    constructor(props) {
        super(props)
        this.state = store.getState()
        console.log(store.getState())
        store.subscribe(this.handleStoreChange)
        // this.handleDel.bind(this)
    }

    handleStoreChange = (e) => {
        this.setState(store.getState())
    }

    handleInputChange = (e) => {
        console.log(e, "askdjfaskljdf")
        const action = getInputChangeAction(e.target.value)
        store.dispatch(action)
    }

    handleDel = (index, a, b) => {
        console.log(index, a, typeof a, "index")
        const action = delTodItem(index)
        store.dispatch(action)
    }

    // handleDel(index, a, b) {
    //     console.log(index, a, b, "index")
    // }

    handleClick = () => {
        const action = addTodoItem()
        store.dispatch(action)
    }

    render() {
        const { list } = this.state;
        return <Fragment>
            <div>
                <Input
                    style={{ width: 300 }}
                    placeholder="Basic usage"
                    value={this.state.inputValue}
                    onChange={this.handleInputChange}
                />
                <Button
                    style={{ marginLeft: 10 }}
                    type="primary"
                    onClick={this.handleClick}
                >
                    点击
                </Button>
            </div>

            <List
                style={{ marginTop: 20, width: 500 }}
                bordered
                dataSource={list}
                renderItem={(item, index) => (
                    <List.Item
                        // onClick={(index) => this.handleDel(index)}
                        // onClick={this.handleDel.bind(this, index)}
                        onClick={() => this.handleDel(index)}
                    >
                        {item}
                    </List.Item>
                )}
            />
        </Fragment>
    }
}


export default TodoList