from mongodb_models import Authors, Quotes
from mongodb_connection import connect

author_data = Authors.objects()
quotes_data = Quotes.objects()


tags_list = set()
for i in quotes_data:
    for j in i.tags:
        tags_list.add(j)
