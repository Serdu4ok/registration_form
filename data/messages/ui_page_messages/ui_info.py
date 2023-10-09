class RegistrationInfo:
    PET_INFO_MSG = {'text': 'Let’s get to know your pet', 'locator': '//h1'}

    @staticmethod
    def issue_info_msg(pet_name: str):
        return {'text': f'What issues does {pet_name}\nneed help with?',
                'locator': '//h1'}

    @staticmethod
    def create_acc_info_msg(pet_name: str):
        return {'text': f'Create {pet_name}’s account',
                'locator': '//h1'}
