import {SEARCH_FOCUS} from "./actionTypes";
import {fromJS} from "immutable"

const defaultState = fromJS({
    focused: false
});


export default (state=defaultState, action) => {
    if(action.type === SEARCH_FOCUS){
        const newState = state.set("focused", action.value)
        return newState


    }
    return state
}



