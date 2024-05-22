from django.db import models
from django.contrib.auth.models import AbstractUser
from rest_framework.exceptions import ValidationError
from assets.models import City

class User(AbstractUser):
    GENDER_CHOICES = (
        ('E', 'Erkak'),
        ('A', 'Ayol'),
    )

    phone = models.CharField(max_length=13, unique=True, null=True, blank=True)
    isGoogle = models.BooleanField(default=False)
    password = models.CharField(max_length=200, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    def nameFile(self, filename):
        return '/'.join(['UserImages', str(self.phone), filename])

    image = models.ImageField(verbose_name='Image', upload_to=nameFile, blank=True, null=True)

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['username', 'password']

    def clean(self):
        if not self.isGoogle and not self.password:
            raise ValidationError("Google orqali ro'yxatdan o'tmasangiz parol majburiy")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Foydalanuvchi'
        verbose_name_plural = 'Foydalanuvchilar'
