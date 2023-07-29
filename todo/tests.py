from django.test import TestCase
from django.utils import timezone
from .models import Category, Task

# Create your tests here.
def create_category(category_name):
    """
    Create a category with the given `category_name` and `date`.
    """
    time = timezone.now()
    return Category.objects.create(category_name=category_name, pub_date=time)

class CategoryIndexViewTest(TestCase):
    pass