

let cropty_js = require("crypto-js");

let md5_abstract = (text) => {
    return cropty_js.MD5(text).toString();
};


function btoa(str) {
  if (Buffer.byteLength(str) !== str.length)
    throw new Error('bad string!');
  return Buffer(str, 'binary').toString('base64');
}

function atob(str){
    return Buffer.from(str, `base64`).toString(`binary`)
}




export {md5_abstract};






