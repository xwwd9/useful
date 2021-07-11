import axios from "axios"
import {loginsuccess} from "./actionTypes";

import {getdetailcontent} from "../../detail/store/actionTypes";


//
// export const mylogin = () => {
// // console.log("detail");
//     return (dispatch) => {
//         console.log("detail");
//         axios.get("/apis/detail_content.json").then((ret) => {
//             const data = ret.data.data;
//             const action = {
//                 type:getdetailcontent,
//                 title:data.title,
//                 content:data.content
//             }
//             dispatch(action)
//         })
//     }
//
// }


export const setLogin = (status) => {
    const action = {
        type: loginsuccess,
        value: status
    }
    return action
}

export const mylogin = (account, password) => {
    console.log("@@@@@@@@@@@");
    return (dispatch) => {
        console.log("login");
        axios.get("/apis/login.json?account=" + account + '&password=' + password).then((ret) => {
            console.log(ret);
            const result = ret.data.result;
            console.log("askdljfd");
            if (result) {
                alert("登录成功")
                const action = setLogin(true)
                dispatch(action)
            } else {
                alert("登录失败")
                const action = setLogin(false)
                dispatch(action)
            }

        })
    }
}













