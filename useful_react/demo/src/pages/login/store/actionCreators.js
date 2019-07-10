

import axiso from "axios"
import {loginsuccess} from "./actionTypes";




export const login = (account, password) => {
    console.log("@@@@@@@@@@@");
    return (dispatch) => {
        console.log("askdljfd");
        axiso.get("/apis/login.json?account="+account+'&password='+password).then((ret) => {
            console.log(ret);
            const result = ret.data.result;
            console.log("askdljfd");
            if(result){
                alert("登录成功")
                const action = {
                    type:loginsuccess,
                    value:true
                }
                dispatch(action)
            }
            else{
                alert("登录失败")
                const action = {
                    type:loginsuccess,
                    value:false
                }
                dispatch(action)
            }

        })
    }
}













