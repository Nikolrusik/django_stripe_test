from django.views.generic import TemplateView, View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from .models import Item
import stripe

class ItemView(TemplateView):
    template_name = "index.html"

   

class BuyView(View):
     def get(self, request, pk=None):
        item = get_object_or_404(
            Item, pk=pk
        )
        product = stripe.Product.create(
            name=item.Name,
            description=item.Description,
        )
        price = stripe.Price.create(
            unit_amount=item.Price,
            currency="usd",
            product=product.id,
        )
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    'price': price.id,
                    'quantity': 1,
                }
            ],
            mode='payment',
            success_url = "http://localhost:8000/buy/",
        )
        
        return HttpResponse(checkout_session.id)