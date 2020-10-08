import csv
import os
import pandas as pd


#
def search(dirname):
    filenames = os.listdir(dirname)
    itemList = []
    for filename in filenames:
        itemList.append(filename.split(".")[0])

    return itemList


def dataReadAndProcess(itemName):
    # df = pd.read_csv('./Data/'+itemName+'.csv') # 이거면 충분한데 현재 버전 때문에 사용을 못함. save_csv도 마찬가지
    # 따라서 불러와서 pandas.DataFrame으로 저장함
    f = open('./Data/' + itemName + '.csv', 'r', encoding='utf-8')
    rdr = csv.reader(f)
    rawData = []

    for line in rdr:
        rawData.append(line)
    f.close()

    column = ['date', 'open', 'high', 'low', 'close', 'amount', 'tradePrice']
    df = pd.DataFrame.from_records(rawData, columns=column)

    # 데이터 중복 제거
    df = df.drop_duplicates()

    # 데이터 정렬
    df = df.set_index(keys=['date'])
    df = df.sort_index(ascending=False)

    return df.to_records()


# 데이터 저장하는 함수
def saveCsv(itemName, itemValue):
    f = open('./DataOutput/' + itemName + '.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(f)
    for value in itemValue:
        wr.writerow(value)
    f.close()


# 데이터 처리
def dataProcess(itemList):
    dirname = './DataOutput'
    if not os.path.isdir(dirname):
        os.mkdir(dirname)

    # 종목별로 데이터를 읽어들여 데이터 중복제거 및 정렬후 저장
    for item in itemList:
        data = dataReadAndProcess(item)
        saveCsv(item, data)


if __name__ == "__main__":
    dirName = "./Data"
    itemList = search(dirName)
    dataProcess(itemList)

