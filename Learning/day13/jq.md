<h1>jQuery</h1>
jQuery是一个兼容多浏览器的javascript库，核心理念是write less,do more(写得更少,做得更多)，对javascript进行了封装，是的更加便捷的开发，并且在兼容性方面十分优秀。

http://www.php100.com/manual/jquery/

测试下面的页面要去jquery官网下载好jq的js文件，具体参数属性去上面的网站查询
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