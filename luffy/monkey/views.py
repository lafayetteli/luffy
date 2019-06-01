from django.shortcuts import render
from django.views import View
from .models import BookInfo
from .serializer import BookSerializers
import json
from django.http import JsonResponse
from django.http import Http404
class BooksView(View):
    def get(self,request):
        book_list = BookInfo.objects.all()
        # book_dict_list = []
        # for book in book_list:
        #      book_dict_list.append({
        #          'id': book.id,
        #          'btitle': book.btitle,
        #          'bpub_date': book.bpub_date
        #     })
        book_serializer = BookSerializers(book_list,many=True)
        book_dict_list = book_serializer.data
        return JsonResponse(book_dict_list,safe=False)
    def post(self,request):
        param_dict = json.loads(request.body.decode())
        btitle = param_dict.get('btitle')
        bpub_date = param_dict.get('bpub_date')
        book = BookInfo.objects.create(btitle=btitle,bpub_date=bpub_date)
        book_serializer = BookSerializers(book)
        book_dict=book_serializer.data

        # book_dict = {
        #     'id':book.id,
        #     'btitle':book.btitle,
        #     'bpub_date':book.bpub_date
        # }
        return JsonResponse(book_dict,status=201)

class BookView(View):
    def get(self,request,pk):
        try:
            book = BookInfo.objects.get(pk=pk)
        except:
            return Http404('数据不存在')
        # book_dict = {
        #     'id': book.id,
        #     'btitle':book.btitle,
        #     'bpub_date':book.bpub_date
        # }
        book_serializer = BookSerializers(book)
        book_dict = book_serializer.data
        return JsonResponse(book_dict)
    def put(self,requset,pk):
        param_dict = json.loads(requset.body.decode())
        btitle = param_dict.get('btitle')
        bpub_date = param_dict.get('bpub_date')
        book = BookInfo.objects.get(pk=pk)
        book.btitle = btitle
        book.bpub_date = bpub_date
        book.save()
        # book_dict = {
        #     'id':book.id,
        #     'btitle':book.btitle,
        #     'bpub_date':book.bpub_date
        # }
        book_serializer = BookSerializers(book)
        book_dict=book_serializer.data
        return JsonResponse(book_dict)
    def delete(self,request,pk):
        book = BookInfo.objects.get(pk=pk)
        book.delete()
        return JsonResponse({},status=204)
