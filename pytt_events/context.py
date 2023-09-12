from typing import Optional
from . import utils
import phonenumbers
import ipaddress
from pydantic import (
    BaseModel,
    validator,
    root_validator,
    AnyUrl,
    constr,
    EmailStr
)


class Ad(BaseModel):
    """ Ad information object.

    If you don't have a ttclid do not include this object in the event.
    Attributes:
        callback (str): TikTok Click ID (ttclid).
    """

    callback: Optional[constr(
        strip_whitespace=True, max_length=501
    )]

    @validator('callback', pre=True)
    @classmethod
    def callback_is_valid(cls, value):
        """ Check if the callback value is a valid ttclid.

        A valid ttclid must start with E.C.P
        """
        if value:
            ttclid_error = utils.ContextFormatError(
                value=value,
                message="Callback must be a valid ttclid please check "
                        "TikTok's documentation for more information on "
                        "ttclid: "
                        "https://ads.tiktok.com/marketing_api/docs?id"
                        "=1739584860883969"
            )

            value_list = value.split('.')

            if value[:6] != 'E.C.P.':
                raise ttclid_error

            if len(value_list) != 4:
                raise ttclid_error

            if any(len(value) != 1 for value in value_list[:3]):
                raise ttclid_error

            if len(value_list[3]) <= 1:
                raise ttclid_error

        return value


class Page(BaseModel):
    """ Page information object.

    If you don't have a source URL or referrer URL do not include this object in the event.
    Attributes:
        url (AnyUrl): [Optional] URL of the page where the event happened.
        referrer (AnyUrl): [Optional] URL of the page where the user came from.
    """
    url: Optional[AnyUrl]
    referrer: Optional[AnyUrl]


class User(BaseModel):
    """ The personal data of a user.

    At least one of the following attributes must be provided.

    Attributes:
        external_id (str): [Optional] User ID.
        email (EmailStr): [Optional] User email.
        phone_number (str): [Optional] User phone number.
        ttp (str): [Optional] TikTok browser ID saved in _ttp cookie.
    """
    external_id: Optional[constr(min_length=1, strip_whitespace=True)]
    email: Optional[EmailStr]
    phone_number: Optional[str]
    ttp: Optional[constr(min_length=1, strip_whitespace=True)]

    @validator('phone_number')
    @classmethod
    def validate_phone_number(cls, field_value):
        if field_value:
            number = phonenumbers.parse(field_value, None)

            if not phonenumbers.is_possible_number(number):
                raise utils.ContextFormatError(
                    value=field_value,
                    message='Must be a valid phone number: +{country code}{'
                            'local code}{phone number} / +001199999999'
                )

            field_value = phonenumbers.format_number(
                number,
                phonenumbers.PhoneNumberFormat.E164
            )

        return field_value

    @root_validator(pre=True)
    @classmethod
    def validate_user(cls, values):
        if not any(values.values()):
            raise utils.ContextFormatError(
                value=values,
                message='User must have at least one of the following: '
                        'external_id, email, phone_number, ttp'
            )
        return values


class Context(BaseModel):
    """ Context information object.

    Required to attribute events to TikTok campaigns.
    Information about the circumstances when the event was triggered, such as User data and conversion URL.

    Attributes:
        user_agent (str): [Optional] Client user agent.
        ip (ipaddress.IPv4Address): [Optional] Client IP address.
        ad (Ad): [Optional] ttclid.
        page (Page): [Optional] URL of the page where the event happened and URL of the page where the user came from.
        user (User): [Optional] User data.
    """
    user_agent: Optional[constr(min_length=1)]
    ip: Optional[ipaddress.IPv4Address]
    ad: Optional[Ad]
    page: Optional[Page]
    user: Optional[User]
