#基本功能測試
import requests

def lineNotifyMessage(token, arg):

    headers = {
        "Authorization": "Bearer " + token, 
        "Content-Type" : "application/x-www-form-urlencoded"
    }
    if arg == 0:
        payload = {'message': "水銀開關偵測到異動 請訪問此網址了解更多信息:https://youtu.be/_DIon6XMrnA"}
    if arg == 1:
        payload = {'message': "光纖模組偵測到異動 請訪問此網址了解更多信息:https://youtu.be/_DIon6XMrnA"}
    else:
        payload = {'message': "影像偵測模組偵測到異動 請訪問此網址了解更多信息:https://youtu.be/_DIon6XMrnA"}

    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
    return r.status_code

def send(arg):
    lineNotifyMessage('6HGqSkizZ7X99IGHcSxprjEpNIInm53TT0Fe6jm67N1', arg)
if __name__ == "__main__":
  token = '6HGqSkizZ7X99IGHcSxprjEpNIInm53TT0Fe6jm67N1'
  message = '基本功能測試'
  lineNotifyMessage(token, message)
