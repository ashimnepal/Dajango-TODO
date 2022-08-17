from django.urls import path
from todo_app.views import item_list, item_add, item_delete, item_update

# CRUD

# C = Create
# R = Retrieve (listing items)
# U = Update
# D = Delete

urlpatterns = [
    path("", item_list),
    path("item-add/", item_add),
    path("item-delete/<int:pk>/", item_delete),
    path("item-update/<int:pk>/", item_update),
]
