from django.contrib import admin
from django.urls import path, re_path

from server import views

urlpatterns = [
    path('', views.single_page_app),
    re_path(r'app/(.*)', views.single_page_app),
    path('blank_form/<image_name>', views.blank_form),
    path('2/<slug>/', views.step_2, name="step_2"),
    path('3/<int:id>/', views.step_3, name="step_3"),
    path('check_3/<int:id>/', views.check_3),
    path('4/<int:id>/', views.step_4, name="step_4"),
    path('5/', views.step_5, name="step_5"),

    path('admin/', admin.site.urls),
]