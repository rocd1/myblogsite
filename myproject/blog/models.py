from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    content = models.TextField()
    image = models.ImageField(upload_to='blog_images', default='default_image.jpg')
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} - {self.pub_date}'


    class Meta:
        ordering = ('-pub_date',)
