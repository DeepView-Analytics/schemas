import uuid
from pydantic import BaseModel
from typing import Optional
from v2.bbox import BBox

class Person(BaseModel):
    id: str  
    track_id: Optional[str] = None
    bbox: Optional[BBox] = None  
    embedding_key: Optional[str] = None
    keypoint_key: Optional[str] = None
    age: Optional[int] = None
    sex: Optional[str] = None
    can_be_auth_face: Optional[bool] = None
    
    def __init__(self, **data):
        super().__init__(id=str(uuid.uuid4()), **data)
    
