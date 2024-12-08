from pydantic import BaseModel, Field
from typing import List

class FrameMetadata(BaseModel):
    frame_key: str
    detected_persons: List[str] = Field(default_factory=list) 
    keypoint_complete: bool = False  
    embeding_complete: bool = False  
