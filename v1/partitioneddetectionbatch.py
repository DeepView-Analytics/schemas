from typing import List
from v1.bbox import Bbox
from pydantic import BaseModel

class PartitionedDetectionBatch(BaseModel):
    camera_id: str
    timestamp: str
    object_detected: List[Bbox]
    partition_number: int
    total_partitions: int
