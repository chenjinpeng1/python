Python的WEB框架有Django、Tornado、Flask 等多种，Django相较与其他WEB框架其优势为：大而全，框架本身集成了ORM、模型绑定、模板引擎、缓存、Session等诸多功能
<h3 style="background:#3366ff">Django 流程图介绍</h3>
![](http://i.imgur.com/HLtEL0A.png)
<h3 style="background:#3366ff"></h3>
<h3 style="background:#3366ff">基本配置</h3>
<ul>
一：创建django程序
<li>终端命令： django-admin startproject sitename</li>
<li>IDE创建Django程序时，本质上都是自动执行上述命令</li>
</ul>
其他常用：
	<p>python manage.py runserver 0.0.0.0</p>
	<p>python manage.py startapp appname
	<p>python manage.py syncdb
	<p>python manage.py makemigrations
	<p>python manage.py migrate
	<p>python manage.py createsuperuser