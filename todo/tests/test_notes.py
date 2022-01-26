import pytest
from django.test import Client

@pytest.mark.django_db
class TestNotes:
    def test_notes_index_view(self):
        client = Client()

        response = client.get("/")
        assert response.status_code == 200

