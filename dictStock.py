import requests

# host = 'localhost:8080'
# path = '/member/changeAppId'
# payload = {'UserId' : userId }
# r = requests.get('localhost:8080/member/changeAppId', params=payload)

# import requests
# import json
#
# # GET
# res = requests.get('http://localhost:8080/member/changeAppId')
# print(str(res.status_code) + " | " + res.text)
#
# # POST (JSON)
# headers = {'Content-Type': 'application/json; chearset=utf-8'}
# payload = {'UserId' : 'userId' }
# res = requests.post('http://localhost:8080/member/changeAppId', payload=json.dumps(payload), headers=headers)
# print(str(res.status_code) + " | " + res.text)

#
# class DictStock:
#     @app.route('/history/buy')
#     def PythonServerResponse(self, itemName, m_date, openPrice, highPrice, lowPrice, currentPrice, volumn, tradingValue):
#         print("It's operate")
#         # self.myViewController = vc.ViewController()
#         json_object = {
#             "name": itemName,
#             "일자": m_date,
#             "시가": openPrice,
#             "고가": highPrice,
#             "저가": lowPrice,
#             "현재가": currentPrice,
#             "거래량": volumn,
#             "거래대금": tradingValue
#         }
#         json_string = json.dumps(json_object)
#         print(json_string)
#         # return jsonify(json_object)
#
#     app.run()
# # # data = {
# # #     # 'itemName' : itemName,
# # #     'date' : m_date,
# # #     'openPrice' : openPrice
# # # }
# # # json_data = json.dumps(data)
# # # print(json_data)
# #
# #
# # # import json
# # #
# # # json_object = {
# # #     "id": 1,
# # #     "username": "Bret",
# # #     "email": "Sincere@april.biz",
# # #     "address": {
# # #         "street": "Kulas Light",
# # #         "suite": "Apt. 556",
# # #         "city": "Gwenborough",
# # #         "zipcode": "92998-3874"
# # #     },
# # #     "admin": False,
# # #     "hobbies": None
# # # }
# # #
# # # json_string = json.dumps(json_object)
# # # print(json_string)
