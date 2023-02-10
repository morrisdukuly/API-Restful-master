from config import db
import enum 
from sqlalchemy import Enum 


class OrderStatus(enum.Enum):
    CREATE = 0
    SHIPPING = 1
    DELIVERED = 2
    PAID = 3