from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from usersApp.models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','emailEstudiante','password','nombresEstudiante','apellidosEstudiante')
    
    def create(self,validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','emailEstudiante','nombresEstudiante','apellidosEstudiante')

class PasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=128, min_length=6, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=6, write_only=True)

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError(
                {'password':'Debe ingresar ambas contraseñas iguales'}
            )
        return data

class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User

    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'nombresEstudiante': instance['nombresEstudiante'],
            'apellidosEstudiante': instance['apellidosEstudiante'],
            'username': instance['username'],
            'emailEstudiante': instance['emailEstudiante']
        }