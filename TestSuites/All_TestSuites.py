import unittest
from Tests.E2E_HealthCard import E2EHealthCardTest
from Tests.E2E_ToolsAndTrackers import E2EToolsAndTrackersTest
from Tests.login import LoginTest

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(E2EToolsAndTrackersTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(E2EHealthCardTest)

masterSuite = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner().run(masterSuite)