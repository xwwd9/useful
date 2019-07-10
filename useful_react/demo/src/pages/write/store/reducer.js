import {fromJS} from "immutable"
import {
    change_home_data,
    change_to_top,
    get_list_more,
    getdetailcontent, loginsuccess
} from "./actionTypes";

const defaultState = fromJS({
    login:false,
    })
;


export default (state = defaultState, action) => {


    switch (action.type) {

        case loginsuccess:
            return state.set("login", action.value);

        default:
            return state
    }

}



