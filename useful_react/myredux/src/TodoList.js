import React, { Component, Fragment } from 'react';
import { Input, Button, List } from 'antd';

import store from "./store"

class TodoList extends Component {
    constructor(props) {
        super(props)
        this.state = store.getState()
        console.log(store.getState())
        store.subscribe(this.handleStoreChange)
    }

    handleStoreChange = (e) => {
        this.setState(store.getState())
    }

    handleInputChange = (e) => {
        console.log(e, "askdjfaskljdf")
        const action = {
            type: 'change_input_value',
            value: e.target.value
        }
        store.dispatch(action)
    }

    handleDel = (index, a) => {
        console.log(index, a, "index")
    }

    handleClick = () => {
        const action = {
            type: 'add_list',
        }
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
                        onClick={(index) => this.handleDel(index, index)}
                    >
                        <a
                            onClick={() => this.handleDel("asdf")}
                        >askdjf</a>
                        {item}
                    </List.Item>
                )}
            />
        </Fragment>
    }
}


export default TodoList