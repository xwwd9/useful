import {MOUSE_STATUS, SEARCH_FOCUS, SET_SEARCH_LIST} from "./actionTypes";
import axios from "axios"
import {fromJS} from "immutable"


export const search_focus = (value) => {

    return {
        type: SEARCH_FOCUS,
        value
    }
};




export const getList = (isRandom=false) => {
    return (dispatch) => {
        axios.get("/api/headerList.json").then((ret) => {
            const data = ret.data.data;
            const action = setList(data, isRandom);
            dispatch(action)
        }).catch(() => {

        })
    }
};


export const mouseEnter = (value) => {
    return {
        type:MOUSE_STATUS,
        value
    }
}




export const setList = (data, isRandom) => {


    const total = data.length/10;

    if(isRandom){
        const start = Math.floor(Math.random()*total);
        data = data.splice(start, 10);
    }
    else{
        data = data.splice(0, 10);
    }

    return {
        type: SET_SEARCH_LIST,
        data:fromJS(data)
    }
}