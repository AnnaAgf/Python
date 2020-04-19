import unittest
import requests


class GeoDecoder(unittest.TestCase):
    def test_failure(self):
        url = "https://nominatim.openstreetmap.org/rever"
        param = {}

        response = requests.get(url, param)
        self.assertEqual(response.status_code, 404)

    def test_format_xml(self):
        url = "https://nominatim.openstreetmap.org/reverse"
        param = {'format': 'xml', 'lat': 52.51720765, 'lon': 13.397834399325466}

        response = requests.get(url, param)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'text/xml; charset=UTF-8')

    def test_format_json(self):
        url = "https://nominatim.openstreetmap.org/reverse"
        param = {'format': 'json', 'lat': 52.51720765, 'lon': 13.397834399325466}

        response = requests.get(url, param)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=UTF-8')

        data = response.json()
        formatted_address = data['display_name']
        self.assertEqual('Kommandantenhaus, 1, Unter den Linden, Spandauer Vorstadt, Mitte, Berlin, 10117, Deutschland', formatted_address)

    def test_format_default_html(self):
        url = "https://nominatim.openstreetmap.org/reverse"
        param = {'lat': 44.50155, 'lon': 11.33989}

        response = requests.get(url, param)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'text/html; charset=UTF-8')


if __name__ == '__main__':
    unittest.main()
