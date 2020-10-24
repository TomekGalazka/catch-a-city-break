import pytest
from django.test import TestCase
from django.contrib.auth.models import User
from auth_ex.forms import RegisterUserForm
from django.urls import reverse_lazy


@pytest.mark.django_db
def test_register_user(client):
    data = {
        'username': 'DonaldTrump',
        'email': 'rurek123@op.pl',
        'password': 'qwerty',
        'repeat_password': 'qwerty'
    }
    form = RegisterUserForm(data)
    assert form.is_valid()

    response = client.post('/auth/register_user/', data)
    assert response.status_code == 302
    all_users = User.objects.all()

    assert all_users.filter(username=data['username']).exists()
        # import pdb
        # pdb.set_trace()


@pytest.mark.django_db
def test_login(client):
    user = User.objects.create_user(username='DonaldTrump', password='123')
    client.force_login(user)
    response = client.get(reverse_lazy('city_breaks_app:travel-plan-create'))
    assert response.status_code == 200



    # django_user_model.objects.create_user(
    #     username=username,
    #     email=email,
    #     password=password,
    # )
    # user = django_user_model.objects.get(username=username)
    # assert user in django_user_model.objects.all()


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
