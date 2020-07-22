from django.shortcuts import render
from apps.courses.models import Course
from django.views.generic.base import View
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
class CourseView(View):
    def get(self,request,*args,**kwargs):
        #课程名称，时常，人数
        all_courses = Course.objects.order_by('-click_nums')
        #分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_courses, per_page=1 ,request=request)
        #per_page每页显示多少个
        courses = p.page(page)
        return render(request,'course-list.html',{'courses':courses})