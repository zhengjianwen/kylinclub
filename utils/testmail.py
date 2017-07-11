# coding:utf8
'''
日报
'''
'''
import email
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class MyEmail:
    def __init__(self):
        self.user = 'member@kylinclub.org'
        self.passwd = 'wuchao8510290'
        self.smtp = "smtp.exmail.qq.com"
    def send(self):
        try:
            print('开始发邮件')
            server = smtplib.SMTP_SSL(self.smtp, port=465)
            server.login(self.user, self.passwd)
            server.sendmail("<574601624>" % self.user,'574601624@qq.com','python for me hairui')
            server.close()
            print("send email successful")
        except Exception as  e:
            print("send email failed %s" % e)

if __name__ == "__main__":
    my = MyEmail()
    my.send()
'''
'''
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr

# 发送邮件

from_addr = 'member@kylinclub.org'
mail_account = 'smtp.exmail.qq.com'
mail_password = 'wuchao8510290'
to_addr = ['574601624@qq.com', '574601624@qq.com']
mail_Subject = '速运业务线2015上线计划内容'
msg_content = 'The msg Content'

msg = MIMEText(msg_content, 'html', 'utf-8')
msg['From'] = '自营QA上线计划 <%s>'
msg['To'] = '574601624@qq.com'
msg['Subject'] = '速运业务线2015上线计划内容'

smtp_server = 'smtp.exmail.qq.com'
smtp_port = 465
server = smtplib.SMTP_SSL(smtp_server, smtp_port)
server.set_debuglevel(1)
#server.starttls()
server.login(mail_account, mail_password)
server.sendmail(from_addr, to_addr, msg.as_string())
server.quit()
'''
# coding:utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host = "smtp.qq.com"  # 设置服务器
mail_user = "574601624@qq.com"  # 用户名
mail_pass = ""  # 口令,QQ邮箱是输入授权码，在qq邮箱设置 里用验证过的手机发送短信获得，不含空格

sender = 'member@kylinclub.org'
receivers = ['574601624@qq.com', 'hairui@qq.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('a test for python', 'plain', 'utf-8')
message['From'] = Header("ppyy", 'utf-8')
message['To'] = Header("you", 'utf-8')

subject = 'my test'
message['Subject'] = Header(subject, 'utf-8')

try:
    smtpObj = smtplib.SMTP_SSL(mail_host, 465)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    smtpObj.quit()
    print("邮件发送成功")
except smtplib.SMTPException as e:
    print(e)