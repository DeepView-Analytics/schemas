from typing import List
from v1.frame import Frame
from pydantic import BaseModel
class DetectionRequest(BaseModel):
    request_id: int
    frames: List[Frame]
