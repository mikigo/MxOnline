from datetime import datetime

from django.db import models

from apps.users.models import BaseModel
from apps.organizations.models import Teacher
"""
设计表结构
实体之间的关系（一对多），定义具体字段（类型，是否必填）
1、Course 课程基本信息
2、Lesson 章节信息
3、Video 视频
4、CourseResource 课程资源
"""
DEGREE_CHOICES = (
    ("cj", "初级"),
    ("zj", "中级"),
    ("gj", "高级"),
)


class Course(BaseModel):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="讲师")
    name = models.CharField(max_length=100, verbose_name="课程名")
    desc = models.CharField(max_length=1000, verbose_name="课程描述")
    learn_time = models.IntegerField(default=0, verbose_name="学习时长（分钟数")  # 存数据库用秒级别
    degree = models.CharField(max_length=2, verbose_name="难度", choices=DEGREE_CHOICES)
    students = models.IntegerField(default=0, verbose_name="学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name="收藏人数")
    click_nums = models.IntegerField(default=0, verbose_name="点击数")
    category = models.CharField(max_length=20, verbose_name="课程类别", default="后端开发")
    tag = models.CharField(max_length=10, verbose_name="课程标签", default="")
    youneed_now = models.CharField(max_length=300, verbose_name="课程须知", default="")
    teacher_tell = models.CharField(max_length=300, verbose_name="老师告诉你", default="")
    detail = models.TextField(verbose_name="课程详情")  # 富文本
    image = models.ImageField(max_length=100, upload_to="courses/%Y/%m", verbose_name="封面图")

    class Meta:
        verbose_name = "课程信息"
        verbose_name_plural = verbose_name


class Lesson(BaseModel):
    # on_delete表示对应的外键数据被删除后，当前数据应该怎么办
    # CASCADE表示关联删除， SET_NULL表示置为null(on_delete=models.SET_NULL, null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="章节名")
    learn_time = models.IntegerField(default=0, verbose_name="学习时长（分钟数）")

    class Meta:
        verbose_name = "章节信息"
        verbose_name_plural = verbose_name


class Video(BaseModel):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="视频名称")
    learn_times = models.IntegerField(default=0, verbose_name="学习时长（分钟数）")
    url = models.CharField(max_length=200, verbose_name="访问地址")

    class Meta:
        verbose_name = "视频"
        verbose_name_plural = verbose_name


class CourseResource(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name="名称")
    file = models.FileField(max_length=200, upload_to="course/resource/%Y/%m", verbose_name="下载地址")

    class Meta:
        verbose_name = "课程资源"
        verbose_name_plural = verbose_name
