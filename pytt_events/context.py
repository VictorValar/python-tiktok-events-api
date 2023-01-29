import pydantic
from typing import Optional, List, Dict, Any
import phonenumbers

class ContextFormatError(Exception):
    def __init__(self, value, message) -> None:
        self.value = value
        self.message = message
        super().__init__(value, message)

class Ad(pydantic.BaseModel):
    callback: Optional[str]

    @pydantic.validator('callback', pre=True)
    @classmethod
    def callback_is_valid(cls, value):
        ttclid_error = ContextFormatError(value=value, message='Callback must be a valid ttclid')

        # Check if callbaclk is a valid ttclid
        # E.C.P.v3fQ2RHacdksKfofPmlyuStIIHJ4Af1tKYxF9zz2c2PLx1Oaw15oHpcfl5AH
        if not value or value == '':
                raise ttclid_error
        value_list = value.split('.')
        print(len(value_list))
        if len(value_list) != 4:
            raise ttclid_error
        if any(len(value) != 1 for value in value_list[0:3]):
            raise ttclid_error
        if len(value_list[3]) <= 1:
            raise ttclid_error
        return value

class Page(pydantic.BaseModel):
    url: str
    referrer: Optional[str]

    # validate that url is a valid url
    @pydantic.validator('url', 'referrer', pre=True)
    @classmethod
    def url_is_valid(cls, value):
        # check if empty string
        if not value:
            raise ContextFormatError(value=value, message='URL cannot be empty')
        if not value.startswith('http'):
            raise ContextFormatError(value=value, message='URL must start with http')
        return value

class User(pydantic.BaseModel):
    external_id: Optional[str]
    email: Optional[str]
    phone_number: Optional[str]
    ttp: Optional[str]

    @pydantic.root_validator(pre=True)
    @classmethod
    def validate_user(cls, values):
        if not any(values.values()):
            raise ContextFormatError(value=values, message='User must have at least one of the following: external_id, email, phone_number, ttp')
        return values

    @pydantic.validator('email')
    @classmethod
    def validate_email(cls, field_value):
        if field_value:
            if '@' not in field_value:
                raise ContextFormatError(value=field_value, message='Must be a valid email address')
        return field_value

    @pydantic.validator('phone_number')
    @classmethod
    def validate_phone_number(cls, field_value):
        if field_value:
            number = phonenumbers.parse(field_value, None)
            phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)
            print(number)
            is_possible = phonenumbers.is_possible_number(number)
            print(is_possible)
            if phonenumbers.is_possible_number(number) == False:
                raise ContextFormatError(value=field_value, message='Must be a valid phone number: +{country code}{local code}{phone number} / +001199999999')
        return field_value


# Context object parameters
class Context(pydantic.BaseModel):
    user_agent: str # Client user agent
    ip: str # User IP address
    ad: Optional[Ad] # ttclid
    page: Page
    user: User
