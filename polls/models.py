from django.db import models




class Employees(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    position = models.CharField(max_length=100)
    salary = models.CharField(max_length=55)

    def __str__(self):
        return self.name
#
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

