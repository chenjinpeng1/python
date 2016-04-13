<h1>JavaScript</h1>
<h6>JavaScript是一门编程语言，浏览器内置了JavaScript语言的解释器，所以在浏览器上按照JavaScript语言的规则编写相应代码之，浏览器可以解释并做出相应的处理。</h6>
1、JavaScript代码存在形式
	
	方式一
		<script type"text/javascript" src="js文件"></script>
	方式二
		<script type"text/javascript">
			js代码内容
		<script>
2、JavaScript代码存在的位置
	
	Html的head中
	Html的body代码底部（推荐）
	由于Html代码是从上到下执行，如果Head中的js代码耗时严重，就会导致用户长时间无法看到页面，如果放置在body代码块底部，那么即使js代码耗时严重，也不会影响用户看到页面效果，只是js实现特效慢而已。
&nbsp;
	
	如： 
	<script src="https://www.gstatic.com/og/_/js/k=og.og2.en_US.iF4jnkQuaf0.O/rt=j/t=zcms/m=def/exm=in,fot/d=1/ed=1/rs=AA2YrTv5-POC4Ks9GtGRdY2ywUWisqz7-Q"></script>
	<script>
	    alert('123');
	</script>
3、变量

	全局变量
	局部变量 （尽量使用局部变量 避免出错）
	JavaScript中变量的声明是一个非常容易出错的点，局部变量必须是一个var开头，则默认表示全局变量
	局部变量：	var name = "chen"
	全局变量:	age = 18
    var a1='chen',a2='zhang',a3=1 多行声明变量
4、 注释

    单行注释 //
    多行注释 /*   */

5、 基本数据类型

数字

    两种方式
        var age = 18;
        var age = Number("18")；
    将一个字符串转换为数字类型
        Number('123');
        parseInt（'123'）;
        n2='123';
        a=parseInt(n2); # 必须赋值给变量才会生效，不会直接将原变量的类型进行改变
        转换为float类型
        parsefloat('18.9');
    调试js
        console.log(age);
        age 类型 console.log(age,typeof age);
        或者在html F12中的Console里也可以直接进行测试和调试
字符串

    var age = '18';
	var	name = String("chen");
	var age_str = String(18);
	常用方法
	obj.trim()过滤空格
	obj.charAt(index) 获取下标对应的字符串
	obj.substring(start,end)返回位于String对象中指定位置的子字符串
	obj.indexOf(char)返回字符串索引位置
	obj.length 字符串长度
数组

        num = [11,22,33]
        num.unshift("aa") 前插入
        num.push（'bb''） 后插入 追加
        num.splice(1,0,'bbb')指定插入(中间的0必须要加，只有为0的时候才会帮你去插入)
        li.splice(1,3) 删除索引位置后的三个元素 （obj.splice(index,count)         数组指定位置后count个字符）
        li.slice(0,2) 切片
        num.pop() 删除最后一个值，并获取
        num.shift() 删除第一个值
        num.concat(n) 数组合并
            n=['a','b']
        num.rerverse（）  翻转
        num.join('-') 字符串格式化

字典（js中的字典是数组伪造出来的“数组(字典)）

        dic = {'k1':'v1'}

序列化

         s=JSON.stringify(dic)
         JSON.parse(s)
布尔

        Boolean(1) true
        Boolean(0) false
undefined
	
	undefined表示未定义值
null

	null是一个特殊值
6、条件语句

	 for 循环
            数组
                var li = [11,22,33,44];
                for(var index in li){
                    console.log(index,li[index]);
                    }
                for (var i=0;i<li.length;i++){
                    console.log(i,li[i])；
                }
            字典
                var dic = {"k1":11,"k2":22}
                for (var key in dic){
                    console.log(key)；
                }

            while 循环
                while (li.length<10){
                    console.log("小于10")
                    li.push("aa")
                    console.log(li)
                    continue

                }
            switch 循环
                switch (li){
                    case li.length <5:
                        console.log("小于5");
                        break;
                    case li.length < 8:
                        console.log("小于8");
                        break;
                    default:
                        console.log("大于8")
                }
            try 异常检错
                try{
                    li.sasasasasas(2)
                }
                    catch (e){
                        console.log("异常")
                    }
                    finally {
                        console.log("完成")
                    }
7、函数

	 function func1(arg){
                console.log(arg);
                return "aaa";
            };
            var ret = fun1("123");
            console.log(ret)

            匿名函数
            var f = function(arg){
                console.log(arg);
            }
            f(1234)

            自执行函数
                ()();
                (function(arg){
                    console.log("111",arg)
                    })("chen");

        10 类（函数模拟类）
            function fun1(name,age){
                this.Name = name;
                this.Age = age;
                this.fun2 = function(arg){
                    return this.Name + arg;
                }
            }
            var obj = new fun1("chen","18");
            console.log(obj.Name);
            console.log(obj.Age);
            var ret = obj.fun2("66666")
            console.log(ret); 
Dom

文档对象模型（Document Object Model，DOM）是一种用于HTML和XML文档的编程接口。它给文档提供了一种结构化的表示方法，可以改变文档的内容和呈现方式。我们最为关心的是，DOM把网页和脚本以及其他的编程语言联系了起来。DOM属于浏览器，而不是JavaScript语言规范里的规定的核心内容。

注：一般说的JS让页面动起来泛指JavaScript和Dom
1、选择器

	document.getElementByid('id');
	document.getElementsByname('name');
	document.getElementsByTagName('tagname');
	document.getElementsByClassName('c1');
2、操作内容

	obj.innerText   获取文本内容
	obj.innerText = 'hello' 设置文本内容
	obj.innerHtml	获取html内容
	obj.innerHtml = <h1>hello</h1>

	var nid = document.getElementByid('myid') 获取用户id的值的信息
	nid.innerText="change_id"</script> 修改信息

	特殊的：
		input系列
		textarea标签
		select标签
		对于上述的特殊的标签可以用value属性修改标签的value值
3、创建标签

需求 点击添加 添加文本框
<div  id="container"></div>
<a onclick="return AddElement()">添加</a>

	方式一：
		<div  id="container">		
		</div>
		<a href="http://www.baidu.com" onclick="return AddElement()">添加</a>

	    var nid = document.getElementById("container");
	    var tag = "<input type='text'/>";
	    nid.innerHTML = tag;
	    return false
		注意:如果，创建按钮有href属性，又有onclick属性，则先触发onclick属性，在触发href属性，若不想触发href，则删除或者函数返回false
上述添加只能添加一次，就失效了，因为它是替换了div里的元素
&nbsp;

	方式二：
		<div  id="container">		
		</div>
		<a href="http://www.baidu.com" onclick="return AddElement()">添加</a>
		function AddElement(){
	    var createObj = document.createElement("a")
	    createObj.href = "http://www.baidu.com";
	    createObj.innerText = "百度"
	    var nid = document.getElementById("container");
	    nid.appendChild(createObj);}
	    return false
	实例二：（替换样式）
		function bb(){
		    nid = document.getElementById("aa")
		    nid.style.color = "blue"
		    nid.style.fontSize = "160px"}

4、标签属性

	function aa(){
    var nid = document.getElementById('container')
    console.log(nid.id)
    console.log(nid.className)
    console.log(nid.style.fontSize='88px')
}

5、提交表单
		
	document.geElementById('form').submit()
	---------
		<!DOCTYPE html>
		<html lang="en">
		<head>
		    <meta charset="UTF-8">
		    <title>Title</title>
		</head>
		<body>
		<form id="aa" action="https://www.sogou.com/web" method="get">
		    <input name="query" type="text"/>
		    <input type="submit"  value="提交">
		    <!--另一种方式-->
		    <div onclick="mysubmit()">提交</div>
		
		</form>
		<script>
		    function mysubmit(){
		        document.getElementById("aa").submit();
		    }
		</script>
		</body>
		</html>
6、事件
<div>
<table>
<tr>
	<td style=background-color:#676767>属性</td>
	<td style=background-color:#676767>此事件发生在何时...</td>
</tr>
<tr>
	<td>onabort</td>
	<td>图像的加载被中断。</td>
</tr>
<tr>
	<td>onblur</td>
	<td>元素失去焦点。</td>
</tr>
<tr>
	<td>onchange</td>
	<td>域的内容被改变。</td>
</tr>
<tr>
	<td>onclick</td>
	<td>当用户点击某个对象调用的事件句柄。</td>
</tr>
<tr>
	<td>ondblclick</td>
	<td>当用户双击某个对象时调用的事件句柄。</td>
</tr>
<tr>
	<td>onerror</td>
	<td>在加载文档或图像时发生错误。</td>
</tr>
<tr>
	<td>onfocus</td>
	<td>元素获得焦点。</td>
</tr>
<tr>
	<td>onkeydown</td>
	<td>某个键盘按键被按下。</td>
</tr>
<tr>
	<td>onkeypress</td>
	<td>某个键盘按键被按下并松开。</td>
</tr>
<tr>
	<td>onkeyup</td>
	<td>某个键盘按键被松开。</td>
</tr>
<tr>
	<td>onload</td>
	<td>一张页面或者一副图像加载完成。</td>
</tr>
<tr>
	<td>onmousedown</td>
	<td>鼠标按钮被按下。</td>
</tr>
<tr>
	<td>onmousemove</td>
	<td>鼠标被移动。</td>
</tr>
<tr>
	<td>onmouseout</td>
	<td>鼠标从某元素已开。</td>
</tr>
<tr>
	<td>onmouseover</td>
	<td>鼠标移动到某元素之上。</td>
</tr>
<tr>
	<td>onmouseup</td>
	<td>鼠标按键被松开。</td>
</tr>
<tr>
	<td>onreset</td>
	<td>重置按钮被点击。</td>
</tr>
<tr>
	<td>onresize</td>
	<td>窗口或框架被重新调整大小。</td>
</tr>
<tr>
	<td>onselect</td>
	<td>文本被选中。</td>
</tr>
<tr>
	<td>onsubmit</td>
	<td>确认按钮被点击。</td>
</tr>
<tr>
	<td>onunload</td>
	<td>用户退出页面。</td>
</tr>
</table>
</div>
特殊的：
		
	window.onload = function(){}
	    //jQuery：$(document).ready(function(){})
	    //onload是所有DOM元素创建、图片加载完毕后才触发的。而ready则是DOM元素创建完毕后触发的，不等图片加载完毕。图片还没有渲染，就可以进行事件的执行。
特殊参数：this,event
7、其他功能

	console.log()
	//用于显示一个带有指定消息和 OK 及取消按钮的警告框
	alert() 
	//用于显示一个带有指定消息和 OK 及取消按钮的对话框
	confirm()
	 
	// URL和刷新
	location.href
	location.href = "url"  window.location.reload()
	 
	// 定时器
	/*setInterval() 方法可按照指定的周期（以毫秒计）来调用函数或计算表达式。setInterval() 方法会不停地调用函数，直到 clearInterval() 被调用或窗口被关闭。由 setInterval() 返回的 ID 值可用作 clearInterval() 方法的参数。*/
	setInterval("alert()",2000);   
	//clearInterval() 方法可取消由 setInterval() 设置的 timeout。clearInterval() 方法的参数必须是由 setInterval() 返回的 ID 值。
	clearInterval(obj)
	//超时时间
	setTimeout();   
	clearTimeout(obj)

  实例

	<!DOCTYPE html>
	<html>
    <head>
        <meta charset='utf-8' >
        <title>欢迎blue shit莅临指导&nbsp;&nbsp;</title>
        <script type='text/javascript'>
            function Go(){
                var content = document.title;
                var firstChar = content.charAt(0)
                var sub = content.substring(1,content.length)
                document.title = sub + firstChar;
            }
            setInterval('Go()',1000);
        </script>
    </head>
    <body>    
    </body>
	</html>
&nbsp;

	<!DOCTYPE html>
	<html>
    <head>
        <meta charset='utf-8' />
        <title></title>
        
        <style>
            .gray{
                color:gray;
            }
            .black{
                color:black;
            }
        </style>
        <script type="text/javascript">
            function Enter(){
               var id= document.getElementById("tip")
               id.className = 'black';
               if(id.value=='请输入关键字'||id.value.trim()==''){
                    id.value = ''
               }
            }
            function Leave(){
                var id= document.getElementById("tip")
                var val = id.value;
                if(val.length==0||id.value.trim()==''){
                    id.value = '请输入关键字'
                    id.className = 'gray';
                }else{
                    id.className = 'black';
                }
            }
        </script>
    </head>
    <body>
        <input type='text' class='gray' id='tip' value='请输入关键字' onfocus='Enter();'  onblur='Leave();'/>
    </body>
	</html>
	
	搜索框
