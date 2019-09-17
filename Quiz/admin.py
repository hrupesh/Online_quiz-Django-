from django.contrib import admin
from Quiz import models
# Register your models here.


admin.site.register(models.Question)

admin.site.register(models.userprofile)

admin.site.register(models.Tag)


# class Question(models.Model):
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
#     question_text = models.CharField(max_length=1000)
#     choice_text1 = models.CharField(max_length=1000)
#     choice_text2 = models.CharField(max_length=1000)
#     choice_text3= models.CharField(max_length=1000)
#     choice_text4 = models.CharField(max_length=1000)
#     correct_option = models.CharField(max_length=1000)
#     # is_correct = models.BooleanField()
#     def __str__(self):
#         return f"{self.question_text}"

