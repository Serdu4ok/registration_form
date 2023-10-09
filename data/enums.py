from enum import Enum


class PetType(str, Enum):
    DOG = 'dog'
    CAT = 'cat'


class State(str, Enum):
    ALABAMA = 'AL'
    ALASKA = 'AK'
    ARIZONA = 'AZ'
    ARKANSAS = 'AR'
    CALIFORNIA = 'CA'
    COLORADO = 'CO'
    CONNECTICUT = 'CT'
    DISTRICT_COLUMBIA = 'DC'
    DELAWARE = 'DE'
    FLORIDA = 'FL'
    GEORGIA = 'GA'
    HAWAII = 'HI'
    IDAHO = 'ID'
    ILLINOIS = 'IL'
    INDIANA = 'IN'
    IOWA = 'IA'
    KANSAS = 'KS'
    KENTUCKY = 'KY'
    LOUISIANA = 'LA'
    MAINE = 'ME'
    MARYLAND = 'MD'
    MASSACHUSETTS = 'MA'
    MICHIGAN = 'MI'
    MINNESOTA = 'MN'
    MISSISSIPPI = 'MS'
    MISSOURI = 'MO'
    MONTANA = 'MT'
    NEBRASKA = 'NE'
    NEVADA = 'NV'
    NEW_HAMPSHIRE = 'NH'
    NEW_JERSEY = 'NJ'
    NEW_MEXICO = 'NM'
    NEW_YORK = 'NY'
    NORTH_CAROLINA = 'NC'
    NORTH_DAKOTA = 'ND'
    OHIO = 'OH'
    OKLAHOMA = 'OK'
    OREGON = 'OR'
    PENNSYLVANIA = 'PA'
    RHODE_ISLAND = 'RI'
    SOUTH_CAROLINA = 'SC'
    SOUTH_DAKOTA = 'SD'
    TENNESSEE = 'TN'
    TEXAS = 'TX'
    UTAH = 'UT'
    VERMONT = 'VT'
    VIRGINIA = 'VA'
    WASHINGTON = 'WA'
    WEST_VIRGINIA = 'WV'
    WISCONSIN = 'WI'
    WYOMING = 'WY'

    @staticmethod
    def get_state_list():
        return list(State)


class Urls(str, Enum):
    REGISTRATION = 'https://www.dutch.com/account/register#/'
    MAIN_PAGE = 'https://www.dutch.com/'


class Issues(str, Enum):
    ALLERGY = 'Allergy'
    ANXIETY = 'Anxiety'
    ARTHRITIS_JOINTS = 'Arthritis/joints'
    BEHAVIORAL = 'Behavioral'
    COUGHING = 'Coughing'
    DIARRHEA = 'Diarrhea'


class GeneralConstants(str, Enum):
    LONG_MSG_25 = 'To long message for test '
    DEFAULT_EMAIL = 'test.test@0gmail.com'
    INVALID_EMAIL = '123@2'
