

import axios from "axios"
import {getdetailcontent} from "./actionTypes";


export const getDetailContent = () => {

    return (dispatch) => {
        console.log("detail");
        axios.get("/apis/detail_content.json").then((ret) => {
            const data = ret.data.data;
            const action = {
                type:getdetailcontent,
                title:data.title,
                content:data.content
            }
            dispatch(action)
        })
    }

}