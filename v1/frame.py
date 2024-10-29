from pydantic import BaseModel
class Frame(BaseModel):
    camera_id: str
    timestamp: str 