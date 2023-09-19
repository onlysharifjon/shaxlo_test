from rest_framework import serializers
from .models import  News #Admins,

# class AdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Admins
#         fields = "__all__"

# class OneAdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Admins
#         fields = ("name", )

# class PlaceAdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Admins
#         fields = ("place", )

# class CategoryAdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Admins
#         fields = ('job_category',)

class NewsSerializer(serializers.ModelSerializer):
    full_image_url = serializers.SerializerMethodField()
    class Meta:
        model = News
        fields = "__all__"
        
    def get_full_image_url(self, obj):
        domain_name = "taknews-backend.uz"
        relative_image_url = obj.field.url if obj.field else None
        if relative_image_url:
            return f"http://{domain_name}{relative_image_url}"
        else:
            return None


class PlaceNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ("place", 'language')

class CategoryNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('category', 'language')

# class OneNewsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = News
#         fields = ('id', )   KERAK EMAS

# class AdminLoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Admins
#         fields = ('username', 'password')