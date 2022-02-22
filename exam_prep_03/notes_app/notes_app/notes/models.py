from django.db import models


class Profile(models.Model):
    FIRSTNAME_MAX_LENGTH = 20
    LASTNAME_MAX_LENGTH = 20

    first_name = models.CharField(
        max_length=FIRSTNAME_MAX_LENGTH,
    )

    last_name = models.CharField(
        max_length=LASTNAME_MAX_LENGTH,
    )

    age = models.IntegerField()

    image = models.URLField()


class Note(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    image = models.URLField()

    content = models.TextField()
