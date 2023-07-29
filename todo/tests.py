from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from .models import Category, Task

# Create your tests here.
def create_category(category_name):
    """
    Create a category with the given `category_name` and `date`.
    """
    time = timezone.now()
    return Category.objects.create(category_name=category_name, pub_date=time)

class CategoryIndexViewTest(TestCase):
    """For index view response"""
    def test_response(self):
        """test for index view get response"""
        response = self.client.get(reverse('todo:index'))
        self.assertEqual(response.status_code, 200)

    """Tests for only one category"""
    def test_cars_category(self):
        """Category is displayed in the index page"""
        category = create_category(category_name='cars')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [category]
        )
    
    def test_clothes_category(self):
        """Category is displayed in the index page"""
        category = create_category(category_name='clothes')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [category]
        )
    
    def test_food_category(self):
        """Category is displayed in the index page"""
        category = create_category(category_name='food')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [category]
        )
    
    def test_friends_category(self):
        """Category is displayed in the index page"""
        category = create_category(category_name='friends')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [category]
        )
    
    def test_games_category(self):
        """Category is displayed in the index page"""
        category = create_category(category_name='games')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [category]
        )
    
    def test_clothes_category(self):
        """Category is displayed in the index page"""
        category = create_category(category_name='clothes')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [category]
        )
    
    def test_health_category(self):
        """Category is displayed in the index page"""
        category = create_category(category_name='health')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [category]
        )
    
    def test_homework_category(self):
        """Category is displayed in the index page"""
        category = create_category(category_name='homework')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [category]
        )
    
    def test_insurance_category(self):
        """Category is displayed in the index page"""
        category = create_category(category_name='insurance')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [category]
        )
    
    def test_money_category(self):
        """Category is displayed in the index page"""
        category = create_category(category_name='money')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [category]
        )
    
    def test_sport_category(self):
        """Category is displayed in the index page"""
        category = create_category(category_name='sport')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [category]
        )
    
    def test_study_category(self):
        """Category is displayed in the index page"""
        category = create_category(category_name='study')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [category]
        )
    
    def test_travel_category(self):
        """Category is displayed in the index page"""
        category = create_category(category_name='travel')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [category]
        )
    
    def test_vacation_category(self):
        """Category is displayed in the index page"""
        category = create_category(category_name='vacation')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [category]
        )
    
    def test_work_category(self):
        """Category is displayed in the index page"""
        category = create_category(category_name='work')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [category]
        )
    
    """Tests for only two categories"""
    def test_cars_clothes_two_categories(self):
        """Only two categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        clothes_category = create_category(category_name='clothes')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [cars_category, clothes_category],
            ordered=False
        )
    
    def test_cars_food_two_categories(self):
        """Only two categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        food_category = create_category(category_name='food')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [cars_category, food_category],
            ordered=False
        )
    
    def test_cars_friends_two_categories(self):
        """Only two categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        friends_category = create_category(category_name='friends')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [cars_category, friends_category],
            ordered=False
        )
    
    def test_cars_games_two_categories(self):
        """Only two categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        games_category = create_category(category_name='games')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [cars_category, games_category],
            ordered=False
        )
    
    def test_cars_health_two_categories(self):
        """Only two categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        health_category = create_category(category_name='health')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [cars_category, health_category],
            ordered=False
        )
    
    def test_cars_homework_two_categories(self):
        """Only two categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        homework_category = create_category(category_name='homework')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [cars_category, homework_category],
            ordered=False
        )
    
    def test_cars_insurance_two_categories(self):
        """Only two categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        insurance_category = create_category(category_name='insurance')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [cars_category, insurance_category],
            ordered=False
        )
    
    def test_cars_money_two_categories(self):
        """Only two categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        money_category = create_category(category_name='money')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [cars_category, money_category],
            ordered=False
        )
    
    def test_cars_sport_two_categories(self):
        """Only two categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        sport_category = create_category(category_name='sport')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [cars_category, sport_category],
            ordered=False
        )
    
    def test_cars_study_two_categories(self):
        """Only two categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        study_category = create_category(category_name='study')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [cars_category, study_category],
            ordered=False
        )
    
    def test_cars_travel_two_categories(self):
        """Only two categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        travel_category = create_category(category_name='travel')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [cars_category, travel_category],
            ordered=False
        )
    
    def test_cars_vacation_two_categories(self):
        """Only two categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        vacation_category = create_category(category_name='vacation')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [cars_category, vacation_category],
            ordered=False
        )
    
    def test_cars_work_two_categories(self):
        """Only two categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        work_category = create_category(category_name='work')
        response = self.client.get(reverse("todo:index"))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [cars_category, work_category],
            ordered=False
        )
    
    """Tests for only three categories"""
    def test_three_categories(self):
        """Only three categories are displayed in the index page"""
        friends_category = create_category(category_name='friends')
        insurance_category = create_category(category_name='insurance')
        sport_category = create_category(category_name='sport')
        response = self.client.get(reverse('todo:index'))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [friends_category, insurance_category, sport_category],
            ordered=False
        )
    
    """Tests for only four categories"""
    def test_four_categories(self):
        """Only four categories are displayed in the index page"""
        work_category = create_category(category_name='work')
        games_category = create_category(category_name='games')
        health_category = create_category(category_name='health')
        vacation_category = create_category(category_name='vacation')
        response = self.client.get(reverse('todo:index'))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [
                work_category, games_category, health_category,
                vacation_category
            ],
            ordered=False
        )
    
    """Tests for only five categories"""
    def test_five_categories(self):
        """Only five categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        clothes_category = create_category(category_name='clothes')
        food_category = create_category(category_name='food')
        friends_category = create_category(category_name='friends')
        games_category = create_category(category_name='games')
        response = self.client.get(reverse('todo:index'))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [
                cars_category, clothes_category, food_category,
                friends_category, games_category
            ],
            ordered=False
        )
    
    """Tests for only six categories"""
    def test_six_caetgories(self):
        """Only six categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        clothes_category = create_category(category_name='clothes')
        food_category = create_category(category_name='food')
        friends_category = create_category(category_name='friends')
        games_category = create_category(category_name='games')
        health_category = create_category(category_name='health')
        response = self.client.get(reverse('todo:index'))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [
                cars_category, clothes_category, food_category,
                friends_category, games_category, health_category
            ],
            ordered=False
        )
    
    """Tests for only seven categories"""
    def test_seven_caetgories(self):
        """Only seven categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        clothes_category = create_category(category_name='clothes')
        food_category = create_category(category_name='food')
        friends_category = create_category(category_name='friends')
        games_category = create_category(category_name='games')
        health_category = create_category(category_name='health')
        homework_category = create_category(category_name='homework')
        response = self.client.get(reverse('todo:index'))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [
                cars_category, clothes_category, food_category,
                friends_category, games_category, health_category,
                homework_category
            ],
            ordered=False
        )
    
    """Tests for only eight categories"""
    def test_eight_caetgories(self):
        """Only eight categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        clothes_category = create_category(category_name='clothes')
        food_category = create_category(category_name='food')
        friends_category = create_category(category_name='friends')
        games_category = create_category(category_name='games')
        health_category = create_category(category_name='health')
        homework_category = create_category(category_name='homework')
        insurance_category = create_category(category_name='insurance')
        response = self.client.get(reverse('todo:index'))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [
                cars_category, clothes_category, food_category,
                friends_category, games_category, health_category,
                homework_category, insurance_category
            ],
            ordered=False
        )
    
    """Tests for only nine categories"""
    def test_nine_caetgories(self):
        """Only nine categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        clothes_category = create_category(category_name='clothes')
        food_category = create_category(category_name='food')
        friends_category = create_category(category_name='friends')
        games_category = create_category(category_name='games')
        health_category = create_category(category_name='health')
        homework_category = create_category(category_name='homework')
        insurance_category = create_category(category_name='insurance')
        money_category = create_category(category_name='money')
        response = self.client.get(reverse('todo:index'))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [
                cars_category, clothes_category, food_category,
                friends_category, games_category, health_category,
                homework_category, insurance_category, money_category
            ],
            ordered=False
        )
    
    """Tests for only ten categories"""
    def test_ten_caetgories(self):
        """Only ten categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        clothes_category = create_category(category_name='clothes')
        food_category = create_category(category_name='food')
        friends_category = create_category(category_name='friends')
        games_category = create_category(category_name='games')
        health_category = create_category(category_name='health')
        homework_category = create_category(category_name='homework')
        insurance_category = create_category(category_name='insurance')
        money_category = create_category(category_name='money')
        sport_category = create_category(category_name='sport')
        response = self.client.get(reverse('todo:index'))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [
                cars_category, clothes_category, food_category,
                friends_category, games_category, health_category,
                homework_category, insurance_category, money_category,
                sport_category
            ],
            ordered=False
        )
    
    """Tests for only eleven categories"""
    def test_eleven_caetgories(self):
        """Only eleven categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        clothes_category = create_category(category_name='clothes')
        food_category = create_category(category_name='food')
        friends_category = create_category(category_name='friends')
        games_category = create_category(category_name='games')
        health_category = create_category(category_name='health')
        homework_category = create_category(category_name='homework')
        insurance_category = create_category(category_name='insurance')
        money_category = create_category(category_name='money')
        sport_category = create_category(category_name='sport')
        study_category = create_category(category_name='study')
        response = self.client.get(reverse('todo:index'))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [
                cars_category, clothes_category, food_category,
                friends_category, games_category, health_category,
                homework_category, insurance_category, money_category,
                sport_category, study_category
            ],
            ordered=False
        )
    
    """Tests for only twelve categories"""
    def test_twelve_caetgories(self):
        """Only twelve categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        clothes_category = create_category(category_name='clothes')
        food_category = create_category(category_name='food')
        friends_category = create_category(category_name='friends')
        games_category = create_category(category_name='games')
        health_category = create_category(category_name='health')
        homework_category = create_category(category_name='homework')
        insurance_category = create_category(category_name='insurance')
        money_category = create_category(category_name='money')
        sport_category = create_category(category_name='sport')
        study_category = create_category(category_name='study')
        travel_category = create_category(category_name='travel')
        response = self.client.get(reverse('todo:index'))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [
                cars_category, clothes_category, food_category,
                friends_category, games_category, health_category,
                homework_category, insurance_category, money_category,
                sport_category, study_category, travel_category
            ],
            ordered=False
        )
    
    """Tests for only thirteen categories"""
    def test_thirteen_caetgories(self):
        """Only thirteen categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        clothes_category = create_category(category_name='clothes')
        food_category = create_category(category_name='food')
        friends_category = create_category(category_name='friends')
        games_category = create_category(category_name='games')
        health_category = create_category(category_name='health')
        homework_category = create_category(category_name='homework')
        insurance_category = create_category(category_name='insurance')
        money_category = create_category(category_name='money')
        sport_category = create_category(category_name='sport')
        study_category = create_category(category_name='study')
        travel_category = create_category(category_name='travel')
        vacation_category = create_category(category_name='vacation')
        response = self.client.get(reverse('todo:index'))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [
                cars_category, clothes_category, food_category,
                friends_category, games_category, health_category,
                homework_category, insurance_category, money_category,
                sport_category, study_category, travel_category,
                vacation_category
            ],
            ordered=False
        )
    
    """Tests for only fourteen categories"""
    def test_fourteen_caetgories(self):
        """Only fourteen categories are displayed in the index page"""
        cars_category = create_category(category_name='cars')
        clothes_category = create_category(category_name='clothes')
        food_category = create_category(category_name='food')
        friends_category = create_category(category_name='friends')
        games_category = create_category(category_name='games')
        health_category = create_category(category_name='health')
        homework_category = create_category(category_name='homework')
        insurance_category = create_category(category_name='insurance')
        money_category = create_category(category_name='money')
        sport_category = create_category(category_name='sport')
        study_category = create_category(category_name='study')
        travel_category = create_category(category_name='travel')
        vacation_category = create_category(category_name='vacation')
        work_category = create_category(category_name='work')
        response = self.client.get(reverse('todo:index'))
        self.assertQuerysetEqual(
            response.context["categories_and_labels"]["categories"],
            [
                cars_category, clothes_category, food_category,
                friends_category, games_category, health_category,
                homework_category, insurance_category, money_category,
                sport_category, study_category, travel_category,
                vacation_category, work_category
            ],
            ordered=False
        )