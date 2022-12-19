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
    permission_classes = [IsAuthenticated]
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
            user = request.user
            d.myCourseIcon = False
            d.save()
            ls = CartItem.objects.filter(userCartItem = user).all()
            for op in ls:
                op.Courses.cartIcon = False
                op.Courses.save()
            

            if user in d.users.all():
                d.myCourseIcon = True
                d.save()
            else:
                d.myCourseIcon = False
                d.save()
            serializers = CatCourseSerializers(d)
            
        else:
            d = CatCourses.objects.filter(star = True).filter(active = True).all()
            user = request.user
            
            
            
                
                
            for i in d:
                if user in i.users.all():
                    i.myCourseIcon = True
                    i.cartIcon = False
                    if CartItem.objects.filter(Courses = i).filter(userCartItem = user).exists():
                        i.cartIcon = True
                    i.save()


                    
                else:
                    i.myCourseIcon = False
                    i.cartIcon = False
                    
                    if CartItem.objects.filter(Courses = i).filter(userCartItem = user).exists():
                        i.cartIcon = True
                    i.save
            
                
            serializers = CatCourseSerializers(d , many=True)
        return Response({"data":serializers.data},status=status.HTTP_200_OK)

class CoursesViews(generics.GenericAPIView):
    serializer_class = YearSerializerswithCatCourses
    permission_classes = [AllowAny]
    def get(self,request):
        if request.query_params:
                            
            id1 = request.query_params['CollegeId']
            d = year.objects.filter(college = id1).all()
            serializers = yearSerializers(d, many = True)
            try:
                if request.query_params:
                    ii = request.query_params['YearId']
                    oo = request.query_params['Term']
                    yy = CatCourses.objects.filter(year = ii)
                    user = request.user
                    oooo = yy.filter(term = oo).filter(active = True).all()
                    for i in oooo:
                        if user in i.users.all():
                            i.myCourseIcon = True
                            i.cartIcon = False
                            if CartItem.objects.filter(Courses = i).filter(userCartItem = user).exists():
                                i.cartIcon = True
                            i.save()
                        else:
                            i.myCourseIcon = False
                            i.cartIcon = False
                            if CartItem.objects.filter(Courses = i).filter(userCartItem = user).exists():
                                i.cartIcon = True
                            i.save()
                    serializers = CatCourseSerializers(oooo, many = True)
                    

                    try:
                        if request.query_params:
                            iii = request.query_params['CourseId']
                            ll = CatCourses.objects.get(id = iii)

                            for i in ll:
                                if user in i.users.all():
                                    i.myCourseIcon = True
                                    i.cartIcon = False
                                    if CartItem.objects.filter(Courses = i).filter(userCartItem = user).exists():
                                        i.cartIcon = True
                                    i.save()

                                else:
                                    i.myCourseIcon = False
                                    i.cartIcon = False
                                    if CartItem.objects.filter(Courses = i).filter(userCartItem = user).exists():
                                        i.cartIcon = True
                                    i.save()
                            serializers = CatCourseSerializers(ll)
                            
                        
                    except:
                        pass
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
            
class MyCoursesView(generics.GenericAPIView):
    serializer_class = CatCourseSerializers
    permission_classes = [IsAuthenticated, HasAPIKey]
    def get(self,request):
        user = request.user
        if request.query_params:
            pp = request.query_params['CourseId']
            y = CatCourses.objects.get(id = pp)
            serializers = CatWithvideSerializers(y)
            try:
                if request.query_params:
                    ll = request.query_params['VideoId']
                    yy = Courses.objects.get(id = ll)
                    serializers = CourseSerializers(yy)
            except:
                pass
        else:
            d = CatCourses.objects.filter(users = user).all()
            serializers = CatCourseSerializers(d , many = True)
        return Response({"data":serializers.data},status=status.HTTP_200_OK)

    
class BanarsView(generics.GenericAPIView):
    serializer_class = BannarsSerializers
    permission_classes = [IsAuthenticated, HasAPIKey]
    def get (self , request):
        qq = Banars.objects.all()
        serializers = self.serializer_class(qq , many = True)
        return Response({"data":serializers.data},status=status.HTTP_200_OK)

class RecomendedView(generics.GenericAPIView):
    serializer_class = CatCourseSerializers
    permission_classes = [IsAuthenticated, HasAPIKey]
    def get (self , request):
        user = request.user
        if request.query_params:
            pp = request.query_params['CourseId']
            yy = CatCourses.objects.get(id = pp)
            if user in yy.users.all():
                yy.myCourseIcon = True
                yy.cartIcon = False
                if CartItem.objects.filter(Courses = yy).filter(userCartItem = user).exists():
                    yy.cartIcon = True
                yy.save()
            else:
                yy.myCourseIcon = False
                yy.cartIcon = False
                if CartItem.objects.filter(Courses = yy).filter(userCartItem = user).exists():
                    yy.cartIcon = True
                yy.save()
            serializers = self.serializer_class(yy)
        else:
            ll = CatCourses.objects.filter(year = user.year).filter(active = True).all()
            for i in ll:
                if user in i.users.all():
                    i.myCourseIcon = True
                    i.cartIcon = False
                    if CartItem.objects.filter(Courses = i).filter(userCartItem = user).exists():
                        i.cartIcon = True
                    i.save()
                    
                else:
                    i.myCourseIcon = False
                    i.cartIcon = False
                    if CartItem.objects.filter(Courses = i).filter(userCartItem = user).exists():
                        i.cartIcon = True
                    i.save()
            serializers = self.serializer_class(ll, many = True)
        return Response({"data":serializers.data}, status= status.HTTP_200_OK)