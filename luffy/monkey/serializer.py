from rest_framework import serializers
from monkey.models import BookInfo

class BookSerializers(serializers.Serializer):
    #主键
    id = serializers.IntegerField()
    #书名
    btitle = serializers.CharField()
    #发布日期
    bpub_date = serializers.DateField()
    #阅读量
    bread = serializers.IntegerField()
    #评论量
    bcomment = serializers.IntegerField()