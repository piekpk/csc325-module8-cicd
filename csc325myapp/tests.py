from django.test import TestCase
from rest_framework.test import APIClient


class HealthEndpointTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_health_returns_200(self):
        response = self.client.get("/api/health/")
        self.assertEqual(response.status_code, 200)

    def test_health_returns_ok_status(self):
        response = self.client.get("/api/health/")
        self.assertEqual(response.data["status"], "ok")
        self.assertEqual(response.data["service"], "csc325-module8-cicd")

    def test_hello_returns_greeting(self):
        response = self.client.get("/api/hello/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["message"], "Hello, world!")

    def test_health_returns_version(self):
        response = self.client.get("/api/health/")
        self.assertEqual(response.data["version"], "1.1")