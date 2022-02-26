from django.urls import path

from expenses_tracker.web.views import index, expense_create, expense_edit, expense_delete, profile_details, \
    profile_create, profile_edit, profile_delete

urlpatterns = (
    path('', index, name='home page'),

    path('create/', expense_create, name='create expense'),
    path('edit/<int:pk>/', expense_edit, name='edit expense'),
    path('delete/<int:pk>/', expense_delete, name='delete expense'),

    path('profile/create/', profile_create, name='create profile'),
    path('profile/', profile_details, name='profile details'),
    path('profile/edit/<int:pk>/', profile_edit, name='edit profile'),
    path('profile/delete/<int:pk>/', profile_delete, name='delete profile'),
)
