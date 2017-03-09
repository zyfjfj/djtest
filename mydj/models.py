#coding=utf-8
from __future__ import unicode_literals

from django.db import models


# Create your models here.
#一本书由一家出版社出版，一家出版社可以出版很多书。一本书由多个作者合写，一个作者可以写很多书。

class Author(models.Model):
    name = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Publisher(models.Model):
    name = models.CharField(max_length=20)


    def __unicode__(self):
        return self.name
class Book(models.Model):
    name = models.CharField(max_length=20)
    pub = models.ForeignKey(Publisher, blank=True, null=True,on_delete=models.SET_NULL)
    authors = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.name

# 题目
class Items(models.Model):
    class Meta:
        verbose_name = '题目'
        verbose_name_plural = '题目'
    name = models.CharField(verbose_name="题目", max_length=100)
    parameter = models.CharField(verbose_name='参数', max_length=10, blank=True)
    answer = models.ManyToManyField('Answers', blank=True, verbose_name='答案')

    def get_answers(self):
        return "； ".join([(unicode(p.answer_name) + u"," + unicode(p.score)) for p in self.answer.all()])


    def __unicode__(self):
        return self.name

class Answers(models.Model):
    class Meta:
        verbose_name = '答案'
        verbose_name_plural = '答案'
        ordering = ['score']
    name = models.CharField(verbose_name="答案", max_length=100)
    score = models.IntegerField(verbose_name="分数", blank=True)

    def __unicode__(self):
        return self.answer_name + u":" + str(self.score)

class ItemAnswer(models.Model):
    item=models.ForeignKey(Items)
    answer=models.ForeignKey(Answers)

    def __unicode__(self):
        return self.item.name + u":" + self.answer.name

class Subject(models.Model):
    class Meta:
        verbose_name = '被试'
        verbose_name_plural = '被试'

    identity = models.CharField(verbose_name='学号/身份证号', max_length=18)
    item_answer = models.ManyToManyField(ItemAnswer, blank=True, verbose_name='答案')
    score = models.IntegerField(blank=True, verbose_name="得分")


    def __unicode__(self):
        return self.identity
