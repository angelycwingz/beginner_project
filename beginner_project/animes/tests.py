from django.test import SimpleTestCase

# Create your tests here.
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
        self.assertContains(response, "<h1>Top 3 Anime in the world</h1>")

    def test_for_cards(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, '<div class ="card">', count=3)


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
            "<p>The purpose of this website is to let the non-otakus know which are the most watched anime in the world.</p>",
        )


class DbzpageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/dbz/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("dbz"))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse("dbz"))
        self.assertTemplateUsed(response, "dbz.html")

    def test_for_title(self):
        response = self.client.get(reverse("dbz"))
        self.assertContains(response, "<h1>Dragon Ball Z </h1>")

    def test_for_subtitles(self):
        response = self.client.get(reverse("dbz"))
        self.assertContains(response, "<h2>Summary</h2>")
        self.assertContains(response, "<h2>Rating</h2>")


class NarutopageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/naruto/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("naruto"))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse("naruto"))
        self.assertTemplateUsed(response, "naruto.html")

    def test_for_title(self):
        response = self.client.get(reverse("naruto"))
        self.assertContains(response, "<h1>Naruto</h1>")

    def test_for_subtitles(self):
        response = self.client.get(reverse("naruto"))
        self.assertContains(response, "<h2>Summary</h2>")
        self.assertContains(response, "<h2>Rating</h2>")


class OnePiecepageTests(SimpleTestCase):
    def test_url_by_pattern(self):
        response = self.client.get("/one_piece/")
        self.assertEqual(response.status_code, 200)

    def test_url_by_name(self):
        response = self.client.get(reverse("one_piece"))
        self.assertEqual(response.status_code, 200)

    def test_correct_template(self):
        response = self.client.get(reverse("one_piece"))
        self.assertTemplateUsed(response, "onepiece.html")

    def test_for_title(self):
        response = self.client.get(reverse("one_piece"))
        self.assertContains(response, "<h1>One Piece</h1>")

    def test_for_subtitles(self):
        response = self.client.get(reverse("one_piece"))
        self.assertContains(response, "<h2>Summary</h2>")
        self.assertContains(response, "<h2>Rating</h2>")
