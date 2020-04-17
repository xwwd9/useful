// ==UserScript==
// @name         New Userscript
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  try to take over the world!
// @author       You
// @match        http://flight.qunar.com/*
// @run-at       document-start
// @grant        none
// url = http://flight.qunar.com/site/oneway_list.htm?searchDepartureAirport=%E9%87%8D%E5%BA%86&searchArrivalAirport=%E6%98%86%E6%98%8E&searchDepartureTime=2020-04-28&searchArrivalTime=2020-04-27&nextNDays=0&startSearch=true&fromCode=CKG&toCode=KMG&from=tejia_d_search&lowestPrice=null
// 加密参数有个window._pt_, 当设置window._pt_的时候hook
// ==/UserScript==

(function() {
    'use strict';
    let pre = window._pt_;
    Object.defineProperty(window,"_pt_", {
       get:function () {
           return pre
       },
        set:function (pt) {
           console.log("pt", pt);
           debugger
            pre = pt;
            return pre
        }
    });
    // Your code here...
})();
