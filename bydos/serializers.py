from rest_framework import serializers
from .models import *

class ClientsSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Clients
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = '__all__'

class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = "__all__"

class HomeFaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeFaq
        fields="__all__"
    
class ProjectSerializer(serializers.ModelSerializer):
    formatted_starting_date = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = '__all__'

    def get_formatted_starting_date(self, obj):
        return obj.formatted_starting_date

class ServiceFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceFAQ
        fields = ['question', 'answer']

class ServiceSerializer(serializers.ModelSerializer):
    faqs = ServiceFAQSerializer(many=True, read_only=True)

    class Meta:
        model = Service
        fields = [
            'id','slug', 'service_name', 'thumbnail_image', 'icon_image', 'banner_image',
            'title_main', 'desc', 'title_2', 'desc_2', 'title_3', 'desc_3', 'title_4', 'desc_4', 'faqs'
        ]

class BlogSerializer(serializers.ModelSerializer):
    formatted_date = serializers.ReadOnlyField()

    class Meta:
        model = Blog
        fields = ['id', 'title', 'slug', 'image', 'author', 'formatted_date', 'category', 'tags', 'short_description', 'content']

class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = ['name', 'email', 'website', 'message', 'blog']
        read_only_fields = ['approved', 'created_at'] 

class HomeAboutsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeAbouts
        fields =['id', 'title', 'desc','image']

class SubscribeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscribe
        fields = ['id', 'email']

class ContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactForm
        fields = ['id', 'name','email', 'message', 'phone_number', 'website', ]