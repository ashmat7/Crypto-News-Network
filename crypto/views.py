from django.shortcuts import render
def home(request):
    import requests
    import json
    #grab crypto price data
    price_request=requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,XRP,ETH,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD,EUR")
    price=json.loads(price_request.content)

    #grab crypto news here
    api_request=requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api=json.loads(api_request.content)
    for i in api['Data']:
        if(len(i['body'])>25):
            i['body']=i['body'][:35]+"..."
    return render(request,'home.html',{'api':api,'price':price})