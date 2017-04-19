#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

import urllib.request
import requests
import os, time, sys, re
from tqdm import tqdm  # 进度条模块


# 读取网页
def getHtml(url):
    headers = {
        'Referer': 'http://www.qiushibaike.com/pic/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0'
    }
    page = urllib.request.build_opener()
    page.addheaders = [headers]
    html = page.open(url).read()

    return html


# 获取图片地址
def getImg(html):
    reg = r'<img src="(.+?.jpg)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html);  # print(imglist)

    return imglist


# 显示下载进度
def download(num, block, total):
    '''回调函数 单位byte
    @num-blocknum: 已经下载的数据块
    @block-blocksize: 数据块的大小
    @total-totalsize: 远程文件的大小
    '''
    per = 100.0 * num * block / total
    if per > 100:
        per = 100
    if num * block > total:
        a = total
    else:
        a = num * block

    if total < 1024 * 1024:
        sys.stdout.write('%.2f/%.2f(KB)  %.2f%%\r' % (a / 1024, total / 1024, per))
        print('')  # 防止下载文件太小，看不到下载进度

    else:
        sys.stdout.write('%.2f/%.2f(MB)  %.2f%%\r' % (a / 1024 / 1024, total / 1024 / 1024, per))
    sys.stdout.flush()


# 获取文件
def get_file(url):
    html = getHtml(url)
    try:
        html = html.decode('UTF-8')
    except Exception as e:
        html = html.decode('gbk')

    imglist = getImg(html)

    dirname = 'img_spider'
    path = os.path.join(os.getcwd(), dirname)

    if os.path.exists(path) != True:
        os.mkdir(dirname)
        print('文件夹：%s 创建成功\n路  径：%s' % (dirname, path))
    else:
        print('文件夹：%s 已经存在\n路  径：%s' % (dirname, path))
    os.chdir(path)  # 切换到图片保存路径

    imglist = ['http://mm.howkuai.com/wp-content/uploads/2017a/01/01/11.jpg']  # test
    
    n = 1
    for imgurl in imglist[:3]:
        t = time.strftime("%m-%d_%H-%M-%S")
        filename = '%s_%s.png' % (t, n)
        print("文件地址：%s\n文件名称：%s" % (imgurl, filename))
        # try:
            # urllib.request.urlretrieve(imgurl, filename, download)  # method first
        req = requests.get(imgurl, stream=True, headers={'User-agent': 'Mozilla/5.0'})
        with open(filename, 'wb') as pbar:
            # pbar.write(req.content)
            for data in tqdm(req.iter_content()): # tqdm 括号内是迭代器
                pbar.write(data)
                # time.sleep(0.001) # test

        n += 1
        # except Exception as e:
        #     print('提示：当前文件下载失败')

    print('\n保存文件：%s 张' % (n - 1))
    print('保存目录：%s' % path)
    # 窗口关闭时间
    window_close_time = 5
    print('>>> 脚本 %s s后自动关闭' % window_close_time)
    time.sleep(window_close_time)


if __name__ == '__main__':
    url = 'http://www.qiushibaike.com/pic/'
    get_file(url)
