from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User
from rest_framework.response import Response

#using plain serializer
# class ProfileSerializer(serializers.Serializer):
#     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
#     bio = serializers.CharField(max_length=500)
#     location = serializers.CharField(max_length=50)
#     birth_date = serializers.DateField()

#     class Meta:
#         fields = ('user', 'bio', 'location', 'birth_date')


#     def create(self, validated_data):
#         user = validated_data['user']
#         bio = validated_data['bio']
#         location = validated_data['location']
#         birth_date = validated_data['birth_date']

#         obj = Profile.objects.create(user=user, bio=bio, location=location, birth_date=birth_date)
#         return Response(obj)

#Using modelserializer
class UserCreateReadSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = ('username', 'email','password' )
        extra_kwargs={
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        username=validated_data['username']
        email = validated_data['email']
        password = validated_data['password']
        user = User.objects.create_user(username=username, email=email, password=password)
        return user

class ProfileSerializer(serializers.ModelSerializer):
    user = UserCreateReadSerializer()
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'location', 'birth_date')

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_serializer = UserCreateReadSerializer(data=user_data)
        user_serializer.is_valid(raise_exception=True)
        user = user_serializer.save()

        profile = Profile.objects.create(user=user, **validated_data)
        return profile