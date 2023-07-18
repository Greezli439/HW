"""
A set of functions for user administration.
"""
from libgravatar import Gravatar
from sqlalchemy.orm import Session

from src.database.models import User
from src.schemas import UserModel


async def get_user_by_email(email: str, db: Session) -> User:
    """
    Search User by email in db.

    :param email: Users email.
    :type email: str
    :param db: db session.
    :type db: Session
    :return: User.
    :rtype: UserModel
    """
    res = db.query(User).filter(User.email == email).first()
    return res


async def create_user(body: UserModel, db: Session) -> User:
    """

    :param body: New User.
    :type body: UserModel
    :param db: db session.
    :type db: Session
    :return: User.
    :rtype: UserModel
    """
    avatar = None
    try:
        g = Gravatar(body.email)
        avatar = g.get_image()
    except Exception as e:
        print(e)
    new_user = User(**body.dict(), avatar=avatar)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def update_token(user: User, token: str | None, db: Session) -> None:
    """
    Update refresh token in db.

    :param user: User.
    :type user: UserModel
    :param token: old token.
    :type token: str
    :param db: db session.
    :type db: Session
    :return: None
    :rtype: None
    """
    user.refresh_token = token
    db.commit()


async def confirmed_email(email: str, db: Session) -> None:
    """
    Change confirmed tag in db to True.

    :param email: Users email.
    :type email: str
    :param db: db session.
    :type db: Session
    :return: None.
    """
    user = await get_user_by_email(email, db)
    user.confirmed = True
    db.commit()


async def update_avatar(email, url: str, db: Session) -> User:
    """
    Set or change users avatar.

    :param email: Users email.
    :type email: str
    :param db: db session.
    :type db: Session
    :param url: URL to image on cloudinary.
    :type url: str
    :return: User.
    :rtype: UserModel
    """
    user = await get_user_by_email(email, db)
    user.avatar = url
    db.commit()
    return user
