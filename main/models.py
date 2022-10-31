from django.db import models

# Create your models here.


class Product (models.Model):

    choices = [('mobile', 'Mobile'), ('computers', 'Computers'), ('tv/video', 'TV/Video'),
               ('audio', 'Audio'), ('home', 'Home')]
    product_id = models.CharField('ID', max_length=16, primary_key=True)
    name = models.CharField('Name',  max_length=100)
    price = models.CharField('price', max_length=16)
    category = models.CharField('category', max_length=10, choices=choices)
    image1 = models.ImageField('image1', upload_to='images/')
    image2 = models.ImageField('image2', upload_to='images/')
    image3 = models.ImageField('image3', upload_to='images/')
    anons_fi = models.CharField('anons_fi', max_length=300)
    anons_eng = models.CharField('anons_eng', max_length=300)
    main_description_fi = models.TextField('Main_description_fi')
    main_description_eng = models.TextField('Main_description_eng')
    guaranty = models.CharField('guaranty', max_length=400)
    service_center = models.CharField('service_center', max_length=400)
    size = models.CharField('Size',  max_length=100)
    weight = models.CharField('weight', max_length=100)

    def __str__(self):
        return self.name