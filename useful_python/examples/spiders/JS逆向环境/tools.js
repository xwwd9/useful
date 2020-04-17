

let cropty_js = require("crypto-js");

let md5_abstract = (text) => {
    return cropty_js.MD5(text).toString();
};




export {md5_abstract};






