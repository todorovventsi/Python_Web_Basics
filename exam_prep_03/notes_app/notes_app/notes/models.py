from django.db import models


class Profile(models.Model):
    FIRSTNAME_MAX_LENGTH = 20
    LASTNAME_MAX_LENGTH = 20

    first_name = models.CharField(
        max_length=FIRSTNAME_MAX_LENGTH,
        verbose_name='First Name',
    )

    last_name = models.CharField(
        max_length=LASTNAME_MAX_LENGTH,
        verbose_name='Last Name',
    )

    age = models.IntegerField(
        verbose_name='Age',
    )

    image = models.URLField(
        verbose_name='Link to Profile Image',
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Note(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
        verbose_name="Title",
    )

    image = models.URLField(
        verbose_name="Link To Image",
    )

    content = models.TextField(
        verbose_name="Content",
    )

    def __str__(self):
        return self.title
