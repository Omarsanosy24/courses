from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny , IsAuthenticatedOrReadOnly
from .models import *
from rest_framework_api_key.permissions import HasAPIKey


class teacherSerializers(serializers.ModelSerializer):

    class Meta:
        model = Teacher
        fields = '__all__'

class CourseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Courses
        fields = "__all__"

class yearSerializers(serializers.ModelSerializer):

    class Meta:
        model = year
        fields = ['id','name']
class CatCourseSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = CatCourses
        fields = '__all__'


class YearSerializerswithCatCourses(serializers.ModelSerializer):
    year = serializers.SlugRelatedField(slug_field='name', read_only = True , source ='ye')
    class Meta:
        model = year
        fields = '__all__'

class collegeSerializers(serializers.ModelSerializer):

    class Meta:
        model = college
        fields = '__all__'


class CartItemSerilaizers(serializers.ModelSerializer):
    
    Courses = CatCourseSerializers(many = True)
    class Meta:
        model = CartItem
        fields = '__all__'
class CartItemSer(serializers.ModelSerializer):
    Courses = CatCourseSerializers( read_only = True)

    class Meta:
        model = CartItem
        fields = ['Courses','price']

class CartSerializers11(serializers.ModelSerializer):

    cartItemWithCart = CartItemSer(many=True)
    class Meta:
        model = Cart
        fields = '__all__'
    

class teacherSerializers1(serializers.ModelSerializer):
    cources = CatCourseSerializers(many = True , read_only = True)
    class Meta:
        model = Teacher
        fields = '__all__'

class CatWithvideSerializers(serializers.ModelSerializer):
    videos = CourseSerializers(read_only = True, many = True)
    class Meta:
        model = CatCourses
        fields = '__all__'
    
class BannarsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Banars
        fields = '__all__'

