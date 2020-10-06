class DataModel:
    def __init__(self):
        print("Data Model")
        myLoginInfo = None

    class LoginInfo:
        def __init__(self, accCnt, accList, userId, userName, keyBSEC, firew, serverGubun):
           self.accCnt = accCnt
           self.accList = accList
           self.userid = userId
           self.userName = userName
           self.keyBSEC = keyBSEC
           self.firew = firew
           self.serverGubun = serverGubun

        def getServerGubun(self):
            if self.serverGubun == "1":
                return "모의 투자"
            else:
                return "실 서버"

           # print("userName: " + str(userName))
