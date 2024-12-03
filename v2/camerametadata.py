import uuid
from dataclasses import dataclass
from typing import Optional, List
from v2.person import Person

@dataclass
class CameraMetadata:
    camera_id: str
    timestamp: str
    persons: List[Person]  = None
    emmbedding_complete : bool = False
    keypoint_complete : bool = False

    def __init__(self, camera_id: str, timestamp: str, persons: List[Person]):
        self.camera_id = camera_id
        self.timestamp = timestamp
        self.persons = persons
    