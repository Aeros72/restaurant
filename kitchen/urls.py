from django.urls import path

from .views import (
    index,
    DishListView,
    DishDetailView,
    DishCreateView,
    DishUpdateView,
    DishDeleteView,
    CookListView,
    CookDetailView,
    CookCreateView,
    CookYearsUpdateView,
    CookDeleteView,
    DishTypeListView,
    DishTypeCreateView,
    DishTypeUpdateView,
    DishTypeDeleteView,
    ToggleAssignToDishView,
)

urlpatterns = [
    path("", index, name="index"),
    path(
        "dish_types/",
        DishTypeListView.as_view(),
        name="dish-type-list",
    ),
    path(
        "dish_types/create/",
        DishTypeCreateView.as_view(),
        name="dish-type-create",
    ),
    path(
        "dish_types/<int:pk>/update/",
        DishTypeUpdateView.as_view(),
        name="dish-type-update",
    ),
    path(
        "dish_types/<int:pk>/delete/",
        DishTypeDeleteView.as_view(),
        name="dish-type-delete",
    ),
    path("dishes/", DishListView.as_view(), name="dish-list"),
    path("dishes/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("dishes/create/", DishCreateView.as_view(), name="dish-create"),
    path("dishes/<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("dishes/<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path(
        "dishes/<int:pk>/toggle-assign/",
        ToggleAssignToDishView.as_view(),
        name="toggle-dish-assign",
    ),
    path("cooks/", CookListView.as_view(), name="cook-list"),
    path(
        "cooks/<int:pk>/", CookDetailView.as_view(), name="cook-detail"
    ),
    path("cooks/create/", CookCreateView.as_view(), name="cook-create"),
    path(
        "cooks/<int:pk>/update/",
        CookYearsUpdateView.as_view(),
        name="cook-update",
    ),
    path(
        "cooks/<int:pk>/delete/",
        CookDeleteView.as_view(),
        name="cook-delete",
    ),
]

app_name = "kitchen"
