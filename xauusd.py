import re
import requests

headers = { 'Host': 'api.jijinhao.com',
            'Connection': 'keep-alive',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36',
            'Accept': '*/*',
            'Referer': 'http://www.cngold.org/quote/',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9'
            }

# the url of api from jintou website
url = 'https://api.jijinhao.com/sQuoteCenter/realTime.htm?code=JO_92233'

# the url of api sending email
apiurl="http://api.sendcloud.net/apiv2/mail/send"

# api params to send email
params = {"from" : "service@sendcloud.im" }

def getGoldPrice():
    '''
    to get the price of gold
    :return: dict include
    '''
    res = requests.get(url=url, headers=headers)
    raw_data = re.findall(r'"(.*),"',res.text)[0].split(',')
    data = {}
    data['Name'] = raw_data[0]
    data['Last Trade'] = raw_data[3]
    # split price int and float
    data['int'] = raw_data[3][0:4]
    data['float'] = raw_data[3][5:7]
    data['Bid'] = raw_data[36]
    data['Sell'] = raw_data[37]
    data['High Price'] = raw_data[4]
    data['Low Price'] = raw_data[5]
    data['Prev Close'] = raw_data[2]
    data['Open'] = raw_data[38]
    data['Change'] = raw_data[34]
    data['% Chg'] = raw_data[35]
    data['Last Updated'] = raw_data[40] + ' ' + raw_data[41]
    data['time'] = raw_data[41]
    # split time
    data['hour'] = raw_data[41][0:2]
    data['minute'] = raw_data[41][3:5]
    data['second'] = raw_data[41][6:8]
    return data
