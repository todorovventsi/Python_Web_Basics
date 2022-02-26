from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from expenses_tracker.web.validators import only_letters_validator, ImageMaxSizeValidatorInMb


class Profile(models.Model):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 15

    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 15

    DEFAULT_BUDGET_VALUE = 0
    MIN_BUDGET_VALUE = 0

    IMAGE_UPLOAD_PATH = 'profiles/'
    IMAGE_MAX_SIZE_MB = 5

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,
        )
    )

    last_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            only_letters_validator,
        )
    )

    budget = models.FloatField(
        default=DEFAULT_BUDGET_VALUE,
        validators=(
            MinValueValidator(MIN_BUDGET_VALUE),
        )
    )

    profile_image = models.ImageField(
        upload_to=IMAGE_UPLOAD_PATH,
        null=True,
        blank=True,
        validators=(
            ImageMaxSizeValidatorInMb(IMAGE_MAX_SIZE_MB),
        )
    )


class Expense(models.Model):
    TITLE_MAX_LENGTH = 30

    title = models.CharField(
        max_length=TITLE_MAX_LENGTH,
    )

    expense_image = models.URLField(
        verbose_name='Link to Image'
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    price = models.FloatField()

    class Meta:
        ordering = ['title', 'price', ]
