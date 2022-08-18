from genericpath import isfile
import os
import unittest
from unittest.mock import patch
import manage_ressource
from dotenv import load_dotenv

# If in dev environment, get env variables from .env file
if os.path.isfile(os.path.join(os.path.dirname(__file__), '.env')):
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    load_dotenv(dotenv_path=env_path)

GEOCAT_USERNAME = os.environ["GEOCAT_USERNAME"]
GEOCAT_PASSWORD = os.environ["GEOCAT_PASSWORD"]

class TestObject(unittest.TestCase):

    @classmethod
    @patch("builtins.input")
    @patch("getpass.getpass")
    def setUpClass(self, password, username):

        username.return_value = GEOCAT_USERNAME
        password.return_value = GEOCAT_PASSWORD

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
