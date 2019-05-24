import { CHANGE_INPUT_VALUE, ADD_LIST, DEL_ITEM } from "./actionTypes";

export const getInputChangeAction = (value) => ({
    type: CHANGE_INPUT_VALUE,
    value
})
export const addTodoItem = (value) => ({
    type: ADD_LIST,
})
export const delTodItem= (value) => ({
    type:DEL_ITEM,
    value
})