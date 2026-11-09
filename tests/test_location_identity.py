"""Guard a source-to-book mix-up that assigned street life to the final institution."""
import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('omen_location_canon',ROOT/'tools/canon.py')
canon=importlib.util.module_from_spec(spec);spec.loader.exec_module(canon)

class LocationIdentity(unittest.TestCase):
    def test_basilica_has_its_own_institutional_record(self):
        basilica=canon.land_info('The Basilica')
        meridian=canon.land_info('Meridian')
        self.assertIn('Even Hand',basilica['Key locations'])
        self.assertIn('Ivo',basilica['Key locations'])
        self.assertNotEqual(basilica,meridian)
        self.assertIn('Rain Alley',meridian['Key locations'])
        self.assertNotIn('Rain Alley',basilica['Key locations'])

if __name__=='__main__':unittest.main()
