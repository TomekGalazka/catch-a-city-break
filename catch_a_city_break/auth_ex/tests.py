import pytest
from django.test import TestCase
from django.contrib.auth.models import User


# @pytest.mark.django_db
# def test_register_user(client, django_user_model):
#     username = 'DonaldTrump'
#     email = 'rurek123@op.pl'
#     password = 'qwerty'
#     user = django_user_model.objects.get(username=username)
#     with pytest.raises(ValueError):
#         if user in django_user_model.objects.all():
#     # django_user_model.objects.create_user(
#     #     username=username,
#     #     email=email,
#     #     password=password,
#     # )
#     # user = django_user_model.objects.get(username=username)
#     # assert user in django_user_model.objects.all()


# @pytest.mark.parametrize('key', [
#     ('name'),
#     ('password'),
#     ('repeat_password'),
#     ('email')
# ])
# def test_register_context(key, client):
#     url = '/product/{}/'.format(product.pk)  # => /product/23/
#     response = client.get(url)
#     assert response.context[key]
