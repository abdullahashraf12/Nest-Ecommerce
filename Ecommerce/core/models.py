from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.safestring import mark_safe
from userauths.models import User
# Create your models here.

STATUS_CHOICE = (
    ("process","Processing"),
    ("shipped","Shipped"),
    ("delivered","Delivered"),
)
STATUS = (
    ("draft","Draft"),
    ("disabled","Disabled"),
    ("in_review","In_Review"),
    ("published","Published"),
)

RATING = (
    (1,"⭐★★★★★★"),
    (2,"⭐⭐★★★★★"),
    (3,"⭐⭐⭐★★★★"),
    (4,"⭐⭐⭐⭐★★★"),
    (5,"⭐⭐⭐⭐⭐★★"),
    (6,"⭐⭐⭐⭐⭐⭐★"),
    (7,"⭐⭐⭐⭐⭐⭐⭐")
)



def user_directory_path(instance,filename):
    return 'user_{0}/{1}'.format(instance.user.id,filename)

class Category(models.Model):
    cid = ShortUUIDField(unique=True,length=10,max_length= 20,prefix="cat",alphabet="abcdefgh12345")
    title = models.CharField(max_length=100,default = "Food")
    image = models.ImageField(upload_to="Category",default="category.jpg")
    class Meta:
        verbose_name_plural = "Category"
    
    def category_image(self):
        return mark_safe("<img src='/media/%s' width='50' height ='50'/>" % (self.image))
    def __str__(self):
        return str(self.title)
        
class Vendor(models.Model):
    vid =ShortUUIDField(unique=True,length=10,max_length= 20,prefix="ven",alphabet="abcdefgh12345")
    title = models.CharField(max_length = 100,default="Nestify")
    image = models.ImageField(upload_to=user_directory_path,default="vendor.jpg")
    description = models.TextField(null=True,blank=True,default="i am amazing vendor")
    
    address = models.CharField(max_length=100,default="123 Main Street")
    contact = models.CharField(max_length=100,default="+123 (456) 789")
    chat_resp_time =models.CharField(max_length=100,default ="100")
    shipping_resp_time =models.CharField(max_length=100,default ="100")
    Authentic_rating =models.CharField(max_length=100,default ="100")
    days_return =models.CharField(max_length=100,default ="100")
    warrantly_period = models.CharField(max_length=100,default ="100")

    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    class Meta:
        verbose_name_plural = "Category"
    
    def category_image(self):
        return mark_safe("<img src='/media/%s' width='50' height ='50'/>" % (self.image))
    def __str__(self):
        return str(self.title)
class Tags(models.Model):
    tid =ShortUUIDField(unique=True,length=10,max_length= 20,alphabet="abcdefgh12345")
    title = models.CharField(max_length = 100,default="Fresh Pear")

    # pass


class Products(models.Model):
    pid =ShortUUIDField(unique=True,length=10,max_length= 20,alphabet="abcdefgh12345")
    title = models.CharField(max_length = 100,default="Fresh Pear")
    image = models.ImageField(upload_to=user_directory_path,default="product.jpg")
    back_image = models.ImageField(upload_to=user_directory_path,default="product.jpg")
    description = models.TextField(null=True,blank=True)
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    category = models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name="category")
    vendor = models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True,related_name = "product")
    price = models.DecimalField(max_digits=9999999999999,decimal_places = 2,default="1.99")
    old_Price = models.DecimalField(max_digits=9999999999999,decimal_places = 2,default="2.99")
    spescification = models.TextField(null=True,blank=True)
    tags=models.ForeignKey(Tags,on_delete=models.SET_NULL,null=True,related_name="tags")
    products_status = models.CharField(choices=STATUS,max_length=30,default="in_review")
    status=models.BooleanField(default=True)
    in_stock=models.BooleanField(default=True)
    digital=models.BooleanField(default=False)
    featured = models.BooleanField(default=True)
    sku=ShortUUIDField(unique=True,length=10,max_length= 20,alphabet="abcdefgh12345")
    date=models.DateTimeField(auto_now_add=True)
    update=models.DateTimeField(null=True,blank=True)
    class Meta:
        verbose_name_plural = "Products"
    
    def product_image(self):
        return mark_safe("<img src='/media/%s' width='50' height ='50'/>" % (self.image))
    def __str__(self):
        return str(self.title)
    def precentage(self):
        new_price = (self.price/self.old_Price) * 100
        return new_price
class ProductImages(models.Model):
    images = models.ImageField(upload_to="product-images",default="product.jpg")
    product = models.ForeignKey(Products,on_delete=models.SET_NULL,null=True,related_name="p_images")
    date=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Products images"



class CardOrder(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9999999999999,decimal_places = 2,default="1.99")
    paid_status = models.BooleanField(default=False)
    order_date=models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE,max_length=30,default="processing")
    class Meta:
        verbose_name_plural = "Cards Order"
    
class CardOrderItems(models.Model): 
    order = models.ForeignKey(CardOrder,on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status= models.CharField(max_length=200)
    item=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    qty=models.IntegerField()
    price = models.DecimalField(max_digits=9999999999999,decimal_places = 2,default="1.99")
    total = models.DecimalField(max_digits=9999999999999,decimal_places = 2,default="1.99")
    class Meta:
        verbose_name_plural = "Cards Order Items"
    
    def order_image(self):
        return mark_safe("<img src='/media/%s' width='50' height ='50'/>" % (self.image))



class ProductReview(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    product= models.ForeignKey(Products,on_delete=models.CASCADE)
    review = models.TextField()
    rating=models.IntegerField(choices=RATING,default= None)
    date= models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "Product Reviews"
    
    def __str__(self):
        return str(self.product.title)
    def get_rating(self):
        return self.rating
class WishList(models.Model):
    user= models.ForeignKey(User,on_delete=models.CASCADE)
    product= models.ForeignKey(Products,on_delete=models.CASCADE)
    date= models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural = "WishList"
    
    def __str__(self):
        return str(self.product.title)
class Address(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    address = models.CharField(max_length = 100,null=True)
    status= models.BooleanField(default=False)
    class Meta:
        verbose_name_plural = "Address"
    