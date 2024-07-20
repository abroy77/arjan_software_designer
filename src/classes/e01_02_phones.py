# Exercise 2
# making a datastructure for phones, customers and phone plans
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Customer:
   name: str
   address: str
   email_address: str

@dataclass
class Phone:
   brand: str
   model: str
   price: int
   serial_number: str

@dataclass
class Plan:
   Customer: Customer
   phone: Phone
   start_time: datetime = field(default_factory=datetime.now)
   months: int
   monthly_price: int

