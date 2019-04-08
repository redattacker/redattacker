from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

class IndexView(View):
    def get(self,request):
        return render(request,'index.html')


import logging

# 生成一个以当前文件名为名字的logger实例
logger = logging.getLogger(__name__)
# 生成一个名为collect的logger实例
collect_logger = logging.getLogger("collect")


class IndexLog(View):
    def get(self,request):
        logger.error("一个萌萌的请求过来了。。。。")
        logger.info("一个更萌的请求过来了。。。。")
        logger.error("这是app01里面的index视图函数")

        collect_logger.info("用户1:河南")

        return HttpResponse("OK")