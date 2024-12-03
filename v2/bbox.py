from dataclasses import dataclass
from typing import Optional, List

@dataclass
class BBox:
    xmin: float
    xmax: float
    ymin: float
    ymax: float
    conf: float

    def __init__(self, xmin: float, xmax: float, ymin: float, ymax: float, conf: float):
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax
        self.conf = conf