from src.database.models import Contact
from datetime import timedelta, datetime
from src.database.models import User, Contact
from sqlalchemy import and_


async def get_contacts(skip, limit, user: User, db):
    return db.query(Contact).filter(Contact.user_id == user.id).offset(skip).limit(limit).all()


async def get_contact(contact_id, user: User, db):
    return db.query(Contact).filter(and_(Contact.id == contact_id,
                                         Contact.user_id == user.id)).first()


async def create_contact(body, user: User, db):
    print(user.id)
    contact = Contact(first_name=body.first_name, phone=body.phone,
                      last_name=body.last_name, email=body.email,
                      birthday=body.birthday, user_id=str(user.id))
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(contact_id, body, user: User, db):
    contact = db.query(Contact).filter(and_(Contact.id == contact_id,
                                            Contact.user_id == user.id)).first()
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.phone = body.phone
        contact.email = body.email
        contact.birthday = body.birthday
        db.commit()
        db.refresh(contact)
    return contact


async def remove_contact(contact_id, user: User, db):
    contact = db.query(Contact).filter(and_(Contact.id == contact_id,
                                            Contact.user_id == user.id)).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def nearest_birthday(db, user: User):
    date_after_week = (today := datetime.today()) + timedelta(days=7)
    contacts = db.query(Contact)\
        .filter(and_(Contact.birthday >= today, Contact.user_id == user.id,
                     Contact.birthday <= date_after_week)).all()
    return contacts


async def search_contacts(query, user: User, db):
    contacts = db.query(Contact).filter(and_(Contact.first_name.like('%{}%'.format(query)),
                                             Contact.last_name.like('%{}%'.format(query)),
                                             Contact.email.like('%{}%'.format(query)),
                                             Contact.user_id == user.id)).all()
    return contacts
