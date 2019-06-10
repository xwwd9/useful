import {MOUSE_STATUS, SEARCH_FOCUS, SET_SEARCH_LIST} from "./actionTypes";
import {fromJS} from "immutable"

const defaultState = fromJS({
    list: [],
    focused: false,
    mouseIn:false,
});


export default (state = defaultState, action) => {
    console.log("as666666666dfdd", action.data);


    switch (action.type) {
        case SEARCH_FOCUS: {
            const newState = state.set("focused", action.value);
            return newState
        }

        case SET_SEARCH_LIST: {
            console.log("as666666666dfdd", action.data, typeof state.data);
            const newState = state.set("list", action.data);
            console.log(typeof newState.data)
            return newState
        }

        case MOUSE_STATUS: {
            const newState = state.set("mouseIn", action.value);
            return newState
        }


        default:
            return state
    }

}



