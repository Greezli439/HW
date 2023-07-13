from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy import Column, Integer, String
from Search_from_mongo import tags_list, author_data, quotes_data

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:12345@localhost/HW_10'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Base = declarative_base()

DBSession = sessionmaker(bind=engine)
session = DBSession()

class Author(Base):

    __tablename__ = 'quotes_author'
    id = Column(Integer, primary_key=True, autoincrement=True)
    fullname = Column(String)
    born_date = Column(String)
    born_location = Column(String)
    description = Column(String)

class Tag(Base):
    __tablename__ = 'quotes_tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    tag_name = Column(String)


class Quote(Base):
    __tablename__ = 'quotes_quote'
    id = Column(Integer, primary_key=True, autoincrement=True)
    quote = Column(String)
    author_id_id = Column(Integer)


class QuoteTags(Base):
    __tablename__ = 'quotes_quote_tags'
    id = Column(Integer, primary_key=True, autoincrement=True)
    quote_id = Column(Integer)
    tag_id = Column(Integer)


def fill_quote_tags(quotes_data):
    for i in quotes_data:
        for j in i['tags']:
            new_record = QuoteTags(quote_id=session.query(Quote.id).select_from(Quote)
                                            .filter(Quote.quote == i['quote']),
                                   tag_id=session.query(Tag.id).select_from(Tag)
                                            .filter(Tag.tag_name == j))
            session.add(new_record)
    session.commit()


def fill_quote(quotes_data, author_data):
    for i in quotes_data:
        for j in author_data:
            if j['id'] == i.author.id:
                new_record = Quote(quote=i.quote,
                                   author_id_id=session.query(Author.id).select_from(Author)
                                   .filter(Author.fullname == j['fullname']))
                session.add(new_record)
    session.commit()


def fill_tag_table(tags_list):
    for i in tags_list:
        new_record = Tag(tag_name=i)
        session.add(new_record)
    session.commit()

def fill_author_table(author_data):
    for i in author_data:
        new_record = Author(
            fullname=i.fullname,
            born_date=i.born_date,
            born_location=i.born_location,
            description=i.description
        )
        session.add(new_record)
    session.commit()

if __name__ == '__main__':
    fill_tag_table(tags_list)
    fill_author_table(author_data)
    fill_quote(quotes_data, author_data)
    fill_quote_tags(quotes_data)


