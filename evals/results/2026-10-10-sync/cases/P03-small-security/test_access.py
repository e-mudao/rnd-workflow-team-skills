import unittest
from access import can_read

class AccessTests(unittest.TestCase):
    def test_authorization_matrix(self):
        for same_tenant in (False, True):
            for owner in (False, True):
                for admin in (False, True):
                    with self.subTest(same_tenant=same_tenant, owner=owner, admin=admin):
                        user = {"tenant": "a" if same_tenant else "b", "id": 1 if owner else 2, "admin": admin}
                        resource = {"tenant": "a", "owner": 1}
                        self.assertEqual(can_read(user, resource), same_tenant and (owner or admin))

if __name__ == "__main__":
    unittest.main()
