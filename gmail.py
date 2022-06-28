import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send(arg):
	content = MIMEMultipart()  #建立MIMEMultipart物件
	if arg == 0:
		content["subject"] = "水銀開關偵測到異動"
	if arg == 1:
		content["subject"] = "光纖模組偵測到異動"
	else:
		content["subject"] = "影像偵測模組偵測到異動"

	content["subject"] = "土石流發生【土石流發生】"  #郵件	標題
	content["from"] = "webai404@gmail.com"  #寄件者
	content["to"] = "webai404@gmail.com" #收件者
	with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
    		try:
        		smtp.ehlo()  # 驗證SMTP伺服器
        		smtp.starttls()  # 建立加密傳輸
        		smtp.login("webai404@gmail.com", "mjotxdvfzbbvxmdp")  # 登入寄件者gmail
        		smtp.send_message(content)  # 寄送郵件
        		print("Complete!")
    		except Exception as e:
        		print("Error message: ", e)
