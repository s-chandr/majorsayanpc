from django.db import models

class Shop(models.Model):
    shop_id = models.AutoField(primary_key=True)
    
class Customer(models.Model):
    customer_id = models.AutoField(primary_key=True)

class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

class Payment(models.Model):
    payment_id = order_id = models.AutoField(primary_key=True)
    #cantake from razorpay id as well
    shop_id = models.ForeignKey(Shop,on_delete=models.CASCADE)
    customer_id = models.ForeignKey(Customer,on_delete=models.CASCADE)
    order_id = models.ForeignKey(Order,on_delete=models.CASCADE)
    time_stamp = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()


class ShopReview(models.Model):
    user_id=models.ForeignKey(Customer,on_delete=models.CASCADE)
    shop_id=models.ForeignKey(Shop,on_delete=models.CASCADE)
    rating=models.IntegerField()

    def get_review_rating(self):
        return self.review_rating
