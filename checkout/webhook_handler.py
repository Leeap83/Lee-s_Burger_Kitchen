from django.http import HttpResponse


class StripeWH_Handler:
    """Handle Stripe Webhook"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, request):
        """Handle generic webhook events"""

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
