from django.shortcuts import render
from apps.organizations.models import City,CourseOrg,Teacher
from django.views.generic.base import View
from pure_pagination import Paginator,EmptyPage,PageNotAnInteger
# Create your views here.
class OrgView(View):
    def get(self,request,*args,**kwargs):
        all_orgs = CourseOrg.objects.all()

        all_citys = City.objects.all()
        # city_id = request.GET.get('city','')
        category = request.GET.get('ct','')

        if category:
            all_orgs = all_orgs.filter(category=category)

        city_id = request.GET.get('city', '')
        if city_id:
            if city_id.isdigit:
                #判断输入的是否是数字
                all_orgs = all_orgs.filter(city__id=int(city_id))
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
                       'category':category,'city_id':city_id})