from src.database.models import Contact
from datetime import timedelta, datetime


async def get_contacts(skip, limit, db):
    return db.query(Contact).offset(skip).limit(limit).all()


async def get_contact(contact_id, db):
    return db.query(Contact).filter(Contact.id == contact_id).first()


async def create_contact(body, db):
    contact = Contact(first_name=body.first_name, phone=body.phone,
                      last_name=body.last_name, email=body.email,
                      birthday=body.birthday)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update_contact(contact_id, body, db):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.phone = body.phone
        contact.email = body.email
        contact.birthday = body.birthday
        db.commit()
        db.refresh(contact)
    return contact


async def remove_contact(contact_id, db):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact


async def nearest_birthday(db):
    date_after_week = (today := datetime.today()) + timedelta(days=7)
    contacts = db.query(Contact).filter((Contact.birthday >= today) & (Contact.birthday <= date_after_week)).all()
    return contacts


async def search_contacts(query, db):
    contacts = db.query(Contact).filter((Contact.first_name.like('%{}%'.format(query))) |
                                        (Contact.last_name.like('%{}%'.format(query))) |
                                        (Contact.email.like('%{}%'.format(query)))).all()

    return contacts
