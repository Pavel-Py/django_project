from re import search

from django.core.exceptions import ValidationError


def only_letters(value):
    if search('[^\w -]|\d|_', value):
        raise ValidationError('Поле может содержать только буквы')