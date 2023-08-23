from rest_framework import serializers
from dj_rest_auth.models import TokenModel
from dj_rest_auth.serializers import UserDetailsSerializer


class CurrentUserSerializer(UserDetailsSerializer):
    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields


class TokenSerializer(serializers.ModelSerializer):
    """
    Serializer for Token model.
    """
    user = CurrentUserSerializer(many=False, read_only=True)

    class Meta:
        model = TokenModel
        fields = ('key', 'user', 'refresh_token')