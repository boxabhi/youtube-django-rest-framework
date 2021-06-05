from home.helpers import save_pdf
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
import datetime


from rest_framework import generics



class StudentGeneric(generics.ListAPIView , generics.CreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentGeneric1(generics.UpdateAPIView , generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    lookup_field = 'id'



class GeneratePdf(APIView):
    def get(self , request):
        student_objs = Student.objects.all()
        params = {
            'today' : datetime.date.today(),
            'student_objs' : student_objs 
        } 
        file_name , status = save_pdf(params)

        if not status:
            return Response({'status' : 400})



        return Response({'status' : 200 , 'path' : f'/media/{file_name}.pdf'})

















@api_view(['GET'])
def get_book(request):
    book_objs = Book.objects.all()
    serializer = BookSerializer(book_objs , many=True)
    return Response({'status' : 200 , 'payload' : serializer.data})
    

from rest_framework_simplejwt.tokens import RefreshToken
    
class RegisterUser(APIView):
    def post(self , request):
        serializer = UserSerializer(data = request.data)

        if not serializer.is_valid():
            return Response({'status' : 403 ,'errors' : serializer.errors , 'messge' : 'Something went wrong'})
            
        serializer.save()  

        user = User.objects.get(username = serializer.data['username'])
        refresh = RefreshToken.for_user(user)
        
        
        return Response({'status' : 200 ,
        'payload' : serializer.data,
        'refresh': str(refresh),
        'access': str(refresh.access_token), 'messge' : 'your data is saved'})

        

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class StudentAPI(APIView):
    authentication_classes = [ JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        student_objs = Student.objects.all()
        serializer = StudentSerializer(student_objs , many=True)
        print(request.user)
        return Response({'status' : 200 , 'payload' : serializer.data})
       
    def post(self, request):
        serializer = StudentSerializer(data = request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status' : 403 ,'errors' : serializer.errors , 'messge' : 'Something went wrong'})
            
        serializer.save()   
        return Response({'status' : 200 , 'payload' : serializer.data , 'messge' : 'your data is saved'})

   
    def put(self, request):
        pass
    
    def patch(self,request):
        try:
            student_obj = Student.objects.get(id = request.data['id'])
            serializer = StudentSerializer(student_obj , data = request.data , partial =True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status' : 403 ,'errors' : serializer.errors , 'messge' : 'Something went wrong'})
                
            serializer.save()   
            return Response({'status' : 200 , 'payload' : serializer.data , 'messge' : 'your data is updated'})

        except Exception as e:
            print(e)
            return Response({'status' :403 , 'message' : 'invalid id'})
   
    def delete(self, request):
        try:
            id = request.GET.get('id')
            student_obj = Student.objects.get(id = id)    
            student_obj.delete()
            return Response({'status' : 200, 'message' : 'deleted'})
    
        except Exception as e:
            print(e)
            return Response({'status' :403 , 'message' : 'invalid id'})
        
            

    



# @api_view(['GET'])
# def home(request):
#     student_objs = Student.objects.all()
#     serializer = StudentSerializer(student_objs , many=True)
#     return Response({'status' : 200 , 'payload' : serializer.data})

# @api_view(['POST'])
# def post_student(request):
#     serializer = StudentSerializer(data = request.data)
    

#     if not serializer.is_valid():
#         print(serializer.errors)
#         return Response({'status' : 403 ,'errors' : serializer.errors , 'messge' : 'Something went wrong'})
        
#     serializer.save()   
#     return Response({'status' : 200 , 'payload' : serializer.data , 'messge' : 'your data is saved'})

# @api_view(['PUT'])
# def update_student(request , id):
#     try:
    
#         student_obj = Student.objects.get(id = id)
        
#         serializer = StudentSerializer(student_obj , data = request.data , partial =True)
#         if not serializer.is_valid():
#             print(serializer.errors)
#             return Response({'status' : 403 ,'errors' : serializer.errors , 'messge' : 'Something went wrong'})
            
#         serializer.save()   
#         return Response({'status' : 200 , 'payload' : serializer.data , 'messge' : 'your data is saved'})

#     except Exception as e:
#         print(e)
#         return Response({'status' :403 , 'message' : 'invalid id'})


# @api_view(['DELETE'])
# def delete_student(request): 
#     try:
#         id = request.GET.get('id')
#         student_obj = Student.objects.get(id = id)    
#         student_obj.delete()
#         return Response({'status' : 200, 'message' : 'deleted'})
    
#     except Exception as e:
#         print(e)
#         return Response({'status' :403 , 'message' : 'invalid id'})
    


    


    
    
    
    
django pdf generator | django generate pdf from html | django generate pdf from view | django generate pdf report | django generate pdf from model | django generate pdf from template | django generate pdf dynamically | django pdf creation | pdf generator for django | pdf generator in django | django generate pdf invoice | 

django generate pdf from html,
generate pdf from html in django,
django create pdf from html,

What you will learn - 
    - How to generate dyamic PDF django
    - Django generate pdf from html
    - Django generate pdf from view
    - How you can  generate pdf report 
    - How you can  generate pdf from template
    - How to generate pdf dynamically 
    - How you can save PDF in django
