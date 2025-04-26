from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Clients(models.Model):
    title= models.CharField(max_length=100)
    image = models.ImageField(upload_to='clients/')

    def __str__(self):
        return self.title

#for team data

class Team(models.Model):
    image = models.ImageField(upload_to='team/')
    name = models.CharField(max_length=50)
    prof = models.CharField(max_length=50)
    fburl = models.URLField(blank=True, null=True)
    linkdinurl = models.URLField(blank=True, null=True)
    twitterurl = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

#testimonails home

class Testimonial(models.Model):
    image = models.ImageField(upload_to='testimonials/')
    name = models.CharField(max_length=50)
    prof = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.name

class HomeFaq(models.Model):
    ques = models.CharField(max_length=350)
    ans = models.CharField(max_length=1000)

    def __str__(self):
        return self.ques
class Project(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True,  null=True)
    thumbnail = models.ImageField(upload_to='projects/thumbnails/')
    banner_image = models.ImageField(upload_to='projects/banners/')
    banner_image1 = models.ImageField(upload_to='projects/banners/', blank=True, null=True)
    banner_image2 = models.ImageField(upload_to='projects/banners/', blank=True, null=True)
    client = models.CharField(max_length=100, blank=True, null=True)
    handler_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)  # fixed typo here
    starting_date = models.DateField(blank=True, null=True)
    time_duration = models.CharField(max_length=100)
    website_url = models.URLField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    projectoverview = RichTextField()
    report_analyis = RichTextField()
    result = RichTextField()

    def __str__(self):
        return self.title

    @property
    def formatted_starting_date(self):
        if self.starting_date:
            return self.starting_date.strftime('%d %b, %Y')
        return ''

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Project, self).save(*args, **kwargs)


class Service(models.Model):
    service_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True) 

    thumbnail_image = models.ImageField(upload_to='services/thumbnails/')
    icon_image = models.FileField(upload_to='services/icons/')
    banner_image = models.FileField(upload_to='services/banners/')

    title_main = models.CharField(max_length=200)
    desc = RichTextField()
    
    title_2 = models.CharField(max_length=200, blank=True, null=True)
    desc_2 = RichTextField(blank=True, null=True)

    title_3 = models.CharField(max_length=200, blank=True, null=True)
    desc_3 = RichTextField(blank=True, null=True)

    title_4 = models.CharField(max_length=200, blank=True, null=True)
    desc_4 = RichTextField(blank=True, null=True)

    def __str__(self):
        return self.service_name
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.service_name)
        super(Service, self).save(*args, **kwargs)
    
class ServiceFAQ(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name='faqs')
    question = models.CharField(max_length=255)
    answer = RichTextField()

    def __str__(self):
        return f"FAQ for {self.service.service_name}"


class Blog(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='blogs/images/')
    author = models.CharField(max_length=100, default='Editor Team')  # fixed name
    date = models.DateField(auto_now_add=True)  # creation date
    category = models.CharField(max_length=100)
    tags = models.CharField(max_length=200, help_text='Separate tags with commas')
    short_description = RichTextField()  # for card + first para
    content = RichTextField()  # full blog content

    def __str__(self):
        return self.title

    @property
    def formatted_date(self):
        return self.date.strftime('%d %b, %Y') 

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Blog, self).save(*args, **kwargs)


class BlogComment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    website = models.CharField(max_length=200, null= True)
    email = models.EmailField(blank=True, null=True)
    message = RichTextField()
    approved = models.BooleanField(default=False)  # Only show approved comments
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.name} on {self.blog.title}'


class HomeAbouts(models.Model):
    title= models.CharField(max_length=100)
    image = models.FileField(upload_to='about/icons/')
    desc = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Subscribe(models.Model):
    email = models.EmailField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
          return f"{self.email} - {self.submitted_at}"

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    website = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.name} - {self.email}"
    class Meta:
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

