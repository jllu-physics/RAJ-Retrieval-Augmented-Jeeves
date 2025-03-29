from abc import ABC, abstractmethod
import numpy as np
from common.chunk import Chunk
from common.query import Query

class DatabaseWrapper(ABC):
    @abstractmethod
    def index(self, chunks: Chunk):
        pass

    @abstractmethod
    def retrieve(self, query: Query, k: int):
        pass