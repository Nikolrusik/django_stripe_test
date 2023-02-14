from django.views.generic import TemplateView, View
from django.http import HttpResponse, JsonResponse
from django.core.serializers import serialize
from django.shortcuts import get_object_or_404
from .models import Item
import stripe
import json

class ItemView(TemplateView):
    template_name = "base_app/index.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super(ItemView, self).get_context_data(**kwargs)
        context['prod'] = get_object_or_404(
            Item, pk=pk
        )

        return context

   

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
        # data = serialize('json', checkout_session)
        return JsonResponse(
            {'session_id':checkout_session.id}
            )