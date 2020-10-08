# import pymysql
# class MysqlController:
#     db = pymysql.connect(host='localhost', port=3306, user='blackTensorStock',
#                            passwd='456123', db='blacktensorstock')
#
#     cursor = db.cursor()
#
#     sql = """
#         create table pydbtest(
#             id int unsigned not null auto_increment,
#             name varchar(20) not null,
#             price int not null,
#             primary key(id)
#         )
#     """
#     cursor.execute(sql)
#
#     db.commit()
#
#     db.close()
#
#     print("Table Creation Success")