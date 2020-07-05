from django.contrib.auth.models import User                                                       
from rest_framework import serializers
from . import models


#class UserSerializeri(serializers.ModelSerializer):
#    class Meta:
#        model = models.User
#        fields = ('id','email','active','staff','admin')


   #class UserViewset(viewsets.ModelViewSet):                                                         
   #    queryset = models.User.objects.all()                                                         
   #    serializers_class = serializers.UserSerializer                                               
class UserSerializer(serializers.ModelSerializer):                                              
   #snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())    
    class Meta:                                                                                   
        model = User                                                                              
        fields = ['id','email','active','staff','admin']                                          
                      

class FriendSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Friend
        fields = ('id','name')

class BelongingSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Belonging
        fields = ('id','name')

class BorrowedSerializer(serializers.ModelSerializer):
    #nest friends and Belongings inside of the borrowed
    to_who = FriendSerializer(read_only=True)
    what = BelongingSerializer(read_only=True)
    class Meta:
        model = models.Borrowed
        fields = ('pk', 'what', 'to_who', 'when')
        # depth = 1


