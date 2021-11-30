from typing import Optional, List

from sqlalchemy.orm import Session

import crud
import models
import schemas


def create_author(
        author_in: schemas.AuthorCreateUpdateSchema,
        db: Session,
        current_user: models.User
) -> models.Author:
    """
    Create an author.
    """
    crud.crud_user.allow_or_403(current_user)
    crud.crud_author.pass_author_name_or_400(
        new_author_name=author_in.name,
        db=db
    )
    return crud.crud_author.create(db=db, obj_in=author_in)


def update_author(
        author_id: int,
        author_in: schemas.AuthorCreateUpdateSchema,
        db: Session,
        current_user: models.User
) -> models.Author:
    """
    Update an author.
    """
    crud.crud_user.allow_or_403(current_user)
    mutable_author = crud.crud_author.get_or_404(db=db, id=author_id)
    crud.crud_author.pass_author_name_or_400(
        db_author=mutable_author,
        new_author_name=author_in.name,
        db=db
    )
    return crud.crud_author.update(db=db, db_obj=mutable_author, obj_in=author_in)


def get_author(author_id: int, db: Session) -> Optional[models.Author]:
    """
    Get author by id.
    """
    return crud.crud_author.get_or_404(db=db, id=author_id)


def get_author_list(db: Session, skip: int, limit: int) -> List[models.Author]:
    """
    Get list of authors.
    """
    author_list = crud.crud_author.get_multi(db=db, skip=skip, limit=limit)
    return author_list


def delete_author(
        author_id: int,
        db: Session,
        current_user: models.User
) -> models.Author:
    """
    Delete an author.
    """
    crud.crud_user.allow_or_403(current_user)
    crud.crud_author.get_or_404(db=db, id=author_id)
    return crud.crud_author.remove(db=db, id=author_id)

