import React, { Component, Fragment } from 'react';
import "./style.css"
import TodoItem from './TodoItem';
class TodoList extends Component {


    constructor(props) {
        super(props)
        this.state = {
            inputValue: 'ddd',
            list: [],
        }
    }


    // handleInputChange(e){
    //     console.log(e.target.value)
    // }

    handleInputChange = (e) => {
        this.setState({
            inputValue: e.target.value,
        })
    };

    handleBtnClick = (index) => {
        this.setState({
            // 数组展开运算符
            list: [...this.state.list, this.state.inputValue],
            inputValue: ''
        })
    };

    handleDelete = (index) => {

        // state需要拷贝出来再修改
        const list = [...this.state.list]
        list.splice(index, 1)

        this.setState({
            list
        })

    }


    render() {
        return (
            <Fragment>
                <div>
                    <lable htmlFor="insertArea">输入内容</lable>
                    <input
                        id="insertArea"
                        className="input"
                        value={this.state.inputValue}
                        onChange={this.handleInputChange}
                    />
                    <button onClick={this.handleBtnClick}>提交</button>
                </div>


                <ul>
                    {
                        // 数组循环
                        this.state.list.map((item, index) => {
                            console.log(this.state.list)
                            // return (
                            //     <li
                            //         key={index}
                            //         dangerouslySetInnerHTML={{__html:item }}
                            //         onClick={() => this.handleDelete(index)}
                            //     >
                            //         {/* {item} */}
                            //     </li>
                            // )
                            return <TodoItem content={item} key={index}></TodoItem>
                        })
                    }
                </ul>

            </Fragment>
        );
    }
}

export default TodoList;
