
from pydantic import BaseModel


class FrameMetadata(BaseModel):
    frame_key: str
    detected_persons : list[str] 
    keypoint_complete: bool
    embeding_complete: bool
