from rest_framework import serializers
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model

# Custom User Serializer for Registration
class UserSerializer(serializers.ModelSerializer):
    # Here, CharField() is used for text-based fields like username, email, etc.
    username = serializers.CharField(max_length=150)  # Username field
    email = serializers.EmailField()  # Email field (EmailField is more specific)
    password = serializers.CharField(write_only=True)  # Password field, write-only
    bio = serializers.CharField(required=False, allow_blank=True)  # Optional bio field
    profile_picture = serializers.ImageField(required=False, allow_null=True)  # Optional profile picture

    class Meta:
        model = get_user_model()  # Using the custom user model
        fields = ('username', 'email', 'password', 'bio', 'profile_picture')

    def create(self, validated_data):
        # Create the user instance with the provided validated data
        user = get_user_model().objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        
        # Optionally, handle other fields (e.g., bio, profile_picture) if they exist
        user.bio = validated_data.get('bio', '')
        user.profile_picture = validated_data.get('profile_picture', None)
        user.save()

        # Create a Token for the newly created user
        Token.objects.create(user=user)
        return user
