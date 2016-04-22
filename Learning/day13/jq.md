<h1>jQuery</h1>
jQuery是一个兼容多浏览器的javascript库，核心理念是write less,do more(写得更少,做得更多)，对javascript进行了封装，是的更加便捷的开发，并且在兼容性方面十分优秀。

http://www.php100.com/manual/jquery/

测试下面的页面要去jquery官网下载好jq的js文件，具体参数属性去上面的网站查询

jquery基础用法
	
	$("#n1").text("123"); 找到所有id=n1的元素更改内容内容为123
	$("div").text("321");找到所有的div更改内容为321
	$(".c1").text("456") 找到所有的class=c1的类更改内容 为456
	$(".c1,a,#n2").text("ok") 多个匹配修改
	层级
	$("c1 div .c1 span a").text("aaaaaa")层级匹配
	$("form > input") 寻找form表达的子级元素的input标签 子级下（孙子，外孙等等）的不寻找
	$("form + input")匹配所有紧接在form元素后的下一个input元素
	$("form ~ input")匹配form元素之后的所有 siblings(兄弟) 元素input
	--基本筛选器
	$(li:first) li标签下的第一个元素
	$("input:not(:checked)") input标签没有被选中的标签
	$("tr:even")匹配所有索引值为偶数的元素，从 0 开始计数(：odd偶数)
	$("tr:eq(1)")匹配索引值等于1的元素
	--内容匹配
	$("div:contains('John')") 匹配DIV下的内容为John的元素 contains匹配内容 
	$("div:empty")匹配div下内容为空的
	$("div:has(p)") 匹配div下的p标签
	$("div:parent")匹配含有子元素或者文本的元素
	--属性选择器
	$("div[id]")匹配div下的id属性
	$("div[id=“test”]")匹配div下的id=test的属性【扩展：!=不等于，^=已某些值开始,$已什么结尾,*=包含某些值的】
	$("input[id][name$='man']")复合属性选择器，需要同时满足多个条件时使用。
	--子元素
	$("ul li:first-child")匹配ul下的第一个子元素li
	--表单
	$(":input")匹配表单下所有input元素
	$(":password")匹配所有type为password的元素
	--表单对象属性
	1、匹配所有选中的option元素
		<select>
		  <option value="1">Flowers</option>
		  <option value="2" selected="selected">Gardens</option>
		  <option value="3">Trees</option>
		</select>
	$("select option:selected")
	2、匹配所有选中的被选中元素(复选框、单选框等，select中的option)，对于select元素来说，获取选中推荐使用 :selected
		<form>
		  <input type="checkbox" name="newsletter" checked="checked" value="Daily" />
		  <input type="checkbox" name="newsletter" value="Weekly" />
		  <input type="checkbox" name="newsletter" checked="checked" value="Monthly" />
		</form>
	$("input:checked")


	
实例
加载

	<!DOCTYPE html>

	<html>
    <head>
        <meta charset="utf-8">
        <title>Index</title>
        <style>
            a {
                color: #428bca;
                text-decoration: none;
                }

                .modal-backdrop {
                  position: fixed;
                  top: 0;
                  right: 0;
                  bottom: 0;
                  left: 0;
                  z-index: 1050;
                  background-color: white;
                  opacity: 0.8;
                }

                .modal {
                  position: fixed;
                  top: 30%;
                  left: 50%;
                  z-index: 1030;
                }

                .hide {
                    display:none;
                }
        </style>
    </head>
    <body>
        <div>
            <input type="button" onclick="fadeIn();"  value="加载条"/>
        </div>
        <div id="shade" class="modal-backdrop hide">
            <div  class="modal">sss
                <img src="./images/loading_32.gif"/>
            </div>
        </div>
        <script >
            function fadeIn() {
                document.getElementById('shade').className = 'modal-backdrop';
            }

            function fadeOut() {
                document.getElementById('shade').className = 'modal-backdrop hide';
            }
        </script>
    </body>
	</html>

左侧菜单

	<!DOCTYPE html>
	<html lang="en">
	<head>
    <meta charset="UTF-8">
    <title>Title</title>
     <style>
        .menu{
            float: left;width: 30%;height: 500px;background-color: antiquewhite;
        }
        .content{
            float: left;width: 70%;height: 500px;background-color: blue;
        }
        .title{
            background-color: black;
            color: white;
            height: 50px;
            line-height: 50px;
        }
        .hide{
            display: none;
        }
    </style>

	</head>
	<body>
	<div>
        <div class="menu">
            <div class="item">
				// this是js里特殊的参数，把它自己的名字（菜单一）传入函数
                <div class="title" onclick="Func(this);">菜单一</div>
                <div class="body">
                    <div>1.1</div>
                    <div>1.2</div>
                    <div>1.3</div>
                </div>
            </div>

            <div class="item">
                 <div class="title" onclick="Func(this);">菜单二</div>
                <div class="body hide">
                    <div>2.1</div>
                    <div>2.2</div>
                    <div>2.3</div>
                </div>
            </div>

            <div class="item">
                 <div class="title" onclick="Func(this);">菜单三</div>
                <div class="body hide">
                    <div>3.1</div>
                    <div>3.2</div>
                    <div>3.3</div>
                </div>
            </div>

        </div>
        <div class="content"></div>
    </div>


	<script src="jquery-2.2.3.min.js"></script>
	<script>
    function Func(ths){
        if(!$(ths).next().hasClass('hide')){
            console.log('aaaaaa')
            $(ths).next().addClass('hide');
        }else{
            $(ths).next().removeClass('hide');
        }
       
        $(ths).parent().siblings().find('.body').addClass('hide')
    }
	</script>
	</body>
	</html>

返回顶部

	<!DOCTYPE html>
	<html lang="en">
	<head>
    <meta charset="UTF-8">
    <title></title>
    <style>
        .back{
            position: fixed;
            bottom: 0px;
            right: 0px;
        }
        .hide{
            display: none;
        }
    </style>
	</head>
	<body>
	
	<div style="height: 2000px;"></div>
	
	<div onclick="GoTop()" class="back hide">返回顶部</div>
	
	<script src="../jquery-2.2.3.min.js"></script>
	<script type="text/javascript">

    function GoTop(){
        //返回顶部
        $(window).scrollTop(0);
    }

    $(function(){

        $(window).scroll(function(){
            //当滚动滑轮时，执行函数体

            //获取当前滑轮滚动的高度
            var top = $(window).scrollTop();

            if(top>100){
                //展示“返回顶部”
                $('.back').removeClass('hide');
            }else{
                //隐藏“返回顶部”
                $('.back').addClass('hide');
            }
        });
    });

	</script>
	
	</body>
	</html>
	
	实例：返回顶部


更多属性访问 http://www.php100.com/manual/jquery/