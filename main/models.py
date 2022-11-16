from django.db import models
from django.utils import timezone


# Create your models here.

class ProductCategory(models.Model):
    choices = [('main', 'Main'), ('mobile', 'Mobile'), ('computers', 'Computers'), ('laptops', 'Laptops'),
               ('tv/video', 'TV/Video'), ('audio', 'Audio'), ('home tech', 'Home tech'), ('children', 'Children')]
    category_id = models.CharField('Category id', max_length=16, primary_key=True)
    category_name = models.CharField('Category name', max_length=100)
    parent_category = models.CharField('Parent category', max_length=100, choices=choices)

    def __str__(self):
        return self.category_name + ' (' + self.parent_category+')'


class Product (models.Model):

    product_id = models.CharField('ID', max_length=16, primary_key=True)
    name = models.CharField('Name',  max_length=100)
    price = models.CharField('price', max_length=16)
    category_id = models.ForeignKey(ProductCategory, on_delete=models.PROTECT, null=True)
    image1 = models.ImageField('image1',  null=True, blank=True, upload_to='images/')
    image2 = models.ImageField('image2', null=True, blank=True, upload_to='images/')
    image3 = models.ImageField('image3', null=True, blank=True, upload_to='images/')
    main_feature1 = models.CharField('main_feature1',  max_length=200)
    main_feature2 = models.CharField('main_feature2', max_length=200)
    main_feature3 = models.CharField('main_feature3', max_length=200)
    anons_eng = models.CharField('anons_eng', max_length=300)
    main_description_name1 = models.CharField('Main_description_name1', max_length=400)
    main_description1 = models.TextField('Main_description1')
    main_description_name2 = models.CharField('Main_description_name2', max_length=400)
    main_description2 = models.TextField('Main_description2')
    main_description_name3 = models.CharField('Main_description_name3', max_length=400)
    main_description3 = models.TextField('Main_description3')
    technical_description_name1 = models.CharField('technical_description_name1', max_length=400)
    technical_description1 = models.TextField('technical_description1')
    technical_description_name2 = models.CharField('technical_description_name2', max_length=400)
    technical_description2 = models.TextField('technical_description2')
    technical_description_name3 = models.CharField('technical_description_name3', max_length=400)
    technical_description3 = models.TextField('technical_description3')
    guaranty = models.CharField('guaranty', max_length=400)
    service_center = models.CharField('service_center', max_length=400)
    size = models.CharField('Size',  max_length=100)
    size_with_package = models.CharField('size_with_package', max_length=100)
    weight = models.CharField('weight', max_length=100)
    weight_with_package = models.CharField('weight_with_package', max_length=100)
    package_include = models.CharField('package_include', max_length=300)
    date_added = models.DateTimeField('date_added', default=timezone.now)
    last_update = models.DateTimeField('last_update', default=timezone.now)

    def __str__(self):
        return self.name
