from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import *
from .serializers import *
from rest_framework.response import Response
# Create your views here.

class teacherView (generics.GenericAPIView):
    serializer_class = teacherSerializers
    permission_classes = [IsAuthenticated , HasAPIKey]
    def get (self,request):
        if request.query_params:
            id1 = request.query_params['id']
            d = Teacher.objects.get(id=id1)
            serializers = teacherSerializers1(d)
            
        else:
            d = Teacher.objects.all()
            serializers = teacherSerializers(d , many=True)
        return Response({"data":serializers.data},status=status.HTTP_200_OK)

class Star(generics.GenericAPIView):
    serializer_class = CatCourseSerializers
    permission_classes = [IsAuthenticated , HasAPIKey]
    def get (self, request):
        if request.query_params:                
            id1 = request.query_params['id']
            d = CatCourses.objects.get(id=id1)
            serializers = CatCourseSerializers(d)
            
        else:
            d = CatCourses.objects.filter(star = True).filter(active = True)
            serializers = CatCourseSerializers(d , many=True)
        return Response({"data":serializers.data},status=status.HTTP_200_OK)

class CoursesViews(generics.GenericAPIView):
    serializer_class = YearSerializerswithCatCourses
    permission_classes = [IsAuthenticated , HasAPIKey]
    def get(self,request):
        if request.query_params:
                            
            id1 = request.query_params['CollegeId']
            d = year.objects.filter(college = id1).all()
            serializers = yearSerializers(d, many = True)
            try:
                if request.query_params:
                    ii = request.query_params['YearId']
                    l = CatCourses.objects.filter(year = ii).all()
                    serializers = CatCourseSerializers(l, many = True)
            except:
                pass
        else:
            d = college.objects.all()
            serializers = collegeSerializers(d , many=True)
        return Response({"data":serializers.data},status=status.HTTP_200_OK)


class AddToCArt(generics.GenericAPIView):
    serializer_class = CartItemSerilaizers
    permission_classes = [IsAuthenticated , HasAPIKey]
    def post(self,request):
        user = request.user
        course = request.data.get('CourseId')
        try:
            id =CatCourses.objects.get(id = course)
            car = Cart.objects.get(userCart = user)
            try:
                CartItem.objects.filter(userCartItem = request.user).get(Courses = id)
                return Response({"message":"this course in cart"},status=status.HTTP_200_OK)
            except:
                CartItem.objects.create(userCartItem = user,cart= car, Courses=id, price=int(id.price))
                carr = Cart.objects.get(userCart= request.user)
                r = CartItem.objects.filter(cart = carr)
                carr.totlaPrice = 0
                carr.save()
                for i in r:
                
                    carr.totlaPrice = carr.totlaPrice + i.price
                    carr.save()
                return Response({"message":"done"},status=status.HTTP_200_OK)
        except:
            
            return Response({"message":"None id"},status=status.HTTP_200_OK)
    def delete(self,request):
        user = request.user
        course = request.data.get('CourseId')
        try:
            id =CartItem.objects.get(id = course)
            id.delete()
            carr = Cart.objects.get(userCart= request.user)

            r = CartItem.objects.filter(cart = carr)
            carr.totlaPrice = 0
            carr.save()
            for i in r:
                
                carr.totlaPrice = carr.totlaPrice + i.price
                carr.save()
            return Response({"message":"deleted"},status=status.HTTP_200_OK)
        except:
            
            return Response({"message":"None id"},status=status.HTTP_200_OK)

class CartView(generics.GenericAPIView):
    serializer_class = CartSerializers11
    permission_classes = [IsAuthenticated , HasAPIKey]

    def get(self, request):
        user = request.user

        cartt = Cart.objects.filter(userCart = user).all()
        s = CartSerializers11(cartt, many=True)
        return Response({"data":s.data}, status=status.HTTP_200_OK)
            
              