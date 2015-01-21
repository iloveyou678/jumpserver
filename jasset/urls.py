# coding:utf-8
from django.conf.urls import patterns, include, url
from jasset.views import *

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^host_add/$', jadd_host),
    url(r'^host_list/$', jlist_host),
    url(r"^(\d+.\d+.\d+.\d+)/$",jlist_ip),
    url(r'^idc_add/$', jadd_idc),
    url(r'^idc_list/$', jlist_idc),
    url(r'^idc_del/(\d+)/$', idc_del),
    url(r'^group_add/$', jadd_group),
    url(r'^group_list/$', jlist_group),
    url(r'^group_del/(\d+)/$', group_del),
    url(r'^host_del/(\d+.\d+.\d+.\d+)/$', host_del),
    url(r'^host_edit/(\d+.\d+.\d+.\d+)/$', host_edit),
    url(r'^test/$', test),
)