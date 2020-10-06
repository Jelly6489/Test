import dataModel as dm

#pyqt
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QAxContainer import *
from PyQt5.QtGui import *

form_class = uic.loadUiType("main_windows.ui")[0]

class ViewController(QMainWindow, form_class):
    def __init__(self, my_model):
        super().__init__()
        self.setUI()
        self.myModel = my_model
        print("View Controller")

        # kiwoom Open API 초기화
        self.kiwoom = QAxWidget("KHOPENAPI.KHOpenAPICtrl.1")
        self.login()

        # kiwoom Open API event Trigger
        self.kiwoom.OnEventConnect.connect(self.event_connect)

    def login(self):
        self.kiwoom.dynamicCall("CommConnect()")

    def get_login_info(self):
        accCnt = self.kiwoom.dynamicCall("GetLoginInfo(QString)", "ACCOUNT_CNT")
        accList = self.kiwoom.dynamicCall("GetLoginInfo(QString)", "ACCLIST")
        userId = self.kiwoom.dynamicCall("GetLoginInfo(QString)", "USER_ID")
        userName = self.kiwoom.dynamicCall("GetLoginInfo(QString)", "USER_NAME")
        keyBSEC = self.kiwoom.dynamicCall("GetLoginInfo(QString)", "KEY_BSECGB")
        firew = self.kiwoom.dynamicCall("GetLoginInfo(QString)", "FIREW_SECGB")
        serverGubun = self.kiwoom.dynamicCall("GetLoginInfo(QString)", "GetServerGubun")

        self.myModel.myLoginInfo = dm.DataModel.LoginInfo(accCnt, accList, userId, userName, keyBSEC, firew, serverGubun)

        self.statusbar.showMessage(self.myModel.myLoginInfo.getServerGubun())

        print("나의 이름: " + str(self.myModel.myLoginInfo.userName))
        print("나의 ID: " + str(self.myModel.myLoginInfo.userId))
        print("나의 계좌: " + str(self.myModel.myLoginInfo.accList.rstrip(';')))

    def event_connect(self, nErrCode):
        if nErrCode == 0:
            self.label.setText("로그인 성공")
            self.get_login_info()
        elif nErrCode == 100:
            print("사용자 정보 교환 실패")
        elif nErrCode == 101:
            print("서버 접속 실패")
        elif nErrCode == 102:
            print("버전 처리 실패")

    def setUI(self):
        self.setupUi(self)