import unittest
import requests


class GeoEncoder(unittest.TestCase):
    def test_failure(self):
        url = "https://nominatim.openstreetmap.org/sear"
        param = {'q':'135 + pilkington + avenue, +birmingham', 'format': 'xml', 'addressdetails': '1', 'polygon_geojson': '1'}

        response = requests.get(url, param)
        self.assertEqual(response.status_code, 404)

    def test_format_xml(self):
        url = "https://nominatim.openstreetmap.org/search"
        param = {'q':'135 + pilkington + avenue, +birmingham', 'format': 'xml', 'addressdetails': '1', 'polygon_geojson': '1'}

        response = requests.get(url, param)
        self.assertEqual(response.ok, True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'text/xml; charset=UTF-8')


    def test_format_json(self):
        url = "https://nominatim.openstreetmap.org/search/Unter%20den%20Linden%201%20Berlin"
        param = {'format': 'json', 'addressdetails': '1', 'limit': '1', 'polygon_svg': '1'}

        response = requests.get(url, param)
        self.assertEqual(response.ok, True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'application/json; charset=UTF-8')

        data = response.json()
        latitude = data[0]['lat']
        longitude = data[0]['lon']
        formatted_address = data[0]['display_name']
        self.assertEqual('52.51720765', latitude)
        self.assertEqual('13.397834399325466', longitude)
        self.assertEqual('Kommandantenhaus, 1, Unter den Linden, Spandauer Vorstadt, Mitte, Berlin, 10117, Deutschland', formatted_address)

    def test_format_html(self):
        url = "https://nominatim.openstreetmap.org/search"
        param = {}

        response = requests.get(url, param)
        self.assertEqual(response.ok, True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.headers['Content-Type'], 'text/html; charset=UTF-8')


if __name__ == '__main__':
    unittest.main()
