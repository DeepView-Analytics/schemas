from pydantic import BaseModel
from typing import List
from v1.bbox import Bbox


class ObjectDetected(BaseModel):
    camera_id: str
    timestamp: str 
    object_detected: List[Bbox]  
    
