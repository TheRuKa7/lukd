"""Independent specification examples and former bug regressions."""
import importlib.util
import json
from pathlib import Path
import random
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('sim_patterns', ROOT / 'tools/sim_patterns.py')
SIM = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(SIM)


class PatternModelTests(unittest.TestCase):
    def test_spec_examples(self):
        for case in json.loads((ROOT / 'tests/pattern_cases.json').read_text()):
            self.assertEqual(SIM.evaluate(case['digits'], case['lucky']), case['pattern'])
            self.assertEqual(SIM.multiplier(case['pattern'], case['digits']), case['mult'])

    def test_descending_completion_and_legal_fallback(self):
        self.assertEqual(SIM.closer_aim([8,7],7),6)
        # No6: choose legal Zero-Sum5 over lower-priority Pair8.
        self.assertEqual(SIM.closer_aim([8,7],7,[0,1,2,3,5,7,8,9]),5)

    def test_absent_face_is_rejected(self):
        with self.assertRaises(ValueError):
            SIM.stop(SIM.wheel_faces(9,2,[0,1,2,3,5,6,7,8]),9,1,random.Random(7))

    def test_nil_zero_and_chosen_preserved(self):
        for digit in range(10):
            faces=SIM.nil_faces(digit)
            self.assertEqual(len(set(faces)),8)
            self.assertIn(0,faces)
            self.assertIn(digit,faces)

    def test_repair_changes_digits_and_reevaluates(self):
        digits,pattern,source,used=SIM.repair([1,8,4],7,2)
        self.assertEqual((digits,pattern,source,used),([1,8,1],'ZERO_SUM','haps_hand',False))
        digits,pattern,source,used=SIM.repair([2,9,5],7,2,True)
        self.assertEqual(source,'black_cat')
        self.assertTrue(used)

    def test_typed_unique_scalar_tuning(self):
        data=SIM.tuning()
        self.assertEqual(data[('enemy','varro_balance')],1200)
        self.assertEqual(data[('pattern','overwrite')],21)

    def test_reproducible_legal_party_model(self):
        result=SIM.run(9,2,0.25,800,True)
        self.assertEqual(result,SIM.run(9,2,0.25,800,True))
        self.assertAlmostEqual(sum(result['rates'].values()),1)


if __name__ == '__main__':
    unittest.main()
