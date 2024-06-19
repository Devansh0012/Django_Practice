from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class chaiVariety(models.Model):
    CHAI_TYPE_CHOICE = [
        ('ML', 'Masala'),
        ('GC', 'Ginger'),
        ('CC', 'Cardamom'),
        ('KC', 'Kashmiri'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPE_CHOICE, default='ML')
    description = models.TextField(default='')
    price = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
# One to Many relationship

class ChaiReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    chai = models.ForeignKey(chaiVariety, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    rating = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f'{self.user.username} - {self.chai.name} - {self.rating}'
    
# Many to Many relationship

class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varities = models.ManyToManyField(chaiVariety, related_name='stores')
    
    def __str__(self):
        return self.name
    
# One to One relationship

class chaiCertificate(models.Model):
    chai = models.OneToOneField(chaiVariety, on_delete=models.CASCADE, related_name='certificate')
    certificate_number = models.CharField(max_length=100)
    issue_date = models.DateTimeField(default=timezone.now)
    valid_till = models.DateTimeField()
    
    def __str__(self):
        return f'Certificate for {self.chai.name} - {self.certificate_number}'