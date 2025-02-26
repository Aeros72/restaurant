from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from kitchen.models import DishType, Dish, Cook


class ModelTests(TestCase):
    def test_dish_type_str(self):
        dish_type = DishType.objects.create(
            name="Test DishType",
        )

        self.assertEqual(
            str(dish_type), dish_type.name)

    def test_dish_str(self):
        dish_type = DishType.objects.create(
            name="Test DishType",
        )

        dish = Dish.objects.create(
            name="Test Model",
            price=100,
            dish_type=dish_type,
        )

        self.assertEqual(str(dish), dish.name)

    def test_cook_str(self):
        cook = get_user_model().objects.create(
            username="test",
            first_name="test_fn",
            last_name="test_ln"
        )

        self.assertEqual(
            str(cook),
            f"{cook.username} ({cook.first_name} {cook.last_name})"
        )

    def test_create_cook_with_years_of_experience(self):
        username = "test"
        years_of_experience = 15

        cook = get_user_model().objects.create(
            username=username,
            years_of_experience=years_of_experience
        )

        self.assertEqual(username, cook.username)
        self.assertEqual(years_of_experience, cook.years_of_experience)

    def test_get_absolute_url(self):
        cook = Cook.objects.create(
            username="test_user",
            first_name="test_fn",
            last_name="test_ln",
            years_of_experience=25
        )

        expected_url = reverse("kitchen:cook-detail", kwargs={"pk": cook.pk})
        self.assertEqual(cook.get_absolute_url(), expected_url)
