from fastapi import HTTPException, status

import crud


def create_author(author_in, db, current_user):
    if current_user.is_superuser:
        return crud.crud_author.create(db=db, obj_in=author_in)
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail='Current user does not have permissions to create author'
    )


def update_author(author_id, author_in, db, current_user):
    if current_user.is_superuser:
        mutable_author = crud.crud_author.get(db=db, id=author_id)
        if not mutable_author:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Author with id={author_id} does not exist in the system'
            )
        if mutable_author.name == author_in.name:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='The author with this name already exists in the system'
            )
        return crud.crud_author.update(db=db, db_obj=mutable_author, obj_in=author_in)
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail='Current user does not have permissions to update author'
    )


def get_author(author_id, db):
    author = crud.crud_author.get(db=db, id=author_id)
    if not author:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=f'Author with id={author_id} does not exist in the system'
        )
    return author


def get_author_list(db, skip, limit):
    author_list = crud.crud_author.get_multi(db=db, skip=skip, limit=limit)
    return author_list


def delete_author(author_id, db, current_user):
    if current_user.is_superuser:
        author = crud.crud_author.get(db=db, id=author_id)
        if not author:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'Author with id={author_id} does not exist in the system'
            )
        return crud.crud_author.remove(db=db, id=author_id)
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail='Current user does not have permissions to delete author'
    )
