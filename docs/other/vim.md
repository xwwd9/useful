



# 快捷键
* Ctrl+[ 可以取代exc
* ctrl + z 将当前操作弄到后台，用fg进行恢复

# 光标的移动
* { } : 一次跳一个段落 }, 往回跳一个段落 {
* 0 : 0跳到这一行最前面， $跳到这一行最末尾
* gj : 对于一行太长了，有自动换行的时候，可以按gj跳到下一行
* zz : 将当前行弄到中间
* zt : 将当前行弄到最上面
* zb : 将当前行弄到最下面
* H M L : 移动到屏幕的上中下方
* w W : 移动到下一个单词的开头, 大写的W B E 是以空格作为区分.
* b B : 移动到上一个单词的开头
* e E : 移动到光标所在单词的末尾
* \* \# : 移动到光标匹配的下一个或上一个单词
* % : 移动光标到括号左半部分( 包括(、{、[ )对应右半匹配部分( )、}、] )

# 搜索
* :set hlsearch 搜索结果高亮
* \# 和 \* : 会去搜索光标下的字符串
* fx : 在当前行找x


* u: 回到上一步
* ctrl + r : redo


* 有48个暂存器共存储复制的类容, a-z 0-9 等
* 在v模式下进行："ay将当前内容复制到暂存器a中, "ap将暂存器a中的类容粘贴出来


* 默认模式下vim的剪贴板和外面的剪贴板是不想通的
* set clipboard=unnamed

* 进入insert模式: i I o O a A

* 选中按d会删除选中，D会将当前光标后面类容都删除
* 选中按c会删除选中, 并进入i模式

* \>> 向右位移, set shiftwidth=2 可以设置位移长度
* \<<


# v模式下的操作
* ctrl+v : virtual block模式

* vw : 从当前位置选取到单词
* v} : 选取一个段落 
* vi+w : 选取当前光标所在的单词, vi'会选取'符号内的
* va+w : 和viw类似但会对选取一些, va'会选取包括'符号的
```
vi 和 va 的一些其他用法
i 是inner的意思 a是around的意思
vit 如果是html, 那么会选取tag中的内容 <a> asd sdf</a> 这会选取<a>中的内容
vat 会将tag一起选中
```

* viw 些前面跟的动词不一样会不一样, 可换成d或c

# 小节
* 名词: w=word s=sentence p=paragraph t=tag 
* 动词: y=yank p=paste d=delete c=change
* 范围: i=inner a=around


# 技巧
* ^ 移动到行头第一个字符, 和0类似
* ~ 大小写互换
* . 重复
* J 将下一行合并
* ctrl+u : i模式下会把前面类容清除, 这2个在终端也可以用
* ctrl+w : i模式下会删除一个word
* :! ls : 去终端执行指令过后回到vim
* :h 单词 : 查看需要的帮助文档