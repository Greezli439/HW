from mongoengine import connect
from models_mongo import Authors, Quotes

connect(host='mongodb+srv://greezlistuding:UB1VnEMbXIJSxHph@cluster0.1iemlfa.mongodb.net/?retryWrites=true&w=majority')


# data = Quotes.objects()
data1 = Authors.objects(fullname='Albert Einstein')
print( data1)
