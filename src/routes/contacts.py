"""
Module with apps routes.
"""

from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from fastapi_limiter.depends import RateLimiter
from src.database.db import get_db
from src.schemas import ContactBase, ContactDB
from src.repository import contacts as repository_contacts
from src.database.models import User
from src.services.auth import auth_service


router = APIRouter(prefix='/contacts', tags=["contacts"])


@router.get("/", response_model=List[ContactDB], description='No more than 5 requests per minute',
            dependencies=[Depends(RateLimiter(times=5, seconds=60))])
async def read_contacts(skip: int = 0, limit: int = 100,
                        current_user: User = Depends(auth_service.get_current_user),
                        db: Session = Depends(get_db)):
    """
    Function for getting contacts from db.

    :param skip: count records for skip.
    :type skip: int
    :param limit: count records for getting.
    :type limit: int
    :param current_user: User.
    :type current_user: UserDb
    :param db: db session.
    :type db: Session
    :return: list contacts.
    :rtype: ContactDB
    """
    contacts = await repository_contacts.get_contacts(skip, limit, current_user, db)
    return contacts


@router.post("/", response_model=ContactDB, status_code=status.HTTP_201_CREATED,
             description='No more than 3 requests per minute',
             dependencies=[Depends(RateLimiter(times=3, seconds=60))])
async def create_contact(body: ContactBase, current_user: User = Depends(auth_service.get_current_user),
                         db: Session = Depends(get_db)):
    """
    Adding new records to Contacts.

    :param body: New contact.
    :type body: ContactBase
    :param current_user: User.
    :type current_user: UserDb
    :param db: db session.
    :type db: Session
    :return: Added contact.
    :rtype: ContactDB
    """
    return await repository_contacts.create_contact(body, current_user, db)


@router.get("/nearestbirthday/", response_model=list[ContactDB], description='No more than 1 requests per minute',
            dependencies=[Depends(RateLimiter(times=1, seconds=60))])
async def nearest_birthday(db: Session = Depends(get_db), current_user: User = Depends(auth_service.get_current_user)):
    """
    Search contacts with birthday on next week.

    :param db: db session.
    :type db: Session
    :param current_user: User.
    :type current_user: UserDb
    :return: list contacts.
    :rtype: ContactDB
    """
    contacts = await repository_contacts.nearest_birthday(db, current_user)
    return contacts


@router.get("/search/{data}", response_model=list[ContactDB])
async def search_contacts(data: str, current_user: User = Depends(auth_service.get_current_user),
                          db: Session = Depends(get_db)):
    """
    Search contact with name or email.

    :param data: Search data.
    :type data: str
    :param current_user: User.
    :type current_user: UserDb
    :param db: db session.
    :type db: session
    :return: list contacts.
    :rtype: ContactDB
    """
    contacts = await repository_contacts.search_contacts(data, current_user, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contacts


@router.get("/{contact_id}/", response_model=ContactDB, description='No more than 10 requests per minute',
            dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def read_contact(contact_id: int, current_user: User = Depends(auth_service.get_current_user),
                       db: Session = Depends(get_db)):
    """
    Search contact for id.

    :param contact_id: Search data.
    :type contact_id:  int
    :param current_user: User.
    :type current_user: UserDb
    :param db: db session.
    :type db: Session
    :return: list contacts.
    :rtype: ContactDB
    """
    contacts = await repository_contacts.get_contact(contact_id, current_user, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contacts


@router.delete("/{contact_id}/", response_model=ContactDB)
async def remove_contact(contact_id: int, current_user: User = Depends(auth_service.get_current_user),
                         db: Session = Depends(get_db)):
    """

    :param contact_id: Contacts id for removing.
    :type contact_id: int
    :param current_user: User
    :type current_user: UserDb
    :param db: db connection.
    :type db: Session
    :return: Contact
    :rtype: ContactDB
    """
    contacts = await repository_contacts.remove_contact(contact_id, current_user, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contacts


@router.put("/{contact_id}/", response_model=ContactDB, status_code=status.HTTP_201_CREATED,
            description='No more than 10 requests per minute',
            dependencies=[Depends(RateLimiter(times=10, seconds=60))])
async def update_contact(body: ContactBase, contact_id: int,
                         current_user: User = Depends(auth_service.get_current_user),
                         db: Session = Depends(get_db)):
    """
    Refresh contacts data.

    :param body: New contacts data.
    :type body: ContactBase
    :param contact_id: Contacts id.
    :type contact_id: int
    :param current_user: User.
    :type current_user: UserDb
    :param db: db connection.
    :type db: Session
    :return: contacts.
    :rtype: ContactDB
    """
    contacts = await repository_contacts.update_contact(contact_id, body, current_user, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contacts
