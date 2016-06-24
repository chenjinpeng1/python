#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.shortcuts import render,HttpResponse

class MyCustomMiddleware(object):
    def process_request(self, request):
        print("------in process request---")
        if request.user.username == 'alex':
            print("no permission")
            return HttpResponse("alex no perssiom")
    def process_view(self,request, view_func, view_args, view_kwargs):
        print("-------in process view------")
        print(request, view_func, view_args, view_kwargs)

    def process_response(self,request, response):
        print("------in process response----",response)
        return response

    def process_exception(self,request, exception):
        print("---coming to excectipn:",exception)


