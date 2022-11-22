from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import permissions
from main_payments.models import Payment,Shop,Order,Customer,ShopReview
from .serializer import PaymentSerializer,ShopSerializer,CustomerSerializer,OrderSerializer,ShopReviewSerializer


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getData(request):
    payments = Payment.objects.all()
    serializer  = PaymentSerializer(payments,many=True) 
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def postData(request): 
    # print(request.data['payment_id']) #WORKS
    serializer  = PaymentSerializer(data = request.data)
    if serializer.is_valid():
         serializer.save()
        
    return Response(serializer.data)






@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getData(request):
    payments = Payment.objects.all()
    serializer  = PaymentSerializer(payments,many=True) 
    return Response(serializer.data)


@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def postData(request): 
    # print(request.data['payment_id']) #WORKS
    serializer  = PaymentSerializer(data = request.data)
    if serializer.is_valid():
         serializer.save()
        
    return Response(serializer.data)






@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getData(request):
    payments = Payment.objects.all()
    serializer  = PaymentSerializer(payments,many=True) 
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def postData(request): 
    # print(request.data['payment_id']) #WORKS
    serializer  = PaymentSerializer(data = request.data)
    if serializer.is_valid():
         serializer.save()
        
    return Response(serializer.data)





@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getData(request):
    payments = Payment.objects.all()
    serializer  = PaymentSerializer(payments,many=True) 
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def postData(request): 
    # print(request.data['payment_id']) #WORKS
    serializer  = PaymentSerializer(data = request.data)
    if serializer.is_valid():
         serializer.save()
        
    return Response(serializer.data)






@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getData(request):
    payments = Payment.objects.all()
    serializer  = PaymentSerializer(payments,many=True) 
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def postData(request): 
    # print(request.data['payment_id']) #WORKS
    serializer  = PaymentSerializer(data = request.data)
    if serializer.is_valid():
         serializer.save()
        
    return Response(serializer.data)






@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getData(request):
    payments = Payment.objects.all()
    serializer  = PaymentSerializer(payments,many=True) 
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def postData(request): 
    # print(request.data['payment_id']) #WORKS
    serializer  = PaymentSerializer(data = request.data)
    if serializer.is_valid():
         serializer.save()
        
    return Response(serializer.data)





@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def getData(request):
    payments = Payment.objects.all()
    serializer  = PaymentSerializer(payments,many=True) 
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes((permissions.AllowAny,))
def postData(request): 
    # print(request.data['payment_id']) #WORKS
    serializer  = PaymentSerializer(data = request.data)
    if serializer.is_valid():
         serializer.save()
        
    return Response(serializer.data)

