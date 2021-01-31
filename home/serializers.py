from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={"input_type": "password"}, write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            password=make_password(validated_data['password']),
        )

        user.save()
        return user

    def validate(self, validated_data):
        # password validation
        password = validated_data.get('password')
        password2 = validated_data.get('password2')

        try:
            validate_password(password)
        except serializers.ValidationError as e:
            raise serializers.ValidationError({'password': e})

        if password != password2:
            raise serializers.ValidationError(
                {'password': "Passwords must match"})

        return validated_data

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email',
                  'password', 'password2', ]
        extra_kwargs = {
            'password': {"write_only": True}
        }
