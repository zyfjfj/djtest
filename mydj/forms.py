# encoding: utf-8
"""
@version: ??
@author: zhayufeng
@describe:
@contact: zyfjfj@163.com
@software: PyCharm
@file: forms.py
@time: 2016/8/25 12:16
"""
from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label=u'姓名', max_length=100)
    up=forms.IPAddressField(label=u'ip')
    ii=forms.DateTimeField(label=u'时间')

TOPIC_CHOICES = (
        ('leve1', '差评'),
        ('leve2', '中评'),
        ('leve3', '好评'),
)

class RemarkForm(forms.Form):
    subject = forms.CharField(max_length=100, label='留言标题')
    mail = forms.EmailField(label='电子邮件')
    topic = forms.ChoiceField(choices=TOPIC_CHOICES, label='选择评分')
    message = forms.CharField(label='留言内容', widget=forms.Textarea)
    cc_myself = forms.BooleanField(required=False, label='订阅该贴')