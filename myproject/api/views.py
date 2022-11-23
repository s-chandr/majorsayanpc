from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
from main_payments.models import Payment,Shop,Order,Customer,ShopReview
from .serializer import PaymentSerializer,ShopSerializer,CustomerSerializer,OrderSerializer,ShopReviewSerializer

#Payments
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getPayment(request):
    payments = Payment.objects.all()
    serializer  = PaymentSerializer(payments,many=True) 
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def postPayment(request): 
    # print(request.data['payment_id']) #WORKS
    serializer  = PaymentSerializer(data = request.data)
    if serializer.is_valid():
         serializer.save()
        
    return Response(serializer.data)
####################################################################



#Reviews
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getReview(request):
    review = ShopReview.objects.all()
    serializer  = ShopReviewSerializer(review,many=True) 
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def postReview(request): 
    serializer  = ShopReviewSerializer(data = request.data)
    if serializer.is_valid():
         serializer.save()
        
    return Response(serializer.data)
#####################################################

#Shop
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getShop(request):
    review = Shop.objects.all()
    serializer  = ShopSerializer(review,many=True) 
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def postShop(request): 
    serializer  = ShopSerializer(data = request.data)
    if serializer.is_valid():
         serializer.save()
        
    return Response(serializer.data)
################################################################

#Customer 
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getCustomer(request):
    review = Customer.objects.all()
    serializer  = CustomerSerializer(review,many=True) 
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def postCustomer(request): 
    serializer  = CustomerSerializer(data = request.data)
    if serializer.is_valid():
         serializer.save()
        
    return Response(serializer.data)


################################################################

#order
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getOrder(request):
    review = Order.objects.all()
    serializer  = OrderSerializer(review,many=True) 
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def postOrder(request): 
    serializer  = OrderSerializer(data = request.data)
    if serializer.is_valid():
         serializer.save()
        
    return Response(serializer.data)
