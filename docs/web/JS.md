[返回主目录](../../README.md)

- [1. js对象拷贝](#1-js对象拷贝)
- [2. 数组遍历：](#2-数组遍历)
- [3. Array:](#3-array)
- [4. 正则的使用](#4-正则的使用)
- [5. Js中读取Json文件](#5-js中读取json文件)
- [6. 对象转换为Json字符串，和Json字符串转换成js对象](#6-对象转换为json字符串和json字符串转换成js对象)
- [7. 数组去重](#7-数组去重)
- [8. 读取本地文件](#8-读取本地文件)
- [9. 方括号 和花括号[], {}](#9-方括号-和花括号-)
- [10. async 和 await](#10-async-和-await)
  - [10.1. async 是一个修饰符，async 定义的函数会默认的返回一个Promise对象resolve的值，因此对async函数可以直接进行then操作,返回的值即为then方法的传入函数](#101-async-是一个修饰符async-定义的函数会默认的返回一个promise对象resolve的值因此对async函数可以直接进行then操作返回的值即为then方法的传入函数)
  - [10.2. await 关键字 只能放在 async 函数内部， await关键字的作用 就是获取 Promise中返回的内容， 获取的是Promise函数中resolve或者reject的值, 等待异步函数的执行结果。](#102-await-关键字-只能放在-async-函数内部-await关键字的作用-就是获取-promise中返回的内容-获取的是promise函数中resolve或者reject的值-等待异步函数的执行结果)
- [11. yield 一个Generator函数与普通function的区别就是函数名前面多了一个星号 * 但是执行时有很大不同，与yield命令配合，可以实现暂停执行的功能](#11-yield-一个generator函数与普通function的区别就是函数名前面多了一个星号--但是执行时有很大不同与yield命令配合可以实现暂停执行的功能)


# 1. js对象拷贝  
    浅拷贝： 
    ```js
    <!-- Object.assign -->
    var obj = { foo: "foo", bar: "bar" };
    var copy = Object.assign({}, obj);
    <!-- ... -->
    var obj = { foo: "foo", bar: "bar" };
    var copy = { ...obj };
    ```
    深拷贝：
    ```js
    <!-- 这个方法只在对象包含可序列化值，并且没有循环引用的时候有用。其中一个不可序列化的类型的就是日期对象 - 尽管它显示出来是字符串化的ISO格式,JSON.parse只会把它解析成为一个字符串,而不是日期类型 -->
    var obj = { a: 0, b: { c: 0 } };
    var copy = JSON.parse(JSON.stringify(obj));


    <!-- 自定义深度拷贝 -->
    function deepClone(obj) {
        var copy;
        // Handle the 3 simple types, and null or undefined
        if (null == obj || "object" != typeof obj) return obj;
        // Handle Date
        if (obj instanceof Date) {
            copy = new Date();
            copy.setTime(obj.getTime());
            return copy;
        }

        // Handle Array
        if (obj instanceof Array) {
            copy = [];
            for (var i = 0, len = obj.length;
                i < len;
                i++) {
                copy[i] = deepClone(obj[i]);
            }
            return copy;
        }

        // Handle Function
        if (obj instanceof Function) {
            copy = function () {
                return obj.apply(this, arguments);
            }
            return copy;
        }

        // Handle Object
        if (obj instanceof Object) {
            copy = {};
            for (var attr in obj) {
                if (obj.hasOwnProperty(attr)) copy[attr] = deepClone(obj[attr]);
            }
            return copy;
        }

        throw new Error("Unable to copy obj as type isn't supported " + obj.constructor.name);
    }

    ```
#  2. 数组遍历：  
    ```javascript
    a = [1,2,3,4];
    b = a.map((item, index) => {
     return item+1
    });
  
    //结果 b = [2,3,4,5]
    ```
    
#  3. Array:  

    *  Array.from(arrayLike[, mapFunction[, thisArg]])  
        * arrayLike：必传参数，想要转换成数组的伪数组对象或可迭代对象。  
        * mapFunction：可选参数，mapFunction(item，index){…} 是在集合中的每个项目上调用的函数。返回的值将插入到新集合中。  
        * thisArg：可选参数，执行回调函数 mapFunction 时 this 对象。这个参数很少使用  
        
        
    ``` javascript
    
    
    //浅拷贝一个数组
    const numbers = [3, 6, 9];
    const numbersCopy = Array.from(numbers);
    
    numbers === numbersCopy; // => false
    
    
    //使用值填充数组
    const length = 3;
    const init   = 0;
    const result = Array.from({ length }, () => init);
    
    result; // => [0, 0, 0]

    const length = 3;
    
    // 使用对象填充数组(fill() 方法创建的 resultB 使用相同的空对象实例进行初始化。不会跳过空项。)
    const resultA = Array.from({ length }, () => ({}));
    const resultB = Array(length).fill({});
    
    resultA; // => [{}, {}, {}]
    resultB; // => [{}, {}, {}]
    
    resultA[0] === resultA[1]; // => false
    resultB[0] === resultB[1]; // => true


    //map() 方法会跳过空项
    const length = 3;
    const init   = 0;
    const result = Array(length).map(() => init);
    result; // => [undefined, undefined, undefined]
    ```
    
# 4. 正则的使用  
    * pattern组成为:\正则\匹配模式  
    * 匹配模式如下：    
        * i:执行对大小写不敏感的匹配  
        * g:执行全局匹配（查找所有匹配而非在找到第一个匹配后停止）。  
        * m:执行多行匹配。  
    * 注意：多行匹配和匹配换行是2个东西
    ```
  
      var content = '<a href="javascript:void(0);" id="js_name">\n\rCSDN              \n       </a>';
  
      var author = content.match(/"js_name">\s+(.*?)\s*</mi);
      if(author !== null){
       console.log(author[1])
      }
      
    ```
  
# 5. Js中读取Json文件
    ```
    var fs  = require("fs")

    //异步的方式读取
    fs.readFile('./data.json',function(err,data){
        if(err){
            return console.error(err);
        }
        var companys = data.toString();//将二进制的数据转换为字符串
        companys = JSON.parse(companys);//将字符串转换为json对象
        
        console.log("***", companys)
        
    })
    
    
    //同步的方式读取
    var companys = JSON.parse(fs.readFileSync('./data.json'))
    
    console.log(companys)
    ```
  
  
# 6. 对象转换为Json字符串，和Json字符串转换成js对象
    * JOSN.stringify()
    * JSON.parse()
    
    

# 7. 数组去重
```
    Array.from( new Set(data.map( d => d['日期']) )); 
```

# 8. 读取本地文件
```

    # html中使用
    function load(name) {
        let xhr = new XMLHttpRequest(),
            okStatus = document.location.protocol === "file:" ? 0 : 200;
        xhr.open('GET', name, false);
        xhr.overrideMimeType("text/html;charset=utf-8");//默认为utf-8
        xhr.send(null);
        return xhr.status === okStatus ? xhr.responseText : null;
    }

    let text = load("test.txt");
```

# 9. 方括号 和花括号[], {}
```
    用于解析对应数组或字典中的数据
    a = [2,3,4]
    b = {"t":10, "d":20}

    const {d} = b;
    const [e,f] = a
    const [,g] = a
    console.log(d, e, f)

    # 输出
    20, 2, 3
    
```

# 10. async 和 await
## 10.1. async 是一个修饰符，async 定义的函数会默认的返回一个Promise对象resolve的值，因此对async函数可以直接进行then操作,返回的值即为then方法的传入函数
```
    async function fun0() {
        console.log(1)
        return 1
    }
    fun0().then( x => { console.log(x) })  //  输出结果 1， 1，
```
## 10.2. await 关键字 只能放在 async 函数内部， await关键字的作用 就是获取 Promise中返回的内容， 获取的是Promise函数中resolve或者reject的值, 等待异步函数的执行结果。
```
    const bbb = function(){ return 'string'}

    async function funAsy() {
       const a = await 1
       const b = await new Promise((resolve, reject)=>{
            setTimeout(function(){
               resolve('time')
            }, 3000)
       })
       const c = await bbb()
       console.log(a, b, c)
    }
    
    funAsy() //  运行结果是 3秒钟之后 ，输出 1， time , string,
```


# 11. yield 一个Generator函数与普通function的区别就是函数名前面多了一个星号 * 但是执行时有很大不同，与yield命令配合，可以实现暂停执行的功能
```
    let go = function*(x) {
      console.log('x', x);
      let a = yield x;
      console.log('xx', x);

      console.log('a', a);

      let b = yield (x + 1) + a;

      yield a + b;

      console.log('a + b =', a + b);

      return a + b;
    }
    go(10);
    let g = go(10);
    console.log(g.next());
    console.log(g.next(1000).value);
    console.log(g.next(50));
    console.log(g.next(8));
    console.log(g.next(8));

    # 结果
    x 10
    { value: 10, done: false }
    xx 10
    a 1000
    1011
    { value: 1050, done: false }
    a + b = 1050
    { value: 1050, done: true }
    { value: undefined, done: true }
```

[返回主目录](../../README.md)




