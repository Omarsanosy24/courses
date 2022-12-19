from django.db import models
from authentication.models import User
# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=50)
    des = models.TextField()
    image = models.ImageField(upload_to='teacher/%y/%m/%d', null=True , blank=True)
    
    def __str__(self):
        return self.name
class college(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class year(models.Model):
    name = models.CharField(max_length=100)
    college = models.ForeignKey(college, on_delete=models.CASCADE)
    

    def __str__(self) -> str:
        return (self.name +"  "+self.college.name)

class CatCourses(models.Model):
    choices = [
        ("1",'1'),('2','2')
    ]
    term = models.CharField(max_length=10, choices=choices)
    name = models.CharField(max_length=100)
    des = models.TextField()
    price = models.IntegerField()
    image = models.ImageField(upload_to='CatCourses/%y/%m/%d', null=True , blank= True)
    year = models.ForeignKey(year, on_delete=models.CASCADE, related_name='ye')
    star = models.BooleanField(default=False, null=True, blank=True)
    active = models.BooleanField(default=True, null=True, blank=True)
    users = models.ManyToManyField(User, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=models.PROTECT, related_name='cources' ,null=True, blank=True) 
    cartIcon = models.BooleanField(null=True, blank=True)
    myCourseIcon = models.BooleanField(null=True, blank=True)

    def __str__(self) -> str:
        return (self.name +"  "+self.year.name +" "+self.term)

class Courses(models.Model):
    name = models.CharField(max_length=100)
    des = models.TextField()
    video = models.TextField()
    CatCourses = models.ForeignKey(CatCourses, on_delete=models.CASCADE, related_name='videos')
    def __str__(self) -> str:
        return self.name



class Banars(models.Model):
    image = models.ImageField(upload_to='banars')


class Cart(models.Model):
    userCart = models.OneToOneField(User, on_delete=models.CASCADE, related_name= 'userCart')
    totlaPrice = models.DecimalField(decimal_places=2, max_digits=100, null = True, blank = True, default=0.00)
    url = models.TextField(null=True, blank=True)
    

    def __str__(self):
        return self.userCart.email

class CartItem(models.Model):
    userCartItem = models.ForeignKey(User, on_delete=models.CASCADE, related_name= 'userCartItem')
    cart = models.ForeignKey(Cart, on_delete = models.CASCADE, related_name = 'cartItemWithCart')
    Courses = models.ForeignKey(CatCourses, related_name = 'Courses', on_delete = models.CASCADE)
    price = models.IntegerField()
    

    def __str__(self):
        return self.userCartItem.email



