from snapshottest import TestCase
import csv
import os

from server.schema import form_map
from server.schemulator import schema_to_form

class SchemaTestCase(TestCase):
    maxDiff = 50000
    def test_csv_to_schema(self):
        for slug, entry in sorted(form_map.items()):
            self.assertMatchSnapshot(entry['schema'])
