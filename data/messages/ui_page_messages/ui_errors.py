class NotificationHelper:

    @staticmethod
    def get_locator_by_id_sibling(current_id: str) -> str:
        return f'//input[@id="{current_id}"]/following-sibling::ul'


class RegistrationErrors:
    empty_pet_name = {'text': 'Pet name cannot be empty',
                      'locator': NotificationHelper.get_locator_by_id_sibling('pet-name')}
    max_len_pet_name = {'text': 'The maximum length allowed is 24',
                        'locator': '//input[@id="pet-name"]/following-sibling::ul'}

    required_email = {'text': 'email is required', 'locator': NotificationHelper.get_locator_by_id_sibling('email')}
    required_password = {'text': 'password is required',
                         'locator': NotificationHelper.get_locator_by_id_sibling('password')}
    shot_password = {'text': 'Password is too short (minimum is 5 characters)',
                     'locator': '//form/following-sibling::ul'}

    invalid_email = {'text': 'email is not a valid email address',
                     'locator': NotificationHelper.get_locator_by_id_sibling('email')}
