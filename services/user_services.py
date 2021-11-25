from fastapi import HTTPException, status

import crud


def check_exists_user_name(user_name, db):
    if crud.crud_user.get_by_name(name=user_name, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='The user with this username already exists in the system'
        )


def check_exists_user_email(user_email, db):
    if crud.crud_user.get_by_email(email=user_email, db=db):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='The user with this email already exists in the system'
        )


def create_user(user_in, db):
    check_exists_user_name(user_name=user_in.name, db=db)
    check_exists_user_email(user_email=user_in.email, db=db)
    return crud.crud_user.create(db=db, obj_in=user_in)


def update_user(db, current_user, user_in, user_id):
    if current_user.id == user_id or current_user.is_superuser:
        mutable_user = crud.crud_user.get(db=db, id=user_id)
        if not mutable_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'User with id={user_id} does not exist in the system'
            )
        if mutable_user.name != user_in.name:
            check_exists_user_name(user_name=user_in.name, db=db)
        if mutable_user.email != user_in.email:
            check_exists_user_email(user_email=user_in.email, db=db)
        if not mutable_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail='The user with this username does not exist in the system'
            )
        return crud.crud_user.update(db=db, db_obj=mutable_user, obj_in=user_in)
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail='Current user does not have permissions to change this object'
    )


def get_user(user_id, db, current_user):
    user = crud.crud_user.get(db=db, id=user_id)
    if user and (current_user.id == user_id or current_user.is_superuser):
        return user
    elif not user and current_user.is_superuser:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f'User with id={user_id} does not exist in the system'
        )
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=f'Current user does not have permission to retrieve user with id={user_id}'
    )


def get_user_list(limit, skip, db, current_user):
    if current_user.is_superuser:
        return crud.crud_user.get_multi(db=db, skip=skip, limit=limit)
    user_list = list()
    return user_list.append(current_user)


def delete_user(user_id, db, current_user):
    if current_user.id == user_id or current_user.is_superuser:
        user = crud.crud_user.get(db=db, id=user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f'User with id={user_id} does not exist in the system'
            )
        return crud.crud_user.remove(db=db, id=user_id)
    raise HTTPException(
        status_code=status.HTTP_403_FORBIDDEN,
        detail=f'Current user does not have permission to remove user with id={user_id}'
    )
