import random
import string

from faker import Faker


class DataGenerator:
    def __init__(self):
        self.faker = Faker()

    def get_random_first_name(self) -> str:
        return self.faker.first_name()

    def get_random_last_name(self) -> str:
        return self.faker.last_name()

    def get_random_email(self) -> str:
        return self.faker.email()

    def get_random_password(self) -> str:
        return self.faker.password()

    @staticmethod
    def generate_random_message(length):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))
