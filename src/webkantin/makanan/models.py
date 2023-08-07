from django.db import models

class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='menu_images/')
    price = models.IntegerField()
    NamaKantin = models.ManyToManyField('NamaKantin')
    
    def __str__(self):
        return self.name

class NamaKantin(models.Model):
    name = models.CharField(max_length=100)
    deskripsi = models.TextField()
    image = models.ImageField(upload_to='kantin_images/')
    
    def __str__(self):
        return self.name

    
class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField()
    items = models.ManyToManyField('MenuItem', related_name='order', blank=True)
    name = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I: %M %p")}'
