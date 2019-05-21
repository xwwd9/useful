import React, { Component, Fragment } from 'react';
import { Input, Button, List, Typography } from 'antd';

import store from "./store"

class TodoList extends Component {
    constructor(props) {
        super(props)
        this.state = store.getState()
        console.log(store.getState())
    }


    render() {
        const { list } = this.state;
        return <Fragment>
            <div>
                <Input
                    style={{ width: 300 }}
                    placeholder="Basic usage"
                    value={this.state.inputValue}
                />
                <Button
                    style={{ marginLeft: 10 }}
                    type="primary"
                >
                    Primary
                </Button>
            </div>

            <List
                style={{ marginTop: 20 ,width:500}}
                bordered
                dataSource={list}
                renderItem={item => (
                    <List.Item>
                        {item}
                    </List.Item>
                )}
            />
        </Fragment>
    }
}


export default TodoList