'''
予め自分の環境に mongoengine をインストールすること
$ pip install mongoengine --user
'''

import mongoengine
from mongoengine import connect, disconnect

from mongoengine.document import Document
from mongoengine import fields

######################################
# MongoDB へ格納するために利用するクラス
class TestClass(Document):
    sid = fields.IntField(primary_key=True)
    name = fields.StringField()
    age = fields.IntField()

######################################
# MongoDB アクセスのための情報
MONGO_DB = 'xxxx'
MONGO_HOST = 'xx.xx.xx.xx'
MONGO_USERNAME = 'xxxx'
MONGO_PASSWORD = 'xxxx'

######################################
# MongoDB とのコネクション確立
connect(db=MONGO_DB,
        host=MONGO_HOST, port=27017,
        username=MONGO_USERNAME, password=MONGO_PASSWORD)

# TestClass オブジェクトを生成した結果，
# DB "test" 内に "test_class" というコレクションが自動的に生成される。
'''
tw = TestClass(sid=5, name="MUTO", age=53)
tw.save() # データ登録
'''

# 次々とデータ登録
TestClass(sid=1, name="MUTO", age=53).save()
TestClass(sid=2, name="SUZUKI", age=20).save()
TestClass(sid=3, name="SATO", age=25).save()
TestClass(sid=4, name="TANAKA", age=18).save()

disconnect() # DB とのコネクションを切断

######################################
# MongoDB とのコネクション確立
connect(db=MONGO_DB,
        host=MONGO_HOST, port=27017,
        username=MONGO_USERNAME, password=MONGO_PASSWORD)

# 全データの取り出し
print("=========================")
print("全データの取り出し")
for obj in TestClass.objects.all():
    print(obj.sid, obj.name, obj.age)

# フィルタによる絞り込み(1)
print("=========================")
print("sid が 4 のデータのみ取り出し")
for obj in TestClass.objects(sid=4):
    print(obj.sid, obj.name, obj.age)

# フィルタによる絞り込み(2)
print("=========================")
print("sid が 2 以下のデータのみ取り出し")
for obj in TestClass.objects(sid__lte=2):
    print(obj.sid, obj.name, obj.age)
    
disconnect() # DB とのコネクションを切断
