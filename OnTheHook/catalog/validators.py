from django.core import exceptions, validators
from django.utils.deconstruct import deconstructible

__all__ = []


@deconstructible
class MaxWordsValidator(validators.BaseValidator):
    def __init__(self, max_words):
        self.max_words = max_words

    def __call__(self, value):
        text_len = len(value.split())
        print(text_len)
        if text_len > self.max_words:
            raise exceptions.ValidationError(
                f"Максимально возможная длина текста состовляет "
                f"{self.max_words} слов. Сейчас {text_len} слов.",
            )

    def __eq__(self, __value: object):
        return super().__eq__(__value)
