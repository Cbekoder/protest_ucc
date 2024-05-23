from django.db import models
from rest_framework.exceptions import ValidationError


class Region(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Viloyatlar'
        verbose_name = 'Viloyat'


class City(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Tuman (Shahar)lar'
        verbose_name = 'Tuman (Shahar)'


class University(models.Model):
    full_name = models.CharField(max_length=400)
    abbr_name = models.CharField(max_length=10)
    description = models.TextField(blank=True)
    image = models.ImageField(max_length=300, upload_to='university_images/')
    phone = models.CharField(max_length=20, blank=True)
    address = models.CharField(max_length=255, blank=True)
    keywords = models.CharField(max_length=800, blank=True)
    longitude = models.FloatField()
    latitude = models.FloatField()

    def __str__(self):
        return self.abbr_name

    class Meta:
        verbose_name_plural = 'Universitetlar'
        verbose_name = 'Universitet'

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

class SciencePairs(models.Model):
    science_1 = models.ForeignKey(Science, on_delete=models.SET_NULL, null=True, blank=True, related_name='science_1')
    science_2 = models.ForeignKey(Science, on_delete=models.SET_NULL, null=True, blank=True, related_name='science_2')

    def __str__(self):
        return f'{self.science_1} | {self.science_2}'

    class Meta:
        verbose_name = 'Fanlar blogi'
        verbose_name_plural = 'Fanlar bloglari'
        unique_together = ('science_1', 'science_2')

class ImportantSciencePairs(models.Model):
    science_1 = models.ForeignKey(Science, on_delete=models.SET_NULL, null=True, blank=True, related_name='Fan_1')
    science_2 = models.ForeignKey(Science, on_delete=models.SET_NULL, null=True, blank=True, related_name='Fan_2')
    science_3 = models.ForeignKey(Science, on_delete=models.SET_NULL, null=True, blank=True, related_name='Fan_3')

    def __str__(self):
        return f'{self.science_1} | {self.science_2} | {self.science_3}'
    def save(self, *args, **kwargs):
        if not self.pk and ImportantSciencePairs.objects.exists():
            raise ValidationError("Faqat bitta majburiy fanlar blogi qo'shish mumkin")
        super(ImportantSciencePairs, self).save(*args, **kwargs)
    class Meta:
        verbose_name = 'Majburiy fanlar blogi'
        verbose_name_plural = 'Majburiy fanlar blogi'
        unique_together = ('science_1', 'science_2', 'science_3')


class Study(models.Model):
    study_name = models.CharField(max_length=400)
    study_code = models.CharField(max_length=15)
    sciencePair = models.ForeignKey(SciencePairs, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.study_name

    class Meta:
        verbose_name_plural = "Yo'nalishlar"
        verbose_name = "Yo'nalish"


class StudyInUniversity(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    study = models.ForeignKey(Study, on_delete=models.CASCADE)
    grant_ball = models.DecimalField(max_digits=3, decimal_places=1, blank=True)
    contract_ball = models.DecimalField(max_digits=3, decimal_places=1, blank=True)
    grant_count = models.IntegerField(default=0, blank=True)
    contract_count = models.IntegerField(default=0, blank=True)

    def __str__(self):
        return self.university.abbr_name

    class Meta:
        verbose_name_plural = "Universitet yo'nalishlari"
        verbose_name = "Universitet yo'nalishi"
