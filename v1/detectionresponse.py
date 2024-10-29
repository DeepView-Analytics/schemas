from typing import List
from v1.objectdetected import ObjectDetected
from pydantic import BaseModel

class DetectionResponse(BaseModel):
    request_id: int
    detection: List[ObjectDetected]

