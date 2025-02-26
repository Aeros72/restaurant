from django.test import TestCase

from kitchen.forms import (CookCreationForm,
                           CookYearsUpdateForm,
                           DishSearchForm,
                           DishTypeSearchForm,
                           CookSearchForm)


class FormsTest(TestCase):
    def test_cook_creation_form_with_firstname_lastname_years_of_experience(self):
        form_data = {
            "username": "test_user",
            "password1": "test_password",
            "password2": "test_password",
            "first_name": "test_name",
            "last_name": "test_surname",
            "years_of_experience": 10
        }
        form = CookCreationForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data, form_data)

    def test_form_valid(self):
        form_data = {
            "years_of_experience": 25,
        }
        form = CookYearsUpdateForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_form_invalid(self):
        form_data = {
            "years_of_experience": -5,
        }
        form = CookYearsUpdateForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_dish_search_form(self):
        form = DishSearchForm(
            data={
                "name": "test"
            }
        )
        self.assertTrue(form.is_valid())

    def test_dish_type_search_form(self):
        form = DishTypeSearchForm(
            data={
                "name": "Test"
            }
        )
        self.assertTrue(form.is_valid())

    def test_cook_search_form(self):
        form = CookSearchForm(
            data={
                "username": "test_username"
            }
        )
        self.assertTrue(form.is_valid())
