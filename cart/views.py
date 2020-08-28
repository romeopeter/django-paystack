import json

from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest

from cart.models import Cart

app_name = "cart"


def cart(request):
    if request.method == "POST":
        cart_items = request.body

        if cart_items.decode("utf-8") == "No Cart":
            return JsonResponse(
                {
                    "statusCode": 200,
                    "statusText": "success",
                    "message": "preflight cart",
                },
            )

        cart_items = json.loads(cart_items.decode("utf-8"))
        cart_object = Cart.objects.all()

        for item in cart_items:
            if cart_object.filter(pk=item["productID"]).exists():
                return JsonResponse(
                    {
                        "statusCode": 400,
                        "statusText": "Erorr",
                        "message": "Item has already been saved",
                    }
                )

            save_carts = Cart.objects.create(
                product_image_url=["productImage"], product_subtotal=["productPrice"]
            )

            if save_carts.saved():
                return JsonResponse(
                    {"status": 200, "statusText": "success", "message": "Cart saved"}
                )

    return JsonResponse(
        {
            "statusCode": 404,
            "statusText": "Bad Request",
            "message": "GET request sent, expecting POST",
        }
    )


def checkout():
    pass
