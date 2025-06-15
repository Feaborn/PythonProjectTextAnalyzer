from rest_framework import serializers
from .models import User, Document, Collection
from api.models import Document, Collection


# Регистрация
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        return user


# Авторизация
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


# Обновление пароля
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)


# Коллекции
class CollectionSerializer(serializers.ModelSerializer):
    documents = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Collection
        fields = ['id', 'name', 'documents']


# Документы
class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        #fields = ['id', 'file', 'created_at', 'user']
        fields = ['id', 'file', 'created_at']
        read_only_fields = ['id', 'created_at']


class CollectionCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Collection
        fields = ['name']
