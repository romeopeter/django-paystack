from rest_framework.views import APIView
from rest_framework import authentication
from rest_framework.response import Response
from rest_framework import status

from .models import Cart
from .serializer import CartSerializer

from products.serializer import ProductSerializer


class AddItemToCart(APIView):
    """
    View to add item to cart

    * Requires authentication
    """

    serializer_class = CartSerializer

    # authentication_classes = [authentication.TokenAuthentication]

    def post(self, request, format=None):
        """
        Add product to cart
        """

        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error, status=status.HTTP_401_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        """
        Delete product from cart
        """

        cart = Cart.objects.get(pk=pk)
        cart.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
