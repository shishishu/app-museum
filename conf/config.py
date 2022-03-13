#!/usr/bin/env python
#coding=utf-8
# @file  : config
# @time  : 2/13/2022 10:42 PM
# @author: shishishu

import os

current_path = os.path.abspath(__file__)
master_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + '..')

data_dir = os.path.join(master_path, 'data')
archive_dir = '/mnt/e/app-museum/data'