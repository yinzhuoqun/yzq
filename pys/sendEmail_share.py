#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'yinzhuoqun'

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
import smtplib
import random,os
import base64

#格式化收件人
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


#简单加密解密
def eAd(enORde,str):
    import base64
    """
    ('en',str) : 加码
    ('de',str) : 解码
    """
    if enORde == 'en':
        #加码 'en'
        b_ende = str.encode(encoding="utf-8")
        b_result = base64.b64encode(b_ende)
        # print(b_result)
        return b_result
    else:
        #解码 'de'
        result = base64.b64decode(str)
        b_result = result.decode()
        # print(b_result)
        # base64.b64decode(str).decode()
        return b_result    
    
def message_diy():
    # 文本信息
    m1=u'长的黑，是因为帅炸了，炸了以后，焦了，就黑了。'
    m2=u'不要逼我出手，我疯起来连自己都打。'
    m3=u'你会喜欢我吗？不会我教你啊。'
    m4=u'对方已被太阳热死，无法接收你的消息。'
    m5=u'你的智商和你的胸一样幼稚。'
    m6=u'我就不信，你能顺着网线爬过来打我。'
    message_user_list=[m1,m2,m3,m4,m5,m6]
    message_user = random.choice(message_user_list)

    # diy信息+正式文本信息
    crash_info=u'我就是来打你脸的，打你的脸我不疼。'
    message='=.='+message_user+'=.=\n\n'+crash_info
    return message


msg_header = ""

def send_mail(to_addr,message, msg_header,msg_file_url=False ):
    # 输入邮件地址, 口令和POP3服务器地址:
    
    
    from_addr = 'xxxxx@xxx.com' # 发件人邮箱
    password = b'xxxxxxx' # 密码是 base64 加密后的,请用eAd函数计算出来
    
    print('发件人：%s' % from_addr)
    
    
    # 收件服务器
    # pop3_server = input('POP3 server: ')
    # pop3_server = 'imap.exmail.qq.com'
    # smtp发件服务器
    # smtp_server = 'smtp.exmail.qq.com'
    smtp_server = 'smtp.qq.com'

    # 收件人信息,必须传入list 
    for to_add in to_addr:
        print('收件人：%s'%to_add)

    # 邮件对象
    msg = MIMEMultipart()
    msg['From'] = _format_addr('Monkey 测试 <%s>' % from_addr)  # 发件人信息

    ## msg['To']接收的是字符串而不是list，如果有多个邮件地址，用,分隔即可，+连接。   
    ## 多人收件人信息格式化
    def msg_to(to_add):
        name_info_list = ['公子', '盗帅', '才子', '君子','佳人','闭月','羞花','沉鱼','落雁']
        msg_to_info = name_info_list
        len_add = len(to_add)
        total_add=[]
        for add in to_add:
            to_info = random.choice(msg_to_info)
            msg_to_info.remove(to_info)  # 删除选中的
            m_add='%s<%s>'%(to_info,add)
            f_m_add=_format_addr(m_add)
            total_add.append(f_m_add)
            total_add.append(",")
            print('格式化：%s'%m_add)
        msg_to_info = name_info_list # 重置格式化信息
        total_add.pop()#删除最后一个，
        print('total_add:',total_add)
        total_add_info=''
        for add_info in total_add:
            total_add_info+=add_info
        print('total_add_info:',total_add_info)
        return total_add_info


    msg['To']=msg_to(to_addr)
    msg['Subject'] = Header('来自 Crash 的问候……', 'utf-8').encode()  # 标题 
    msg.attach(MIMEText(message, 'plain', 'utf-8'))  # 邮件正文是MIMEText:
    
    if msg_file_url != False:
    
        ## 添加附件就是加上一个MIMEBase，从本地读取一个图片:
        # 取出路径的目录名和文件名
        #import os
        tuple_path_file = os.path.split(msg_file_url)
        file = tuple_path_file[1]  # 目录名
        # print(file)
        with open(msg_file_url, 'rb') as f:
            # 设置附件的MIME和文件名，这里是png类型:
            mime = MIMEBase('image', 'txt', filename=file)
            # 加上必要的头信息:
            mime.add_header('Content-Disposition', 'attachment', filename=file)
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            # 把附件的内容读进来:
            mime.set_payload(f.read())
            # 用Base64编码:
            encoders.encode_base64(mime)
            # 添加到MIMEMultipart:
            msg.attach(mime)
    # qq普通邮箱发送邮件服务器：smtp.qq.com，使用SSL，端口号587
    # qq企业邮箱 端口号25，SMTP协议默认端口是25
    # server = smtplib.SMTP(smtp_server, 25)  # 服务器、端口
    server = smtplib.SMTP(smtp_server, 587)  # 服务器、端口
    server.starttls() # SSL 支持安全邮件,qq普通邮箱必须要用
    # server.set_debuglevel(1)#打印出和SMTP服务器交互的所有信息
    server.login(from_addr, eAd('de',password)) # 登陆发件人
    try:
        server.sendmail(from_addr, to_addr, msg.as_string())  # 发送try
    except Exception as e:
        print('提示：邮件发送失败（%s）！' % e.value)
    server.quit()
    
if __name__ == '__main__':
     
    # 收件人信息,必须传入list 
    to_addr = ['xxx@xxx.com']
   
    
    send_mail(to_addr,message_diy())  #不带附件
      
    # msg_file_url = r'C:\Users\yzq\Desktop\test.txt' # 附件地址
    # send_mail(to_addr,message_diy(), msg_file_url) # 带附件
