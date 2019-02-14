#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/2/14 15:49
# @Author  : ZJJ
# @Email   : 597105373@qq.com

from django.db.models import Q
from django_filters import rest_framework as filters
from .models import Server


class ServerFilter(filters.FilterSet):
    host_ip_sn = filters.CharFilter(method="my_custom_filter")

    def my_custom_filter(self, queryset, name, value):
        # 对hostname,ip,sn进行模糊搜索
        return queryset.filter(
            Q(hostname__icontains=value) | Q(ip_managemant__icontains=value) | Q(sn__icontains=value))

    class Meta:
        model = Server
        fields = ['host_ip_sn', 'manufactory','supplier']