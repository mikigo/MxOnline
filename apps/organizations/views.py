from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from apps.organizations.models import CourseOrg
from apps.organizations.models import City


class OrgView(View):

    def get(self, request, *args, **kwargs):
        # 从数据库中获取数据
        all_orgs = CourseOrg.objects.all()
        org_num = CourseOrg.objects.count()
        all_city = City.objects.all()
        return render(request, "org-list.html", {
            "all_orgs": all_orgs,
            "org_num": org_num,
            "all_city": all_city,
        })
