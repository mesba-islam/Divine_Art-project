from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    parent = models.ForeignKey('self', related_name='children', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=50,unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    description = models.TextField(max_length=600, blank=True)
    Image =models.ImageField(upload_to ='categories/images', blank=True)

    class Meta:
        verbose_name='category'
        verbose_name_plural ='categories'

    def get_url(self):
            return reverse('products_by_category', args=[self.slug])


    def __str__(self):
        return self.title
