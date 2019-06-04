import {SEARCH_FOCUS} from "./actionTypes";


const defaultState = {
    focused: false
};


export default (state=defaultState, action) => {
    if(action.type === SEARCH_FOCUS){
        const newState = {focused:action.value}
        return newState
    }
    return state
}



