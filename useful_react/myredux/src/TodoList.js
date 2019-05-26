import React, { Component } from 'react';

import store from "./store"
import { getInputChangeAction, addTodoItem, delTodItem, addListItem } from './store/actionCreator';
import axios from 'axios'
import TodoListUi from './TodoListUi';

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

    componentDidMount(){
        axios.get("http://localhost:3000/json.json").then((ret) => {
            const data = ret.data
            const action = addListItem(data)
            store.dispatch(action)
        })
    }

    render() {
        const { list } = this.state;
        return <TodoListUi
            inputValue={this.state.inputValue}
            handleInputChange={this.handleInputChange}
            handleDel={this.handleDel}
            handleClick={this.handleClick}
            list={list}
        >
        </TodoListUi>
    }
}


export default TodoList