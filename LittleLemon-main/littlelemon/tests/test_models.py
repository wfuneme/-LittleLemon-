from django.forms import ValidationError
from django.test import TestCase
from restaurant.models import Booking, Menu
from django.utils import timezone
from django.db import IntegrityError
from datetime import timedelta

class MenuTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.menu_item = Menu.objects.create(title="IceCream", price=80, inventory=100)

    def test_get_item_returns_correct_string(self):
        itemstr = self.menu_item.get_item()
        self.assertEqual(itemstr, "IceCream: 80")
        
    def test_get_item_with_negative_price(self):
        self.menu_item.price = -10
        itemstr = self.menu_item.get_item()
        self.assertEqual(itemstr, "IceCream: -10")


class BookingTest(TestCase):

    def test_booking_creation_with_valid_data(self):
        booking_date = timezone.localtime(timezone.now()) + timedelta(days=1)  # Data no futuro
        booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=3,
            bookingDate=booking_date
        )
        booking.full_clean() 

        self.assertEqual(booking.name, "John Doe")
        self.assertEqual(booking.no_of_guests, 3)
        self.assertEqual(booking.bookingDate, booking_date)

    def test_booking_creation_with_past_date(self):
        booking_date = timezone.localtime(timezone.now()) - timedelta(days=1)  # Data no passado
        booking = Booking(
            name="Jane Doe",
            no_of_guests=2,
            bookingDate=booking_date
        )

        with self.assertRaises(ValidationError):
            booking.full_clean()

    def test_booking_creation_without_name(self):
        booking_date = timezone.localtime(timezone.now()) + timedelta(days=1)
        booking = Booking(
            no_of_guests=2,
            bookingDate=booking_date
        )

        with self.assertRaises(ValidationError):
            booking.full_clean()

    def test_str_method_returns_name(self):
        booking_date = timezone.localtime(timezone.now()) + timedelta(days=1)
        booking = Booking.objects.create(
            name="John Doe",
            no_of_guests=3,
            bookingDate=booking_date
        )
        self.assertEqual(str(booking), "John Doe")