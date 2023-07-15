from typing import List

from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas import ContactBase, ContactDB
from src.repository import contacts as repository_contacts
from src.database.models import User
from src.services.auth import auth_service


router = APIRouter(prefix='/contacts', tags=["contacts"])


@router.get("/", response_model=List[ContactDB])
async def read_contacts(skip: int = 0, limit: int = 100,
                        current_user: User = Depends(auth_service.get_current_user),
                        db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_contacts(skip, limit, current_user, db)
    return contacts


@router.post("/", response_model=ContactDB, status_code=status.HTTP_201_CREATED)
async def create_contact(body: ContactBase, current_user: User = Depends(auth_service.get_current_user),
                         db: Session = Depends(get_db)):
    return await repository_contacts.create_contact(body, current_user, db)


@router.get("/nearestbirthday/", response_model=list[ContactDB])
async def nearest_birthday(db: Session = Depends(get_db), current_user: User = Depends(auth_service.get_current_user)):
    contacts = await repository_contacts.nearest_birthday(db, current_user)
    return contacts


@router.get("/search/{data}", response_model=list[ContactDB])
async def search_contacts(data: str, current_user: User = Depends(auth_service.get_current_user), db: Session = Depends(get_db)):
    contacts = await repository_contacts.search_contacts(data, current_user, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contacts


@router.get("/{contact_id}/", response_model=ContactDB)
async def read_contact(contact_id: int, current_user: User = Depends(auth_service.get_current_user), db: Session = Depends(get_db)):
    contacts = await repository_contacts.get_contact(contact_id, current_user, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contacts


@router.delete("/{contact_id}/", response_model=ContactDB)
async def remove_contact(contact_id: int, current_user: User = Depends(auth_service.get_current_user),
                         db: Session = Depends(get_db)):
    contacts = await repository_contacts.remove_contact(contact_id, current_user, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contacts


@router.put("/{contact_id}/", response_model=ContactDB, status_code=status.HTTP_201_CREATED)
async def update_contact(body: ContactBase, contact_id: int,
                         current_user: User = Depends(auth_service.get_current_user),
                         db: Session = Depends(get_db)):
    contacts = await repository_contacts.update_contact(contact_id, body, current_user, db)
    if contacts is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Contact not found")
    return contacts
