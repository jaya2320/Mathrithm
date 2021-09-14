from rest_framework import serializers
from django.contrib.auth.models import User

class AllUser(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class particularuser(serializers.ModelSerializer):
    def get_user(self,obj):
        user_id=obj.id
        user=User.objects.get(id=user_id)
        return{
            'user_id':user.id,
            'user_username':user.username,
            'user_email':user.email
        }

    user= serializers.SerializerMethodField()
    class Meta:
        model=User
        fields=['user']
