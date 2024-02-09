from django.test import SimpleTestCase
from django.urls import reverse


class HomepageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse("home"))
        self.assertTemplateUsed(response, "home.html")

    def test_for_title(self):
        response = self.client.get(reverse("home"))
        print(response.content)
        self.assertContains(response, "<h1>Programming Languages</h1>")

    def test_for_cards(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, '<div class="card">', count=3)


class AboutpageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse("about"))
        self.assertTemplateUsed(response, "about.html")

    def test_for_title(self):
        response = self.client.get(reverse("about"))
        self.assertContains(response, "<h1>About Page</h1>")

    def test_for_content(self):
        response = self.client.get(reverse("about"))
        self.assertContains(
            response,
            "<p>This page is an exercise in learning how Django displays templates through URL pattern matching.</p>",
        )


class PythonpageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/python/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("python"))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse("python"))
        self.assertTemplateUsed(response, "python.html")

    def test_for_title(self):
        response = self.client.get(reverse("python"))
        self.assertContains(response, "<h1>Python</h1>")

    def test_for_subtitles(self):
        response = self.client.get(reverse("python"))
        self.assertContains(response, "<h2>History</h2>")
        self.assertContains(response, "<h2>Uses</h2>")


class FsharppageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/fsharp/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("fsharp"))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse("fsharp"))
        self.assertTemplateUsed(response, "fsharp.html")

    def test_for_title(self):
        response = self.client.get(reverse("fsharp"))
        self.assertContains(response, "<h1>F#</h1>")

    def test_for_subtitles(self):
        response = self.client.get(reverse("fsharp"))
        self.assertContains(response, "<h2>History</h2>")
        self.assertContains(response, "<h2>Uses</h2>")


class RacketpageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/racket/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("racket"))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse("racket"))
        self.assertTemplateUsed(response, "racket.html")

    def test_for_title(self):
        response = self.client.get(reverse("racket"))
        self.assertContains(response, "<h1>Racket</h1>")

    def test_for_subtitles(self):
        response = self.client.get(reverse("racket"))
        self.assertContains(response, "<h2>History</h2>")
        self.assertContains(response, "<h2>Uses</h2>")
