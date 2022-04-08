from django.conf import settings
from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    
    #customer manager
    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')
    
    #select options
    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    
    # not allow deleting category
    category = models.ForeignKey(Category, on_delete=models.PROTECT, default=1)
    title = models.CharField(max_length=250)
    excerpt = models.TextField(null=True)
    content = models.TextField()
    slug = models.CharField(max_length=250, unique_for_date='published') #use slug to identify
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='blog_posts')
    status = models.CharField(max_length=10, choices=options, default='published')
    objects = models.Manager() # default manager
    postobjects = PostObjects() # custom manager
    
    #return descending order
    class Meta:
        ordering = ('-published',)
        
    def __str__(self):
        return self.title