from typing import Optional, List, Dict, Any
import phonenumbers
import ipaddress
from pydantic import BaseModel, ValidationError, validator, root_validator, AnyUrl, constr, EmailStr

class ContextFormatError(Exception):
    def __init__(self, value, message) -> None:
        self.value = value
        self.message = message
        super().__init__(value, message)

class Ad(BaseModel):
    # ttclid
    callback: Optional[constr(
        strip_whitespace=True, max_length=501
    )]

    @validator('callback', pre=True)
    @classmethod
    def callback_is_valid(cls, value):
        """
        Check if the callback value is a valid ttclid.
        """
        if value:
            ttclid_error = ContextFormatError(value=value, message="Callback must be a valid ttclid please check TikTok's documentation for more information on ttclid: https://ads.tiktok.com/marketing_api/docs?id=1739584860883969")

            value_list = value.split('.')

            if value[:6] != 'E.C.P.':
                raise ttclid_error

            if len(value_list) != 4:
                raise ttclid_error

            if any(len(value) != 1 for value in value_list[0:3]):
                raise ttclid_error

            if len(value_list[3]) <= 1:
                raise ttclid_error

        return value

class Page(BaseModel):
    url: AnyUrl
    referrer: Optional[AnyUrl]

class User(BaseModel):
    external_id: Optional[constr(min_length=1, strip_whitespace=True)]
    email: Optional[EmailStr]
    phone_number: Optional[str]
    ttp: Optional[constr(min_length=1, strip_whitespace=True)]


    @validator('phone_number')
    @classmethod
    def validate_phone_number(cls, field_value):
        if field_value:
            number = phonenumbers.parse(field_value, None)
            phonenumbers.format_number(number, phonenumbers.PhoneNumberFormat.E164)

            is_possible = phonenumbers.is_possible_number(number)

            if phonenumbers.is_possible_number(number) == False:
                raise ContextFormatError(value=field_value, message='Must be a valid phone number: +{country code}{local code}{phone number} / +001199999999')

        return field_value

    @root_validator(pre=True)
    @classmethod
    def validate_user(cls, values):
        if not any(values.values()):
            raise ContextFormatError(value=values, message='User must have at least one of the following: external_id, email, phone_number, ttp')
        return values

# Context object parameters
class Context(BaseModel):
    user_agent: constr(min_length=1) # Client user agent
    ip: ipaddress.IPv4Address # User IP address
    ad: Optional[Ad] # ttclid
    page: Page
    user: User
