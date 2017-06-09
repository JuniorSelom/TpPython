from rest_framework import serializers
from django.contrib.auth.models import User, Group
from .models import UserInformation, Drink, Cocktail, Queue, Video


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username','password', 'email')


class UserInformationSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserInformation
        fields = ('id', 'coin', 'user')

    def create(self, validated_data):
        print(validated_data)

        djuser = User.objects.create(username=validated_data["user"]["username"], password=validated_data["user"]["password"],email=validated_data["user"]["email"])

        user = UserInformation.objects.create(coin=validated_data["coin"], user=djuser)

        return user


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('id', 'url', 'name')


class DrinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Drink
        fields = ('id', 'name', 'type')


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'url', 'cocktail')


class SimpleVideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'url')


class CocktailSerializer(serializers.ModelSerializer):
    drinks = serializers.PrimaryKeyRelatedField(many=True,queryset=Drink.objects.all())
    video = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Cocktail
        fields = ('id', 'name', 'drinks', 'video')


class CocktailSerializerGet(serializers.ModelSerializer):
    drinks = DrinkSerializer(many=True, read_only=True)
    video = SimpleVideoSerializer(read_only=True)

    class Meta:
        model = Cocktail
        fields = ('id', 'name', 'drinks', 'video')


class QueueSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Queue
        fields = ('id', 'user', 'cocktail', 'mode', 'date')


