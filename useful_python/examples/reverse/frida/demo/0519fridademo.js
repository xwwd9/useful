//打印参数、返回值
function Login(){
    Java.perform(function(){
        Java.use("com.example.androiddemo.Activity.LoginActivity").a.overload('java.lang.String', 'java.lang.String').implementation = function (str, str2){
            var result = this.a(str, str2);
            console.log("args0:"+str+" args1:"+str2+" result:"+result);
            return result;
        }
    })
}

//直接把返回值喂给函数
function challenge1(){
    Java.perform(function(){
        Java.use("com.example.androiddemo.Activity.FridaActivity1").a.implementation = function(bArr){
            console.log("inside Frida1 a function")
            return Java.use('java.lang.String').$new("R4jSLLLLLLLLLLOrLE7/5B+Z6fsl65yj6BgC6YWz66gO6g2t65Pk6a+P65NK44NNROl0wNOLLLL=");
        }
    })
}

function challenge2(){
    Java.perform(function(){
        //hook静态函数直接调用
        var FridaActivity2 = Java.use("com.example.androiddemo.Activity.FridaActivity2")
        FridaActivity2.setStatic_bool_var();
        
        //hook动态函数，找到instance实例，从实例调用函数方法
        Java.choose("com.example.androiddemo.Activity.FridaActivity2",{
            onMatch:function(instance){
                instance.setBool_var();
            },onComplete:function(){}
        })

    })
}


function challenge3(){
    Java.perform(function(){
        var Frida3 = Java.use("com.example.androiddemo.Activity.FridaActivity3");
        
        //静态成员变量可以直接设置结果
        Frida3.static_bool_var.value = true;
        console.log("After set new value 1:"+Frida3.static_bool_var.value);

        //动态成员变量需要找到实例，给实例设置结果；
        Java.choose("com.example.androiddemo.Activity.FridaActivity3",{
            onMatch:function(instance){
                instance.bool_var.value = true ;
                console.log("After set new value 2:"+instance.bool_var.value);
                instance._same_name_bool_var.value = true ;
                console.log("After set new value 3:"+instance._same_name_bool_var.value);
            },onComplete:function(){}
        })

    })
}

function challenge4(){
    Java.perform(function(){
        //内部类
        Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check1.implementation = function(){return true;}
        Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check2.implementation = function(){return true;}
        Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check3.implementation = function(){return true;}
        Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check4.implementation = function(){return true;}
        Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check5.implementation = function(){return true;}
        Java.use("com.example.androiddemo.Activity.FridaActivity4$InnerClasses").check6.implementation = function(){
            console.log("enter check6")
            return true;
        }
    })
}

function challenge42(){
    Java.perform(function(){
        var class_name = "com.example.androiddemo.Activity.FridaActivity4$InnerClasses"
        var InnerClass = Java.use(class_name);
        var all_methods = InnerClass.class.getDeclaredMethods();
        console.log(all_methods);
        for(var i = 0;i<all_methods.length;i++){
            var method = all_methods[i];
            console.log(method);
            var methodStr = method.toString();
            var substring = methodStr.substr(methodStr.indexOf(class_name)+class_name.length+1);
            var finalMethodString = substring.substr(0,substring.indexOf("("));
            console.log(finalMethodString);
            InnerClass[finalMethodString].implementation = function(){return true};
        }
    })
}


function challenge5(){
    Java.perform(function(){
        Java.choose("com.example.androiddemo.Activity.FridaActivity5",{
            onMatch:function(instace){
                console.log(instace.getDynamicDexCheck().$className)
            },onComplete:function(){}
        })

        Java.enumerateClassLoaders({
            onMatch:function(loader){
                try{
                    if(loader.findClass("com.example.androiddemo.Dynamic.DynamicCheck")){
                        console.log("Successfully found loader")
                        console.log(loader);
                        Java.classFactory.loader = loader ;
                    }
                }catch(error){
                    console.log("find error:"+error)
                }
            },onComplete:function(){}
        })

        var DynamicCheck = Java.use("com.example.androiddemo.Dynamic.DynamicCheck");
        console.log(DynamicCheck);
        DynamicCheck.check.implementation = function(){return true};
    })
}


function challenge6(){
    Java.perform(function(){
        Java.use("com.example.androiddemo.Activity.Frida6.Frida6Class0").check.implementation = function(){return true};
        Java.use("com.example.androiddemo.Activity.Frida6.Frida6Class1").check.implementation = function(){return true};
        Java.use("com.example.androiddemo.Activity.Frida6.Frida6Class2").check.implementation = function(){return true};
    })
}


//枚举class，trace原型2
function challenge62(){
    Java.perform(function(){
        Java.enumerateLoadedClasses({
            onMatch:function(name,handle){
                //console.log("name:"+name+" handle:"+handle)
                if(name.indexOf("com.example.androiddemo.Activity.Frida6")>=0){
                    console.log("name:"+name+" handle:"+handle)
                    Java.use(name).check.implementation=function(){return true}
                }
            },onComplete:function(){}
        })
    })
}

setImmediate(challenge62)