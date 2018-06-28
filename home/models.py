from django.db import models
from django.core.validators import MaxLengthValidator
from django.utils import timezone
import os

def get_image_path(instance, filename):
        return os.path.join('home','static', 'home', 'images', 'news',str(instance.id), filename)

class News(models.Model):
    title = models.TextField(validators=[MaxLengthValidator(30)], default = 'Title')
    sub_title = models.TextField(validators=[MaxLengthValidator(50)], default = 'Sub-titulo')
    iniciativa_name = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField('date published', default = timezone.now())
    pic = models.ImageField(upload_to = get_image_path, default = 'home/static/home/images/casd.png')
    # def __str__(self):
    #     return self.question_text
    
    def pic_url(self):
        return self.pic.url[4:]
