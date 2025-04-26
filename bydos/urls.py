from django.urls import path, include
from .views import *
from . import views


urlpatterns = [
    path('clients/', ClientList.as_view(), name='client-list'),
    path('team/', TeamList.as_view(), name='team-list'),
    path('testimonails/', TestimonialList.as_view(), name = 'testimonial-list'),
    path('homefaq/', HomeFaqList.as_view(), name='homefaq-list'),
    path('projects/', ProjectListAPIView.as_view(), name='project-list'),
    path('projects/<slug:slug>/', ProjectDetailAPIView.as_view(), name='project-detail'),
    path('contactform/', views.submit_contact_form, name='submit_contact_form'),
    path('services/', ServiceListView.as_view(), name='services-list'),
    path('services/<slug:slug>/', ServiceDetailView.as_view(), name='service-detail'),
    path('blogs/', BlogList.as_view(), name='blog-list'),
    path('blogs/<slug:slug>/', BlogDetail.as_view(), name='blog-detail'),
    path('comments/create/', CommentFormSubmission.as_view(), name='create-blog-comment'),
    path('blogs/<slug:slug>/comments/', ApprovedBlogComments.as_view(), name='blog-comments'),
    path('homeabouts/', HomeAboutsList.as_view(), name='homeabout-list'),
    path('subscribe/', subscribe_view, name='subscribe'),

    # path('explorer/', include('explorer.urls')),


]