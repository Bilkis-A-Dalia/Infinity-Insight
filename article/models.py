from django.db import models
from user.models import Editors,Viewers
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=30)

    def __str__(self):
        return self.name
    
class Article(models.Model):
    editor = models.ForeignKey(Editors,on_delete=models.CASCADE)
    headline = models.CharField(max_length=100)
    body = models.TextField()
    category = models.ManyToManyField(Category)
    publishing_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to= 'article/images/')
    
    def __str__(self):
        return f'{self.editor.User.username} {self.headline}'

STAR_CHOICES=[
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐')
]
class Review(models.Model):
    reviewer = models.ForeignKey(Viewers,on_delete=models.CASCADE)
    article=models.ForeignKey(Article, on_delete=models.CASCADE)
    body = models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    rating=models.CharField(max_length=10,choices=STAR_CHOICES)

    def __str__(self) -> str:
        return f'Reviews : {self.reviewer.User.first_name} : {self.article.headline}'
