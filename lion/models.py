from django.db import models

# Create your models here.


class Person(models.Model):
    name = models.CharField(max_length=50,verbose_name='İsim Soyisim')
    nat_id = models.CharField(max_length=11,verbose_name='TC No')
    birth_date = models.CharField(max_length=12,verbose_name='Doğum Tarihi')
    seri_no = models.CharField(max_length=20,verbose_name='Seri Numara')
    created_date = models.DateTimeField(auto_now_add=True,verbose_name='İsim Soyisim')
    def __str__(self):
        return self.name
