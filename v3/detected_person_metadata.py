from dataclasses import dataclass, field
from typing import Optional
import uuid
from pydantic import BaseModel
from v3.bbox import BBox

@dataclass
class DetectionMetadata(BaseModel):
    person_key: str = field(default_factory=lambda: str(uuid.uuid4()))
    frame_key: Optional[str] = None
    bbox: Optional[BBox] = None 
    embedding_key: Optional[str] = None
    keypoint_key: Optional[str] = None
    is_face_clear: bool = False
    face_bbox: Optional[BBox] = None 
    def __init__(self, **data):

        if 'person_key' not in data:
            data['person_key'] = str(uuid.uuid4())
        super().__init__(**data)
