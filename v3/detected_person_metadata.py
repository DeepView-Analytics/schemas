
from pydantic import BaseModel

from v3.bbox import BBox

class DetectedPerson(BaseModel):
    person_key: str
    frame_key: str
    bbox : BBox 
    embedding_key: str
    keypoint_key: str
    is_face_clear: bool
    

