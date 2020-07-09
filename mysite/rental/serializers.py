from rest_framework import serializers
from datetime import datetime
from . import models



class BorrowedSerializer(serializers.ModelSerializer):
    # what = BelongingSerializer(read_only=True)
    # to_who = FriendSerializer(read_only=True)
    class Meta:
        model = models.Borrowed
        # fields = '__all__'
        # fields = ('pk', 'what', 'to_who', 'when', 'returned')
        fields = ('what', 'to_who', 'when', 'returned')
        depth = 1

class FriendSerializer(serializers.ModelSerializer):
    borrowedfriend = BorrowedSerializer(many=True,read_only=True)
    class Meta:
        model = models.Friend
        # fields = ('pk', 'name','borrowedfriend')
        fields = ('name','borrowedfriend')

class BelongingSerializer(serializers.ModelSerializer):
    borrowedbelonging = BorrowedSerializer(many=True,read_only=True)
    class Meta:
        model = models.Belonging
        # fields = ('pk', 'name','borrowedbelonging')
        fields = ('name','borrowedbelonging')


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Movie
        # fields = ('pk','created','name', 'category')
        fields = ('pk', 'name')

class CategorySerializer(serializers.HyperlinkedModelSerializer):

    movies = MovieSerializer(many=True, read_only=True)
    class Meta:
        model = models.Category
        # fields = ('pk','created','name', 'movies')
        fields = ('url','pk','created','name', 'movies')
        

class UserSerializer(serializers.ModelSerializer):
    """ Serializer a user object """
    
    class Meta:
        model = models.User
        fields = ('pk','email', 'password')
        extra_kwargs = {
         'password' : {
             'write_only' : True,
             'style' : {'input_type' : 'password'}
         }
        }

    def create(self, validated_data):
        """ create and return new user """
        user = models.User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password']
            )
        return user


