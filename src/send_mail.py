# config:utf-8

import smtplib
from email.mime.text import MIMEText
import datetime

jp="iso-2022-jp"
message=MIMEText("メール送信テスト".encode(jp),"plain",jp,)
from_address="test@aaa.bb"
to_address="nao.zima@gmail.com"

message["Subject"]="件名"
message["From"]=from_address
message["To"]=to_address


server=smtplib.SMTP('localhost')
server.send_message(message)
