from django.shortcuts import render
import urllib
# Create your views here.
# from api.modules import saltapi
from ESZCMDB import settings

def update_asset_info(request):
    if request.method == 'POST':
        print(request.POST)
        POST_DATA = request.POST.get('tgt')
        url = settings.SALT_API['url']
        username = settings.SALT_API['username']
        password = settings.SALT_API['password']
        obj = core.SALT_API(url=url,username=username,password=password)
        obj.token_id()
        # print(a.remote_execution_func(tgt="*",fun="cmd.run",arg='free -m'))
        obj_data = obj.remote_execution_module(tgt='chen',fun='grains.items')


def assetinfo(request):
    pass