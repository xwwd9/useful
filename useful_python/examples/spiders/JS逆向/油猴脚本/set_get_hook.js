// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        https://www.zhihu.com/*
// @run-at       document-start
// @grant        none
// 加密参数有个window._pt_, 当设置window._pt_的时候hook
// ==/UserScript==

(function() {
    'use strict';
    // let pre = window._pt_;
    Object.defineProperty(__g,"_encrypt", {
       get:function () {
           // return pre
           return 10
       },
        set:function (pt) {
           console.log("pt", pt);
           debugger
            return 10
            // pre = pt;
            // return pre
        }
    });
    // Your code here...
})();
