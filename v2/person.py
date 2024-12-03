import uuid
from dataclasses import dataclass
from typing import Optional, List
from v2.bbox import BBox

@dataclass
class Person:
    id: str  
    track_id: Optional[str] = None
    bbox: Optional[BBox] = None  
    embedding_key: Optional[str] = None
    keypoint_key: Optional[str] = None
    age: Optional[int] = None
    sex: Optional[str] = None
    can_be_auth_face : Optional[bool] = None
    
    def __init__(self, track_id: Optional[str] = None, bbox: Optional[BBox] = None,
                 embedding_key: Optional[str] = None, keypoint_key: Optional[str] = None,
                 age: Optional[int] = None, sex: Optional[str] = None):
        self.id = str(uuid.uuid4())  # Generate a unique UUID4 id for each person
        self.track_id = track_id
        self.bbox = bbox
        self.embedding_key = embedding_key
        self.keypoint_key = keypoint_key
        self.age = age
        self.sex = sex