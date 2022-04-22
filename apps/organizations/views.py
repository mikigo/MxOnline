from django.shortcuts import render
from django.views.generic.base import View
# Create your views here.
from apps.organizations.models import CourseOrg


class OrgView(View):

    def get(self, request, *args, **kwargs):
        # 从数据库中获取数据
        all_orgs = CourseOrg.objects.all()
        return render(request, "org-list.html", {
            "all_orgs": all_orgs
        })
