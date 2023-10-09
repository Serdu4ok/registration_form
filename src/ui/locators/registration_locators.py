class RegistrationLocators:
    BUTTON_SUBMIT = 'button[type=\'submit\']'
    BUTTON_INFO_SUBMIT = '(//button[text()=" Continue "])[2]'

    INPUT_PET_NAME = '//input[@id="pet-name"]'
    INPUT_EMAIL = '//input[@type="email"]'
    INPUT_PASSWORD = '//input[@type="password"]'

    SELECT_PET_ISSUE = '//label[@for="{}"]'
    SELECT_STATE = '//option[@value="{}"]'
    DROPDOWN_STATE = '//select[@id="state"]'
    RADIO_PET_TYPE = '//input[@id="{}"]'

    INFO_ABOUT_VET_SEEN = '//h2[text()=" We’ll need info about a vet your pet has seen "]'
    INFO_ONLINE_RESTRICTION = '//h2[contains(text(), "{} doesn’t allow online prescriptions yet")]'
