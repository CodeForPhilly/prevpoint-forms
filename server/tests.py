from snapshottest import TestCase
from server.schema import form_map
import csv
import os

class SchemaTestCase(TestCase):
    maxDiff = 50000
    def test_form_to_schema(self):
        for slug, entry in sorted(form_map.items()):
            self.assertMatchSnapshot(entry['schema'])