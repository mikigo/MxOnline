#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
"""
@Author:Mikigo
@Date  :2022/4/18 22:48
@Desc  :
"""
import xadmin

from apps.courses.models import Course
from apps.courses.models import Lesson
from apps.courses.models import Video
from apps.courses.models import CourseResource


class GlobalSettings:
    site_title = "统信自动化测试后台管理系统"
    site_footer = "统信自动化测试平台"
    # menu_style = "accordion"  # 侧边栏折叠


class BaseSettings:
    enable_themes = True
    use_bootswatch = True


class CourseAdmin(object):
    list_display = ["name", "desc", "detail", "degree", "learn_time", "students", "teacher"]
    search_fields = ["name", "desc", "detail", "degree", "students"]
    list_filter = ["name", "desc", "detail", "degree", "learn_time", "students", "teacher"]
    list_editable = ["degree", "desc"]


class LessonAdmin(object):
    list_display = ['course', 'name', 'add_time']
    search_fields = ['course', 'name']
    # course__name 双下划线表示，对外键中的其中一个字段进行过滤
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    list_display = ['lesson', 'name', 'add_time']
    search_fields = ['lesson', 'name']
    list_filter = ['lesson', 'name', 'add_time']


class CourseResourceAdmin(object):
    list_display = ['course', 'name', 'file', 'add_time']
    search_fields = ['course', 'name', 'file']
    list_filter = ['course', 'name', 'file', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)

xadmin.site.register(xadmin.views.CommAdminView, GlobalSettings)
xadmin.site.register(xadmin.views.BaseAdminView, BaseSettings)

