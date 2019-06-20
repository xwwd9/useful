import {fromJS} from "immutable"
import {change_home_data, change_to_top, get_list_more} from "./actionTypes";

const defaultState = fromJS({
        topics: [],
        artists: [],
        showToTop:false
    })
;


export default (state = defaultState, action) => {


    switch (action.type) {

        case change_home_data:
            return state.merge({
                    topics:fromJS(action.topics),
                artists:fromJS(action.artists)
            });
            console.log(action);

        case get_list_more:
            return state.set('artists', state.get('artists').concat(action.list));
            console.log(action);

        case change_to_top:
            return state.set('showToTop', action.value);
            console.log(action);

        default:
            return state
    }

}



