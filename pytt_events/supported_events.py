from enum import Enum

# Supported web events
# https://ads.tiktok.com/marketing_api/docs?id=1741601162187777
class SupportedEvents(Enum):

    """
    When a page is viewed.
    """
    ViewContent = 'ViewContent'
    """
    When a button is clicked.
    """
    ClickButton = 'ClickButton'
    """
    When a search is made.
    """
    Search = 'Search'
    """
    When an item is added to a wishlist.
    """
    AddToWishlist = 'AddToWishlist'
    """
    When an item is added to the shopping cart.
    """
    AddToCart = 'AddToCart'
    """
    When the checkout process is started.
    """
    InitiateCheckout = 'InitiateCheckout'
    """
    When payment information is added in the checkout flow.
    """
    AddPaymentInfo = 'AddPaymentInfo'
    """
    When a payment is completed.
    """
    CompletePayment = 'CompletePayment'
    """
    When an order is placed.
    """
    PlaceAnOrder = 'PlaceAnOrder'
    """
    When contact or consultation occurs.
    """
    Contact = 'Contact'
    """
    When a button to open an external browser download page is clicked.
    """
    Download = 'Download'
    """
    When a form is submitted.
    """
    SubmitForm = 'SubmitForm'
    """
    When a registration is completed.
    """
    CompleteRegistration = 'CompleteRegistration'
    """
    When a subscription is made.
    """
    Subscribe = 'Subscribe'