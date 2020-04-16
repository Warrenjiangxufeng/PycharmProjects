#coding=utf-8
import unittest
import requests
from HTMLTestRunner import HTMLTestRunner
import time
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

import sys
reload(sys)
sys.setdefaultencoding('utf8')

# ======定义发送邮件========
def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header('接口自动化测试报告', 'utf-8')
    #smtp=smtplib.SMTP_SSL()
    smtp = smtplib.SMTP('reg.163.com')
    #smtp.connect('mail.qq.com', 25)
    smtp.ehlo() #向Gmail发送ehlo命令
    #smtp.starttls()
    smtp.login('warrenjiangxufeng@163.com', 'xy7242807')
    smtp.sendmail('warrenjiangxufeng@163.com', '1647379378@qq.com', msg.as_string())
    smtp.quit()
    print('邮件已发出！注意查收。')


# ======查找测试目录，找到最新生成的测试报告======
def new_report(test_report):
    lists = os.listdir(test_report)
    lists.sort(key=lambda fn: os.path.getmtime(test_report + '/' + fn))
    file_new = os.path.join(test_report, lists[-1])
    print(file_new)
    return file_new


if __name__ == "__main__":
    test_report = "/Users/jiangxufeng1/PycharmProjects/Benlai/testreport"
    sends = new_report(test_report)
    send_mail(sends)
    print 'helleo'
