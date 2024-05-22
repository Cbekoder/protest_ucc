from django.db import models

class Science(models.Model):
    def scienceImage(self, filename):
        return '/'.join(['ScienceImages', filename])

    name = models.CharField(max_length=55)
    image = models.ImageField(upload_to=scienceImage, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Fan'
        verbose_name_plural = 'Fanlar'


class Question(models.Model):
    science = models.ForeignKey(Science, on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Savol'
        verbose_name_plural = 'Savollar'

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.question.text



