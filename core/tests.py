from django.test import TestCase
from django.urls import reverse

from core.forms import SignupForm


class LandingViewTest(TestCase):
    def test_landing_page_renders(self):
        response = self.client.get('/')
        self.assertIs(response.status_code, 200)

    def test_landing_page_has_urls(self):
        response = self.client.get('/')
        self.assertIn('signup_url', response.context)
        self.assertIn('login_url', response.context)


class SignupViewTest(TestCase):
    def test_signup_form_appears(self):
        response = self.client.get(reverse('core:signup'))
        self.assertIs(response.status_code, 200)


class SignupFormTest(TestCase):
    def test_errors_on_alpha_phone(self):
        form = SignupForm(data={
            'phone': 'abcd'
        })
        self.assertIn('phone', form.errors)

    def test_errors_on_short_phone(self):
        form = SignupForm(data={
            'phone': '0171'
        })
        self.assertIn('phone', form.errors)

    def test_valid_phone(self):
        form = SignupForm(data={
            'phone': '01712345678'
        })
        self.assertNotIn('phone', form.errors)
