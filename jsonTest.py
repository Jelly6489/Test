import json
import viewController as vc
# class JsonTest:
def PythonServerResponse(self, itemName, m_date, openPrice, highPrice, lowPrice, currentPrice, volumn, tradingValue):
    self.myViewController = vc.ViewController()
    json_object = {
        "name": itemName,
        "일자": m_date,
        "시가": openPrice,
        "고가": highPrice,
        "저가": lowPrice,
        "현재가": currentPrice,
        "거래량": volumn,
        "거래대금": tradingValue
    }
    json_string = json.dumps(json_object)
    print(json_string)
    # return jsonify(json_object)
