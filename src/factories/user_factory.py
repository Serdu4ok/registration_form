import random

from data.data_generator import DataGenerator
from data.enums import PetType, State, Issues
from data.models.account import Account
from data.models.pet import Pet


class UserFactory:
    def __init__(self):
        self.generator = DataGenerator()

    def user_options(self, pet_type: PetType = PetType.DOG, state: State = State.ALABAMA) -> Account:
        data = Account()
        data.pet = self.pet_options(pet_type)
        data.password = self.generator.get_random_password()
        data.email = self.generator.get_random_email()
        data.state = state
        return data

    def pet_options(self, pet_type: PetType) -> Pet:
        data = Pet()
        data.pet_name = self.generator.get_random_first_name()
        data.pet_type = pet_type
        data.pet_issues = [random.choice(list(Issues))]
        return data
