"""Regression checks for required Play import fields and our actual SDK choices."""
import csv
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parent

class PlayResponses(unittest.TestCase):
    def test_required_account_and_data_responses(self):
        paths = [ROOT / f'play-data-safety-v{v}.csv' for v in ('0.31.28', '0.31.29')]
        self.assertEqual(paths[0].read_bytes(), paths[1].read_bytes())
        with paths[1].open(newline='') as f:
            rows = list(csv.DictReader(f))
        key = lambda r: (r['Question ID (machine readable)'], r['Response ID (machine readable)'])
        values = {key(r):r['Response value'] for r in rows}
        self.assertEqual(len(values), len(rows))
        for q in ('PSL_DATA_COLLECTION_COLLECTS_PERSONAL_DATA','PSL_DATA_COLLECTION_ENCRYPTED_IN_TRANSIT'):
            self.assertEqual(values[q, ''], 'TRUE')
        methods = {r:v for (q,r),v in values.items() if q=='PSL_SUPPORTED_ACCOUNT_CREATION_METHODS'}
        self.assertEqual(set(methods), {'PSL_ACM_USER_ID_PASSWORD','PSL_ACM_USER_ID_OTHER_AUTH','PSL_ACM_USER_ID_PASSWORD_OTHER_AUTH','PSL_ACM_OAUTH','PSL_ACM_OTHER','PSL_ACM_NONE'})
        self.assertEqual({r for r,v in methods.items() if v=='TRUE'}, {'PSL_ACM_NONE'})
        self.assertEqual(values['PSL_HAS_OUTSIDE_APP_ACCOUNTS',''], 'FALSE')
        self.assertEqual(values['PSL_ACCOUNT_DELETION_URL',''], '')
        self.assertEqual(values['PSL_SUPPORT_DATA_DELETION_BY_USER','DATA_DELETION_YES'], 'TRUE')
        self.assertEqual(values['PSL_SUPPORT_DATA_DELETION_BY_USER','DATA_DELETION_NO'], 'FALSE')
        self.assertEqual(values['PSL_SUPPORT_DATA_DELETION_BY_USER','DATA_DELETION_NO_AUTO_DELETED'], 'FALSE')
        self.assertEqual(values['PSL_DATA_DELETION_URL',''], 'https://dydxo116.github.io/shallwepuzzle-privacy/#rights')
        self.assertNotIn(('PSL_DATA_COLLECTION_USER_REQUEST_DELETE',''),values)
        for q in ('PSL_DATA_COLLECTION_COMPLIES_FAMILY_POLICY','PSL_INDEPENDENTLY_VALIDATED','PSL_UPI_BADGE_OPT_IN'):
            self.assertEqual(values[q,''], 'FALSE')
        selected = {r for (q,r),v in values.items() if q.startswith('PSL_DATA_TYPES_') and v=='TRUE'}
        self.assertEqual(selected, {'PSL_APPROX_LOCATION','PSL_USER_INTERACTION','PSL_CRASH_LOGS','PSL_PERFORMANCE_DIAGNOSTICS','PSL_DEVICE_ID'})
        for data_type in selected:
            prefix = f'PSL_DATA_USAGE_RESPONSES:{data_type}:'
            self.assertEqual(values[prefix+'PSL_DATA_USAGE_COLLECTION_AND_SHARING','PSL_DATA_USAGE_ONLY_COLLECTED'], 'TRUE')
            self.assertEqual(values[prefix+'PSL_DATA_USAGE_EPHEMERAL',''], 'FALSE')
            crash = data_type=='PSL_CRASH_LOGS'
            self.assertEqual(values[prefix+'PSL_DATA_USAGE_COLLECTION_AND_SHARING','PSL_DATA_USAGE_ONLY_SHARED'], 'FALSE' if crash else 'TRUE')
            self.assertEqual(values[prefix+'DATA_USAGE_USER_CONTROL','PSL_DATA_USAGE_USER_CONTROL_OPTIONAL'], 'TRUE' if crash else 'FALSE')
            self.assertEqual(values[prefix+'DATA_USAGE_USER_CONTROL','PSL_DATA_USAGE_USER_CONTROL_REQUIRED'], 'FALSE' if crash else 'TRUE')

if __name__ == '__main__':
    unittest.main()
