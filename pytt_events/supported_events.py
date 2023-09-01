"""
Supported web events
https://ads.tiktok.com/marketing_api/docs?id=1741601162187777
"""

from enum import Enum


class SupportedEvents(str, Enum):
    """List of standard events that can be reported to TikTok.

    At this time you can report custom events but TikTok won't optimize for them.
    """
    """
    When a page is viewed.
    """
    VIEW_CONTENT = 'ViewContent'
    """
    When a button is clicked.
    """
    CLICK_BUTTON = 'ClickButton'
    """
    When a search is made.
    """
    SEARCH = 'Search'
    """
    When an item is added to a wishlist.
    """
    ADD_TO_WISHLIST = 'AddToWishlist'
    """
    When an item is added to the shopping cart.
    """
    ADD_TO_CART = 'AddToCart'
    """
    When the checkout process is started.
    """
    INITIATE_CHECKOUT = 'InitiateCheckout'
    """
    When payment information is added in the checkout flow.
    """
    ADD_PAYMENT_INFO = 'AddPaymentInfo'
    """
    When a payment is completed.
    """
    COMPLETE_PAYMENT = 'CompletePayment'
    """
    When an order is placed.
    """
    PLACE_AN_ORDER = 'PlaceAnOrder'
    """
    When contact or consultation occurs.
    """
    CONTACT = 'Contact'
    """
    When a button to open an external browser download page is clicked.
    """
    DOWNLOAD = 'Download'
    """
    When a form is submitted.
    """
    SUBMIT_FORM = 'SubmitForm'
    """
    When a registration is completed.
    """
    COMPLETE_REGISTRATION = 'CompleteRegistration'
    """
    When a subscription is made.
    """
    SUBSCRIBE = 'Subscribe'

    def __str__(self):
        return self.value
