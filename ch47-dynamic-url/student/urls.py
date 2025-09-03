from django.urls import path, register_converter
from student.views import home, profile
from student.converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, 'yyyy')

urlpatterns = [
    path('', home, name='home'),
    # path('profile/<my_id>', profile, name='profile'),
    # path('profile/<int:my_id>', profile, name='profile'),
    # path('profile/<slug:my_id>', profile, name='profile'),
    # path('profile/<int:my_id>/<my_class>', profile, name='profile'),
    path('profile/<yyyy:year>', profile, name='profile'),
]
