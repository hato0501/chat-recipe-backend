from abc import ABC, abstractmethod
from app.domain.entities.message import Message

class IChatRepository(ABC):

    @abstractmethod
    def get_chatgpt_response(self, text: str) -> Message:
        pass
