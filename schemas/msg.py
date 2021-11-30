from pydantic import BaseModel


class Msg(BaseModel):
    """
    Schema for message.
    """
    msg: str
