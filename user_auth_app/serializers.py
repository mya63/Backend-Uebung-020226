from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.Serializer):
  username = serializers.CharField()
  email = serializers.EmailField(required=False)
  password = serializers.CharField(write_only=True)
  repeated_password = serializers.CharField(write_only=True)


  def validate(self, data):
      if data["password"] != data["repeated_password"]:
        raise serializers.ValidationError("Passwörter stimmen nicht überein.")
      return data
    
  def create(self, validated_data):
      validated_data.pop("repeated_password")

      user = User.objects.create_user(
        username=validated_data["username"],
        email=validated_data.get("email", ""),
        password=validated_data["password"],
      )

      Token.objects.create(user=user)
      return user 