from abc import ABC, abstractmethod



class Notification(ABC):

    @abstractmethod
    def send(self, message: str) -> str:
        pass


class SMSNotification(Notification):

    def send(self, message: str) -> str:
        return f"SMS sent to customer: {message}"


class EmailNotification(Notification):

    def send(self, message: str) -> str:
        return f"Email sent to customer: {message}"