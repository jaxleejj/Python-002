from django.shortcuts import render
from django.http import HttpResponse
from .models import T1

# Create your views here.

def index(request):
    return HttpResponse("Hello World ! this is test_page")

def show_page(request):
#麻烦老师请体谅，因工作繁忙，没按题目要求展示电影方面的资料
#为了不耽误作业，大概按照作业的核心要点，快速学习整套django流程，
#只好拿了老师视频中现成的 t1.sql 书评文件作为原始数据导入mysql，展示书评方面信息以完成作业
    to_show=T1.objects.all().filter(n_star__gte=3)
    return render(request, 'index.html', locals())


