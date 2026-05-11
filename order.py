from dataclasses import dataclass, field
from models.payment import Payment
from models.notification import Notification

@dataclass
class Order:

    customer_name: str = ""
    address: str = ""

    items: list = field(default_factory=list)

    payment_method: Payment | None = None
    notification_method: Notification | None = None

    discount: float = 0.0
    special_note: str = ""

    total_price: int = 0
