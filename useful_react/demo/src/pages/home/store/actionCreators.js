

import axiso from "axios"
import {change_home_data, change_to_top, get_list_more} from "./actionTypes";
import {fromJS, List} from "immutable";

export const getHomeInfo = () => {
    return (dispatch) => {
        // console.log("asdkjfaskdf");
        axiso.get('/apis/home_components_list_infos.json').then((ret) => {
            const result = ret.data.data;
            const action = {
                type:change_home_data,
                topics:result.topics,
                artists:result.artists
            };
            dispatch(action)
        })
    }

};

export const getMoreList = () => {
    return (dispatch) => {
        axiso.get('/apis/home_list.json').then((ret) => {
            const result = ret.data.data;
            console.log(result);
            const action = addHomeList(result)
            dispatch(action)
        })
    }
};

export const changeToTop = (value) => ({
    type:change_to_top,
    value:value
})

const addHomeList = (list) => ({
    type:get_list_more,
    list:fromJS(list)
});








