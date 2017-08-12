import urllib.request
import time #시간함수 사용
import math
from urllib.request import Request, urlopen
import json
import os
def strtofor(x):
    return format(round(float(x)),",")
print("1.비트코인\n2.이더리움\n3.대시\n4.라이트\n5.이더리움클래식\n6.리플\n7.비트코인캐쉬\n\n")
yourcoin = int(input('가지고 계신 코인 번호를 입력해주세요(숫자만):'))
os.system('cls')
count = input('코인 수량을 입력해주세요(소수점6자리까지):')
ccount = float(count)
star = "□" * 20
while True:
    bithumb = urllib.request.urlopen('https://api.bithumb.com/public/ticker/all')  #빗썸 api

    outputtime = time.localtime()  # 내장 함수사용
    current_time = "%04d_%02d_%02d %02d:%02d:%02d" % (outputtime.tm_year, outputtime.tm_mon, outputtime.tm_mday, outputtime.tm_hour, outputtime.tm_min, outputtime.tm_sec)
    #사이트에서 정보 받아온 시간(년-월-일-시-분-초)

    readprice = bithumb.read() #받아온 정보 파이썬 타입으로 변경
    savejson = json.loads(readprice) #json을 딕셔너리 형태로 변환

#closingprice =종가(현제가라 보면 되려나) 가상화폐별로 변수에 저장

# 종가(현제 가격 부분 수집)
    #+세자리수로 변환
    BTC = savejson["data"]["BTC"]["closing_price"] #빝코
    ETH = savejson["data"]["ETH"]["closing_price"]#이더
    DASH = savejson["data"]["DASH"]["closing_price"] #대시
    LTC = savejson["data"]["LTC"]["closing_price"] #라이트
    ETC = savejson["data"]["ETC"]["closing_price"] #이더클
    XRP = savejson["data"]["XRP"]["closing_price"] #리플
    BCH = savejson["data"]["BCH"]["closing_price"] #비트코인캐시

    #보유 코인 환산부분
    if (yourcoin == 1):
        ccount = format(int(ccount * float(BTC)),',')
        kd = "비트코인"
    if (yourcoin == 2):
        ccount = format(int(ccount * float(ETH)), ',')
        kd = "이더리움"
    if (yourcoin == 3):
        ccount = format(int(ccount * float(DASH)), ',')
        kd = "대시 코인"
    if (yourcoin == 4):
        ccount = format(int(ccount * float(LTC)), ',')
        kd = "라이트 코인"
    if (yourcoin == 5):
        ccount = format(int(ccount * float(ETC)),',')
        kd = "이더리움 클래식"
    if (yourcoin == 6):
        ccount = format(int(ccount * float(XRP)),',')
        kd = "리플코인"
    if (yourcoin == 7):
        ccount = format(int(ccount * float(BCH)),',')
        kd = "비트코인 캐쉬"


    os.system('cls')
    anothertime = time.localtime()
    a_time = "%02d:%02d:%02d" % (anothertime.tm_hour, anothertime.tm_min, anothertime.tm_sec)

    print("  §가상화폐시세알리미(빗썸)Ver0.1§ \n  ※시세 불러온 시각:", current_time)
    print("  ※화면 출력 시각:",a_time,"\n\n")
    print("▣", star, "▣\n\n\n  [보유한",kd,"의 가격]", ccount, "원\n\n\n▣",star,"▣\n\n")
    ccount = float(count)
    print("    ▣비트코인(BTC)▣", strtofor(BTC),"""원\n
    ▣이더리움(ETH)▣""", strtofor(ETH),"""원\n
    ▣대시(DASH)▣""", strtofor(DASH), """원\n
    ▣이더리움 클래식(ETC)▣""", strtofor(ETC),"""원\n
    ▣라이트코인(Lite)▣""", strtofor(LTC),"""원\n
    ▣리플코인(XRP)▣""", strtofor(XRP), """원\n
    ▣비트코인캐쉬(BCH)▣""", strtofor(BCH), """원\n\n
    거래소 정보(www.bithumb.com)★made by 예서""")
    time.sleep(0.1)
    
