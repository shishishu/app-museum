#!/usr/bin/env python
#coding=utf-8
# @file  : shm
# @time  : 2/13/2022 6:24 PM
# @author: shishishu

levels_map = {
    '金石': ['青铜', '雕塑', '钱币', '其他'],
    '陶瓷': [],
    '书画': ['书法', '绘画', '其他'],
    '工艺': ['玉器', '家具', '少数民族', '其他']
}

levels_stat = {}

category_map = {
    'levels_map': levels_map,
    'levels_stat': levels_stat
}

# 分页机制（防止一个目录下文件数过多）

raw_paging_org_conf = {
    1: {'main_key': 'id', 'use_hash': False, 'num_div': 20},
    2: {'main_key': 'query_id', 'use_hash': True, 'num_div': 10}
}

sort_paging_org_conf = {
    1: {'main_key': 'level_1'},
    2: {'main_key': 'level_2'},
    3: {'main_key': 'query_id', 'use_hash': True, 'num_div': 10}
}