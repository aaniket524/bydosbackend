from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.decorators import permission_classes
from rest_framework.decorators import api_view



from rest_framework.response import Response

# Create your views here.
from .models import *
from .serializers import *


class HomeAboutsList(APIView):
    def get(self, request):
        homeabout = HomeAbouts.objects.all().order_by('id')
        serializer = HomeAboutsSerializer(homeabout, many = True)
        return Response(serializer.data)

class ClientList(APIView):
    def get(self, request):
        clients = Clients.objects.all().order_by('id') 
        serializer = ClientsSerializer(clients, many= True)
        return Response(serializer.data)

class TeamList(APIView):
    def get(self, request):
        team = Team.objects.all().order_by('id')
        serializer = TeamSerializer(team, many = True)
        return Response(serializer.data)

class TestimonialList(APIView):
   def get(self, request):
    testimonails = Testimonial.objects.all().order_by('id')
    serializer = TestimonialSerializer(testimonails, many=True)
    return Response(serializer.data)

class HomeFaqList(APIView):
    def get(self, request):
        homefaq = HomeFaq.objects.all().order_by('id')
        serializer = HomeFaqSerializer(homefaq, many= True)
        return Response(serializer.data)

class ProjectListAPIView(generics.ListAPIView):
    queryset = Project.objects.all().order_by('-id')
    serializer_class = ProjectSerializer

class ProjectDetailAPIView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    lookup_field = 'slug'
class ServiceListView(APIView):
    def get(self, request):
        services = Service.objects.all().order_by('id')
        serializer = ServiceSerializer(services, many=True)
        return Response(serializer.data)

class ServiceDetailView(APIView):
    def get(self, request, slug):
        try:
            service = Service.objects.get(slug=slug)
            serializer = ServiceSerializer(service)
            return Response(serializer.data)
        except Service.DoesNotExist:
            return Response({'error': 'Service not found'}, status=404)

# List all blogs
class BlogList(APIView):
    def get(self, request):
        blogs = Blog.objects.all().order_by('-id')
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)

# Get blog by slug
class BlogDetail(APIView):
    def get(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        serializer = BlogSerializer(blog)
        return Response(serializer.data)

# Get approved comments for blog
class ApprovedBlogComments(APIView):
    def get(self, request, slug):
        blog = get_object_or_404(Blog, slug=slug)
        comments = BlogComment.objects.filter(blog=blog, approved=True).order_by('-created_at')
        serializer = BlogCommentSerializer(comments, many=True)
        return Response(serializer.data)

class CommentFormSubmission(APIView):
    def post(self, request):
        # Deserialize the incoming data
        serializer = BlogCommentSerializer(data=request.data)

        if serializer.is_valid():
            # Save the comment data to the database
            serializer.save()
            return Response({"message": "Comment submitted successfully!"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def subscribe_view(request):
    if request.method == 'POST':
        email = request.data.get('email')
        
        if not email:
            return Response({'error': 'Email is required'}, status=status.HTTP_400_BAD_REQUEST)

        # Save email to database
        Subscribe.objects.create(email=email)
        return Response({'message': 'Subscribed successfully!'}, status=status.HTTP_201_CREATED)

def submit_contact_form(request):
    if request.method == 'POST':
        serializer = ContactFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Message submitted successfully!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Method Not Allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)