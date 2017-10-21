#!/usr/bin/env python
# coding: utf-8

import datetime
import json
import os
import sys
import time

from Waveshare_43inch_ePaper import *

screen_width = 800
screen_height = 600
screen = Screen('/dev/ttyAMA0')
screen.connect()
screen.handshake()

screen.clear()
screen.set_memory(MEM_FLASH)
screen.set_rotation(ROTATION_NORMAL)

def tongji_fail(msg):
    screen.text(10,170, msg)
    screen.update()
    screen.disconnect()
    sys.exit(1)

tongji_data_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'statistics.json',)
#tongji_data_file = codecs.open(statistics.json, encoding='utf-8')
tdata_uv = {}
try:
    with open(tongji_data_file, 'r') as in_file:
        tdata = json.load(in_file)
except IOError:
    tongji_fail(u'ERROR:无法加载统计数据!')
    
tdata_uv = str(tdata['body']['data'][0]['result']['items'][1][0][1]).decode("utf-8")
tdata_pv = str(tdata['body']['data'][0]['result']['items'][1][0][0]).decode("utf-8")

ydata_pv = str(tdata['body']['data'][0]['result']['items'][1][1][0]).decode("utf-8")
ydata_uv = str(tdata['body']['data'][0]['result']['items'][1][1][1]).decode("utf-8")


screen.set_ch_font_size(FONT_SIZE_32)
screen.set_en_font_size(FONT_SIZE_32)

#文本显示位置
tongji_x = 540
tongji_y = 270

screen.text(tongji_x,tongji_y - 42,u'-博客访问统计-')
screen.text(tongji_x,tongji_y,u'今日PV')
screen.text(tongji_x + 100,tongji_y,tdata_pv)

screen.text(tongji_x + 100 + 63,tongji_y,u'UV')
screen.text(tongji_x + 100 + 100,tongji_y,tdata_uv)

screen.text(tongji_x,tongji_y + 42,u'昨日PV')
screen.text(tongji_x + 100,tongji_y + 42,ydata_pv)

screen.text(tongji_x + 100 + 63,tongji_y + 42,u'UV')
screen.text(tongji_x + 100 +100,tongji_y + 42,ydata_uv)

screen.update()
screen.disconnect()
sys.exit(1)
