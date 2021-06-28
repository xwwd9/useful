


# 1. html css笔记

[返回上一级](../README.md)


- [1. html css笔记](#1-html-css笔记)
- [2. css](#2-css)
  - [2.1. 选择器](#21-选择器)
  - [2.2. boder 边框](#22-boder-边框)
  - [2.3. background-color：背景颜色](#23-background-color背景颜色)
  - [2.4. padding: 内边距](#24-padding-内边距)
  - [2.5. margin: 外边距](#25-margin-外边距)
  - [2.6. transform](#26-transform)
- [3. html](#3-html)
  - [3.1. <h>：代表标题， h1主标题， h2副标题，依次类推。](#31-h代表标题-h1主标题-h2副标题依次类推)
  - [3.2. <p>：代表段落](#32-p代表段落)
  - [3.3. 给标签添加样式：](#33-给标签添加样式)
  - [3.4. 可以应用多个class到一个元素，用空格分开即可](#34-可以应用多个class到一个元素用空格分开即可)
  - [3.5. 报warning，可以设置 href="#" 为死链接](#35-报warning可以设置-href-为死链接)
  - [3.6. 每一张图片都应该有一个alt属性，该属性会被搜索引擎搜索。](#36-每一张图片都应该有一个alt属性该属性会被搜索引擎搜索)
  - [3.7. 每个页面都有一个body元素， 并且所有其他元素将继承body元素的样式。](#37-每个页面都有一个body元素-并且所有其他元素将继承body元素的样式)
  - [3.8. HTML DOM Element 对象](#38-html-dom-element-对象)
    - [3.8.1. textContent 设置或返回节点及其后代的文本内容。](#381-textcontent-设置或返回节点及其后代的文本内容)
- [svg](#svg)
  - [text-anchor](#text-anchor)
# 2. css

## 2.1. 选择器
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
  
    4. :first-of-type 选择器匹配元素其父级是特定类型的第一个子元素。
    ```


## 2.2. boder 边框 
    ```
    img {
        border-color: green;
        border-width: 10px;
        border-style: solid;
        border-radius:10px;(50%)
      }
    
    ```
    
## 2.3. background-color：背景颜色
    ```
    background-color: gray;
    ```

## 2.4. padding: 内边距
    ```
    
    ```


## 2.5. margin: 外边距
    ```
    
    ```

## 2.6. transform
```
    # 对于x，y的平移
    transform: translate(0,100px);
```

## 文本多余用省略号，隐藏多余文本
```css
    word-break: break-all;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 5;
    overflow: hidden;
```



# 3. html
## 3.1. <h>：代表标题， h1主标题， h2副标题，依次类推。

## 3.2. <p>：代表段落


## 3.3. 给标签添加样式：  
    ```
    1.内联样式
    <h2 style="color: blue">what</h2> 
    
    
    2.统一设置(以下选择h2标签设置)
    
    <style>
      h2 {color:blue;}
    </style>
    
    <h2>cat</h2>
    ```
    
## 3.4. 可以应用多个class到一个元素，用空格分开即可
    ```
    <img class="class1 class2">
    ```
    
## 3.5. 报warning，可以设置 href="#" 为死链接


## 3.6. 每一张图片都应该有一个alt属性，该属性会被搜索引擎搜索。

## 3.7. 每个页面都有一个body元素， 并且所有其他元素将继承body元素的样式。

## 3.8. HTML DOM Element 对象
### 3.8.1. textContent 设置或返回节点及其后代的文本内容。  















