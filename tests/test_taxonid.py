from unittest import TestCase

from taxonid.taxonid import get_taxonid


class TestTaxonID(TestCase):

    def test_taxonid(self):
        self.assertEqual(
            511145,
            get_taxonid('Escherichia coli str. K-12 substr. MG1655')
        )

    def test_taxonid_error(self):
        self.assertEqual(
            -1,
            get_taxonid('foo')
        )
