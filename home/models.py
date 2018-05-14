from django.db import models
from django.core.validators import MaxLengthValidator
import os

def get_image_path(instance, filename):
        return os.path.join('static', 'home', 'images', 'news',str(instance.id), filename)

# Create your models here.
class News(models.Model):
    

    title = models.TextField(validators=[MaxLengthValidator(30)], default = 'Title')
    sub_title = models.TextField(validators=[MaxLengthValidator(50)], default = 'Sub-titulo')
    iniciativa_name = models.CharField(max_length=100)
    text = models.TextField()
    pub_date = models.DateTimeField('date published')
    pic = models.ImageField(upload_to = get_image_path, default = 'home/static/home/images/casd.png')
    # def __str__(self):
    #     return self.question_text
    
    def pic_url(self):
        return self.pic.url[4:]


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

#     def __str__(self):
#         return self.choice_text