import unittest
from unittest.mock import patch
import manage_ressource


class TestObject(unittest.TestCase):

    @patch("builtins.input")
    @patch("getpass.getpass")
    def setUp(self, password, username):

        username.return_value = "reo"
        password.return_value = "sU6972.."

        self.ogc = manage_ressource.ManageOGCResource()

    def test_init(self):
        self.assertIsInstance(self.ogc, manage_ressource.ManageOGCResource)

    def test_get_layers(self):
        self.ogc.get_ogc_layers(service="wMs", 
            endpoint="https://wms.geo.admin.ch?SERVICE=WMS&VERSION=1.3.0&REQUEST=GetCapabilities")
        self.assertEqual(self.ogc.service, "WMS")
        self.assertEqual(self.ogc.endpoint, "https://wms.geo.admin.ch")
        self.assertTrue(len(self.ogc.layers) > 0)

if __name__ == "__main__":
    unittest.main()
