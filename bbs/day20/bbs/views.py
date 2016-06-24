from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
from  bbs import models
import json
from bbs import comment_hander
from bbs import get_comment
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
        print('----------接收ajax的数据',request.POST)
    article_obj = models.Article.objects.get(id=article_id)
    comment_tree = get_comment.get_comment(article_obj.comment_set.select_related().order_by("date"))
    # print('------------视图接收的数据',comment_tree)
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
    print('---->article_obj:',article_obj)
    # comment_tree = comment_hander.build_tree(article_obj.comment_set.select_related())
    comment_tree = get_comment.get_comment(article_obj.comment_set.select_related().order_by("parent_comment",'-id'))
    print(comment_tree)
    # tree_html = comment_hander.render_comment_tree(comment_tree)
    return HttpResponse(comment_tree)