from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
from  bbs import models
import json
from bbs import comment_hander
from bbs import get_comment
from bbs import form
category_list = models.Category.objects.filter(set_as_top_menu=True).order_by('position_index')
def index(request):
    category_obj = models.Category.objects.get(position_index=1)
    article_list = models.Article.objects.filter(status='published')
    return render(request,'bbs/index.html',{'category_list':category_list,
                                            'article_list':article_list,
                                             'category_obj':category_obj,
                                            })


def category(request,id):
    category_obj = models.Category.objects.get(id=id)
    if category_obj.position_index == 1:#首页
        article_list = models.Article.objects.filter(status='published')
    else:
        article_list = models.Article.objects.filter(category_id = category_obj.id,status='published')
    return render(request,'bbs/index.html',{'category_list':category_list,
                                            'category_obj':category_obj,
                                            'article_list':article_list
                                            })


def acc_login(request):
    if request.method == 'POST':
        print(request.POST)
        user = authenticate(username=request.POST.get('username'),
                            password=request.POST.get('password'))
        if user is not None:
            #pass authentication
            login(request,user)
            print(request.user.userprofile.name)
            return HttpResponseRedirect(request.GET.get('next') or '/bbs')
        else:
            log_error = "Wrong username or password!"
            return render(request,'index.html',{'log_error':log_error})
    return render(request,'index.html')

def acc_logout(request):
    logout(request)
    return HttpResponseRedirect('/bbs')


def article_detail(request,article_id):
    if request.method == "POST":
        data = json.loads(request.POST['data'])
        if  data['comment_type'] == 1:
            get_article_id = models.Article.objects.get(title=data['article_id'])
            user_id = models.UserProfile.objects.get(name=data['user_id']).id
            data['article_id'] = get_article_id.id
            data['user_id'] = user_id
            create_data = models.Comment.objects.create(**data)
            result_data = ["True",create_data.date.strftime('%Y-%m-%d %T')]
            return HttpResponse(json.dumps(result_data))
        elif data['comment_type'] == 2:
            data['article_id'] = models.Article.objects.get(title=data['article_id']).id
            data['user_id'] = models.UserProfile.objects.get(name=data['user_id']).id
            print('----点赞data',data)
            models.Comment.objects.create(**data)
            return HttpResponse("True")
        # result.save()
        # obj.add(**datas)
    article_obj = models.Article.objects.get(id=article_id)

    comment_tree = get_comment.get_comment(article_obj.comment_set.select_related().order_by("date"))
    return render(request,'bbs/article_detail.html',{'article_obj':article_obj,
                                                     'category_list':category_list,
                                                     'comment_tree':comment_tree})

def comment(request):
    print(request.POST)
    if request.method == 'POST':
        new_comment_obj = models.Comment(
            article_id = request.POST.get('article_id'),
            parent_comment_id = request.POST.get('parent_comment_id') or None,
            comment_type = request.POST.get("comment_type"),
            user_id = request.user.userprofile.id,
            comment = request.POST.get('comment')
        )
        new_comment_obj.save()

        return HttpResponse('post-comment-success')


def get_comments(request,article_id):
    article_obj = models.Article.objects.get(id=article_id)
    comment_tree = get_comment.get_comment(article_obj.comment_set.select_related().order_by("parent_comment",'-id'))
    return HttpResponse(comment_tree)

# @login_required(login_url='/login/')           写法1
#setting配置文件里最后协商 LOGIN_URL = '/login/' 写法2
@login_required
def new_article(request):
    if request.method == 'GET':
        article_form = form.ArticleModelForm()
        return render(request,'bbs/new_article.html',{"article_form":article_form})
    elif request.method == 'POST':
        # print(request.POST)
        # print('---------request_file:',request.FILES)
        article_form = form.ArticleModelForm(request.POST,request.FILES)
        if article_form.is_valid():
            print('----',article_form.cleaned_data)
            print(request.user)
            # article_form.cleaned_data['author_id'] = request.user.userprofile.id
            print("发布成功")
            data =article_form.cleaned_data #将验证好的数据转换成字典
            data['author_id'] = request.user.userprofile.id # 将用户id塞进去
            article_obj = models.Article(**data) # 添加文章
            article_obj.save() # 保存
            return HttpResponse("发布成功")
        else:
            return render(request,'bbs/new_article.html',{"article_form":article_form})

def get_new_article_count(request):
    last_article_id=request.GET.get("lastest_id")
    new_article_count = models.Article.objects.filter(id__gt=last_article_id).count()
    return HttpResponse(new_article_count)