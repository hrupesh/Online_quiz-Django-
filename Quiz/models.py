from django.db import models


class userprofile(models.Model):
    registration_number = models.CharField(unique=True , max_length=15)
    password = models.CharField(max_length=250)
    
    def __str__(self):
        return str(self.registration_number)


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)

    def __str__(self):
        return self.tag_name


# class Question(models.Model):
#     question_text = models.CharField(max_length=1000)
#     tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.question_text}\t\t| Tag: {self.tag} |"


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=1000)
#     is_correct = models.BooleanField()
#     def __str__(self):
#         return f"{self.choice_text}"

class Question(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=1000)
    choice_text1 = models.CharField(max_length=200)
    choice_text2 = models.CharField(max_length=200)
    choice_text3= models.CharField(max_length=200)
    choice_text4 = models.CharField(max_length=200)
    correct_option = models.CharField(max_length=200)
    # is_correct = models.BooleanField()
    def __str__(self):
        return f"{self.question_text}"

    
