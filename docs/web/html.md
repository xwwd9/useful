


# html css笔记

[返回上一级](../README.md)



# css

* 选择器
    ```
    以下{...} 为样式
    1. 元素选择器：直接元素名字
        元素名称 {...}
        p {color: blue} 
        
    2. 类选择器：类名前边加个点
          .类名称 {...}
          .blue-text {
            color: blue;
          }
    3. id选择器：以#号开头
    ```


* boder 边框 
    ```
    img {
        border-color: green;
        border-width: 10px;
        border-style: solid;
        border-radius:10px;(50%)
      }
    
    ```
    
* background-color：背景颜色
    ```
    background-color: gray;
    ```

* padding: 内边距
    ```
    
    ```


* margin: 外边距
    ```
    
    ```




# html
* <h>：代表标题， h1主标题， h2副标题，依次类推。

* <p>：代表段落


* 给标签添加样式：  
    ```
    1.内联样式
    <h2 style="color: blue">what</h2> 
    
    
    2.统一设置(以下选择h2标签设置)
    
    <style>
      h2 {color:blue;}
    </style>
    
    <h2>cat</h2>
    ```
    
* 可以应用多个class到一个元素，用空格分开即可
    ```
    <img class="class1 class2">
    ```
    
* 报warning，可以设置 href="#" 为死链接


* 每一张图片都应该有一个alt属性，该属性会被搜索引擎搜索。

* 每个页面都有一个body元素， 并且所有其他元素将继承body元素的样式。