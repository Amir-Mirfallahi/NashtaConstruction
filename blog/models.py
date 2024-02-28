from django.db import models
from tinymce import models as tmodels
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=248)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=512)
    slug = models.SlugField(max_length=256, unique=True)
    image = models.ImageField(upload_to='blog/images')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    publish_date = models.DateTimeField(auto_now_add=True)
    views = models.IntegerField(default=0)
    content = tmodels.HTMLField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    time_to_read = models.IntegerField(default=0, help_text="How much time does it take to read the post?(in min)")

    @property
    def get_date(self):
        return self.publish_date.strftime('%d %b')

    def __str__(self):
        return self.title
