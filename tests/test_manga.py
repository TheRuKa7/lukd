"""Independent boundary and layout-failure tests for the manga export contract."""
import importlib.util
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('build_manga',ROOT/'tools/build_manga.py')
m=importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

class MangaLayoutChecks(unittest.TestCase):
    def test_rejects_rectangles_outside_the_page_and_nonfinite_values(self):
        self.assertTrue(m.rectangle([.1,.1,.3,.4]))
        for box in [[-.1,0,.3,.4],[0,.9,.3,.2],[0,0,0,.4],[0,0,float('inf'),.4]]:
            self.assertFalse(m.rectangle(box))

    def test_containment_is_not_merely_overlap(self):
        self.assertTrue(m.contains([.1,.1,.3,.4],[.12,.12,.2,.2]))
        self.assertFalse(m.contains([.1,.1,.3,.4],[.05,.12,.2,.2]))
        self.assertTrue(m.overlaps([0,0,.3,.3],[.2,.2,.3,.3]))
        self.assertFalse(m.overlaps([0,0,.3,.3],[.3,0,.3,.3]))

    def test_tiny_balloon_fails_instead_of_hiding_text(self):
        entry={'id':'test','text':'This must remain readable.','kind':'speech','box':[.1,.1,.02,.02],'max_lines':2}
        with self.assertRaises(ValueError): m.fit_entry(entry,[1800,2700],{})

    def test_resonance_is_substituted_as_text_not_health(self):
        entry={'id':'test','text':'{{resonance}}','kind':'ui','box':[.1,.1,.4,.08],'max_lines':2}
        fit=m.fit_entry(entry,[1800,2700],{'resonance':0})
        self.assertEqual(fit['copy'],'0')
        self.assertEqual(fit['lines'],['0'])

    def test_nan_identifier_preserves_its_exact_case(self):
        entry={'id':'nan','text':'NaN','kind':'label','preserve_case':True,'box':[.1,.1,.3,.06],'max_lines':1}
        self.assertEqual(m.fit_entry(entry,[1800,2700],{})['lines'],['NaN'])

    def test_nan_is_preserved_inside_uppercase_speech(self):
        entry={'id':'nan_speech','text':'NaN. Worth more.','kind':'speech','box':[.1,.1,.5,.12],'max_lines':2}
        self.assertEqual(' '.join(m.fit_entry(entry,[1800,2700],{})['lines']),'NaN. WORTH MORE.')

    def test_complete_authored_layout_has_unique_resolvable_ids(self):
        manifest=m.read_json(m.CHAPTER/'pages.json')
        dialogue=m.read_json(m.CHAPTER/'dialogue.json')
        report=m.validate(manifest,dialogue,require_art=False)
        self.assertEqual(report['errors'],[])
        self.assertEqual(report['pages'],20)
        self.assertGreater(report['panels'],60)

if __name__=='__main__':unittest.main()
