from django.test import TestCase


# Create your tests here.
class BasicTestClass(TestCase):
    @classmethod
    def setUpTestData(self):
        # print("SetUpTestData")
        pass

    # def setUp(self):
    #     print("setUp")

    def test_true_is_true(self):
        self.assertEqual(True, True)

    def test_suma(self):
        self.assertEquals(4, 2 + 2)

    def test_error(self):
        self.assertTrue(True)
