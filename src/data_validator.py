from pydantic import BaseModel 
from typing import Optional

class Artist(BaseModel):

    id : int 
    name : str 


class Track(BaseModel):

    id : int 
    title : str 
    link : Optional[str] = None
    duration : int
    rank : int
    preview : Optional[str] = None
    artist : Artist
    type : str