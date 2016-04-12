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
	
	




