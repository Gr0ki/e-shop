from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ..v1.views import v1_data


class APIV1RoutesListTestCase(APITestCase):
    @classmethod
    def setUpClass(cls):
        """
        Specifying url, user password, and creating the user with staff permissions.
        Applying instructions from the rewritten 'setUpClass' classmethod.
        """
        cls.url = reverse("docs:api-v1-routes")
        cls.password = "teststaffpassword"
        cls.username = "teststaff"
        cls.user = User.objects.all().filter(username=cls.username).first()
        if cls.user is None:
            cls.user = User.objects.create_user(
                cls.username, email="teststaff@test.com", password=cls.password
            )
            cls.user.is_staff = True
            cls.user.save()
        super().setUpClass()

    def test_response_data_for_guest(self):
        """
        Tests if appropriate data and response code are returned for an unauthorized user.
        """
        response = self.client.get(APIV1RoutesListTestCase.url)
        self.assertEqual(
            response.data["detail"], "Authentication credentials were not provided."
        )
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_response_data_for_staff(self):
        """
        Tests if appropriate data and response code are returned for authorized staff user.
        """
        # Make all requests in the context of a logged in session
        self.client.login(
            username=APIV1RoutesListTestCase.username,
            password=APIV1RoutesListTestCase.password,
        )
        # Get the response and test its data
        response = self.client.get(APIV1RoutesListTestCase.url)
        self.assertEqual(len(response.data.keys()), len(v1_data.keys()))
        for key, value in v1_data.items():
            self.assertEqual(response.data[key], value)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Log out
        self.client.logout()
