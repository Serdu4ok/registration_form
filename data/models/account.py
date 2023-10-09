from typing import Optional

from data.enums import State
from data.models.pet import Pet


class Account:
    pet: Pet
    state: State
    password: str
    email: str
    first_name: Optional[str]
    last_name: Optional[str]
    address: Optional[str]
    apartment: Optional[str]
    city: Optional[str]
    phone_number: Optional[str]
