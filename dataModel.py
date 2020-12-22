from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTime
from PyQt5.QtCore import *

class DataModel:
    def __init__(self):
        print("Data Model")
        self.myLoginInfo = None
        self.itemList = []

    class LoginInfo:
        def __init__(self, accCnt, accList, userId, userName, keyBSEC, firew, serverGubun):
           self.accCnt = accCnt
           self.accList = accList
           self.userId = userId
           self.userName = userName
           self.keyBSEC = keyBSEC
           self.firew = firew
           self.serverGubun = serverGubun

        def getServerGubun(self):
            if self.serverGubun == "1":
                return "<<모의 투자>> "
            else:
                return "<<실 서버>> "

        # ##### 상태표시줄에 들어갈 현재시간
        # def timeout(self):
        #     current_time = QTime.currentTime()             # 현재시간 구함
        #     text_time = current_time.toString("hh:mm:ss")  # 현재시간을 "hh:mm:ss"형식으로 변경
        #     time_msg = "현재시간 : " + text_time            # 표출할 메세지
        #
        #     self.statusbar.showMessage("서버 연결 중 | " + time_msg)  # 상태바에 표출


    class ItemInfo:
        def __init__(self, itemCode, itemName):
            self.itemCode = itemCode
            self.itemName = itemName

           # print("userName: " + str(userName))
##

    class StockTrdata:
        def __init__(self, stockName, stockCode, closingMonth, parValue,
                  capital, listedStock, creditRatio, bestYear, lowYear, marketValue, per, eps, roe, pbr, bps, take,
                  operatProfit, netIncome, openPrice, highPrice, upperPrice, lowerPrice, standardPrice, currentPrice,
                     changeSymbol, netChange, fluctuation, volume, tradePrepare):
            self.stockName = stockName
            self.stockCode = stockCode
            self.closingMonth = closingMonth
            self.parValue = parValue
            self.currentPrice = currentPrice
            self.capital = capital
            self.listedStock = listedStock
            self.creditRatio = creditRatio
            self.bestYear = bestYear
            self.lowYear = lowYear
            self.marketValue = marketValue
            self.per = per
            self.eps = eps
            self.roe = roe
            self.pbr = pbr
            self.bps = bps
            self.take = take
            self.operatProfit = operatProfit
            self.netIncome = netIncome
            self.openPrice = openPrice
            self.highPrice = highPrice
            self.upperPrice = upperPrice
            self.lowerPrice = lowerPrice
            self.standardPrice = standardPrice
            self.currentPrice = currentPrice
            self.changeSymbol = changeSymbol
            self.netChange = netChange
            self.fluctuation = fluctuation
            self.volume = volume
            self.tradePrepare = tradePrepare

