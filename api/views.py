from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Document , SendMessage
from .serializers import DocumentSerializer,TextSerializer,GroqResSerializer
from django.http import JsonResponse
import json
from pypdf import PdfReader
class DocumentUploadView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = DocumentSerializer(data=request.data)
        if serializer.is_valid():
            file = request.FILES['file']
            if file.size < 1024*1024:
                serializer.save()
                pdf_file_obj = file.open('rb')
                reader = PdfReader(pdf_file_obj)
                text = ""
                for page in reader.pages:
                    text += page.extract_text() + "\n"
                data = SendMessage(text)
               # gSerializer= GroqResSerializer(data=data)
                #gSerializer.save()
                print(data)
                return Response(data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class ReceiveData(APIView):
    def post(self, request):
        serializer = TextSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = request.data.get('text')

            res = SendMessage(data)
            return Response(res, status=status.HTTP_201_CREATED)
            # gSerializer= GroqResSerializer(data=res)
            # if gSerializer.is_valid():
            #     gSerializer.save()
            #     return Response(res, status=status.HTTP_201_CREATED)
            # return Response(gSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
