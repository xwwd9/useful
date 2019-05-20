import React, { Component, Fragment } from 'react';
import { Input, Button, List, Typography } from 'antd';

const data = [
    'Racing car sprays burning fuel into crowd.',
    'Japanese princess to wed commoner.',
    'Australian walks 100km after outback crash.',
    'Man charged over missing wedding girl.',
    'Los Angeles battles huge wildfires.',
];

class TodoList extends Component {
    constructor(props) {
        super(props)
    }


    render() {
        return <Fragment>
            <div>
                <Input
                    style={{ width: 300 }}
                    placeholder="Basic usage"
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
                dataSource={data}
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