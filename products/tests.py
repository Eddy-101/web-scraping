from django.test import TestCase

from .scraping import getScrapping

# Create your tests here.
class TestBooks(TestCase):
    # verify books
    def test_verify_products_ebay(self):
        products = getScrapping("https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw=producto&_sacat=0", "ebay")
        self.assertNotEqual(len(products), 0)

    def test_verify_products_mercadolibre(self):
        products = getScrapping("https://listado.mercadolibre.com.bo/productos#D[A:productos]", "mercado_libre")
        self.assertNotEqual(len(products), 0)

        
        

