from django.shortcuts import render
from apps.organizations.models import City,CourseOrg,Teacher
from django.views.generic.base import View
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger
from apps.organizations.forms import AddAskForm
from 
# Create your views here.
class OrgView(View):
    def get(self,request,*args,**kwargs):
        all_orgs = CourseOrg.objects.all()

        all_citys = City.objects.all()
        category = request.GET.get('ct','')
        hot_orgs = all_orgs.order_by('-click_nums')[:3]
        if category:
            all_orgs = all_orgs.filter(category=category)

        city_id = request.GET.get('city', '')
        if city_id:
            if city_id.isdigit:
                #判断输入的是否是数字
                all_orgs = all_orgs.filter(city__id=int(city_id))
        #对课程机构排序
        sort = request.GET.get('sort','')
        if sort:
            all_orgs = all_orgs.order_by(sort)
        # if sort == 'student':
        #     #根据学生人数排序
        #     all_orgs = all_orgs.order_by('students')
        # elif sort == 'courses':
        #     #根据课程数
        #     all_orgs = all_orgs.order_by('course_nums')
        org_nums = all_orgs.count()
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1
        p = Paginator(all_orgs, per_page=3 ,request=request)
        #per_page每页显示多少个
        orgs = p.page(page)
        return render(request,'org-list.html',
                      {'all_orgs':orgs,'org_nums':org_nums,'all_citys':all_citys,
                       'category':category,'city_id':city_id,'sort':sort,
                       'hot_orgs':hot_orgs})
class AddAsk(View):
    '''客户咨询模块'''
    def post(self,request,*args,**kwargs):
        userask_form = AddAskForm(request.POST)
        if userask_form.is_valid():
            """commit是提交"""
            userask_form.save(commit=True)
            return JsonResponse({
                'status':'success',
                'msg':'提交成功',
            })
        else:
            return JsonResponse({
                'status': 'fail',
                'msg': '提交出错',})