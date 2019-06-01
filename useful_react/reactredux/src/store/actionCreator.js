import { CHANGE_INPUT_VALUE, ADD_LIST, DEL_ITEM, ADD_LISTS } from "./actionTypes";
import axios from "axios"
export const getInputChangeAction = (value) => ({
    type: CHANGE_INPUT_VALUE,
    value
})
export const addTodoItem = () => ({
    type: ADD_LIST,
})
export const delTodItem = (value) => ({
    type: DEL_ITEM,
    value
})

export const addListItem = (values) => ({
    type: ADD_LISTS,
    values
})


export const getTodoList = () => {
    return (dispatch) => {
    axios.get("http://localhost:3000/json.json").then((ret) => {
        const data = ret.data
        console.log(data, "*asdf*")
        const action = addListItem(data)
        // store.dispatch(action)
        dispatch(action)
    })
}
}