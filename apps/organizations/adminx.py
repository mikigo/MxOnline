#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Author:Mikigo
@Date  :2022/4/18 22:48
@Desc  :
"""
import xadmin

from apps.organizations.models import Teacher
from apps.organizations.models import CourseOrg
from apps.organizations.models import City


class CourseOrgAdmin(object):
    list_display = ['name', 'desc', 'click_nums', 'fav_nums']
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums']
    style_fields = {
        "desc": "ueditor"
    }


class CityAdmin(object):
    # 列表页需要显示的字段
    list_display = ["id", "name", "desc"]
    # 搜索的时候会搜索哪些字段
    search_fields = ["name", "desc"]
    # 搜索过滤
    list_filter = ["name", "desc", "add_time"]
    # 直接在列表中编辑
    list_editable = ["name", "desc"]


class TeacherAdmin(object):
    list_display = ['org', 'name', 'work_years', 'work_company']
    search_fields = ['org', 'name', 'work_years', 'work_company']
    list_filter = ['org', 'name', 'work_years', 'work_company']


xadmin.site.register(Teacher, TeacherAdmin)
xadmin.site.register(City, CityAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
