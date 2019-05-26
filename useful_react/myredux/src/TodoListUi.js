import React, { Component, Fragment } from "react"
import { Input, Button, List } from 'antd';


const TodoListUi = (props) => {
    return <Fragment>
        <div>
            <Input
                style={{ width: 300 }}
                placeholder="Basic usage"
                value={props.inputValue}
                onChange={props.handleInputChange}
            />
            <Button
                style={{ marginLeft: 10 }}
                type="primary"
                onClick={props.handleClick}
            >
                点击
                </Button>
        </div>

        <List
            style={{ marginTop: 20, width: 500 }}
            bordered
            dataSource={props.list}
            renderItem={(item, index) => (
                <List.Item
                    // onClick={(index) => this.handleDel(index)}
                    // onClick={this.handleDel.bind(this, index)}
                    onClick={() => props.handleDel(index)}
                >
                    {item}
                </List.Item>
            )}
        />
    </Fragment>
}


// class TodoListUi extends Component {
//     render() {
//         return <Fragment>
//             <div>
//                 <Input
//                     style={{ width: 300 }}
//                     placeholder="Basic usage"
//                     value={this.props.inputValue}
//                     onChange={this.props.handleInputChange}
//                 />
//                 <Button
//                     style={{ marginLeft: 10 }}
//                     type="primary"
//                     onClick={this.props.handleClick}
//                 >
//                     点击
//                 </Button>
//             </div>

//             <List
//                 style={{ marginTop: 20, width: 500 }}
//                 bordered
//                 dataSource={this.props.list}
//                 renderItem={(item, index) => (
//                     <List.Item
//                         // onClick={(index) => this.handleDel(index)}
//                         // onClick={this.handleDel.bind(this, index)}
//                         onClick={() => this.props.handleDel(index)}
//                     >
//                         {item}
//                     </List.Item>
//                 )}
//             />
//         </Fragment>
//     }
// }

export default TodoListUi;