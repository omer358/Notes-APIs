from django.contrib.auth.models import User
from django.test import TestCase
from django.utils import timezone

from ..models import Notes


class NoteModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        none = User.objects.create_user('none', 'none@gmail.com', '1234')
        Notes.objects.create(title='Thoughts',
                             content='Though I found a way out!',
                             user=none,
                             created_date=timezone.now())

    def test_verbose_name_plural(self):
        self.assertEqual(str(Notes._meta.verbose_name_plural), "Notes")

    def test_title_label(self):
        note = Notes.objects.get(id=1)
        field_label = note._meta.get_field('title').verbose_name
        self.assertEqual(field_label, 'title')

    def test_content_label(self):
        note = Notes.objects.get(id=1)
        field_label = note._meta.get_field('content').verbose_name
        self.assertEqual(field_label, 'content')

    def test_user_label(self):
        note = Notes.objects.get(id=1)
        field_label = note._meta.get_field('user').verbose_name
        self.assertEqual(field_label, 'user')

    def test_created_date_label(self):
        note = Notes.objects.get(id=1)
        field_label = note._meta.get_field('created_date').verbose_name
        self.assertEqual(field_label, 'created date')

    def test_latest_modify_label(self):
        note = Notes.objects.get(id=1)
        field_label = note._meta.get_field('modified_at').verbose_name
        self.assertEqual(field_label, 'modified at')
