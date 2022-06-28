#基本功能測試
import requests

def lineNotifyMessage(token, arg):

    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    if arg == 0:
        payload = {'message': "水銀開關偵測到異動"}
    if arg == 1:
        payload = {'message': "光纖模組偵測到異動"}
    else:
        payload = {'message': "影像偵測模組偵測到異動"}

    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

def send(arg):
    lineNotifyMessage('<LINE Notify Key>', arg)
if __name__ == "__main__":
  token = '<LINE Notify Key>'
  message = '基本功能測試'
  lineNotifyMessage(token, message)
