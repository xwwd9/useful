

a = {}


Object.defineProperty(a,"ok", {
   get:function () {
       console.log("ok")
       return "ok"
   },
    set:function (d) {
       console.log(d)
    }
});

a.ok = 10;
// console.log(a.ok);
