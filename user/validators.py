from datetime import date

from dateutil.relativedelta import relativedelta
from rest_framework import serializers


def check_birth_date(birth_date: date):
    age = relativedelta(date.today(), birth_date).years
    if age < 9:
        raise serializers.ValidationError(f'Возрастное ограничение младше 9 лет')
