"""
Module contains tests for the AmadeusService class.
"""

# import unittest

# from backend.src.services.carbon_service.amadeus.amadeus_service import AmadeusService
# from backend.tests.services.carbon_service.mock_data import MOCK_COMPONENTS_CLASS_DATA


# class TestAmadeusService(unittest.TestCase):
#    """
#    Class contains tests for the AmadeusService class.
#    """

# def test_init(self):
#     """
#     Test the initialization of the AmadeusService class.
#     """
#     amadeus_model = AmadeusService(60)
#     self.assertIsNotNone(amadeus_model.cpu_model)
#     self.assertIsNotNone(amadeus_model.memory_model)
#
# def test_run_engine(self):
#     """
#     Test the run_engine method of the AmadeusService class.
#     """
#     amadeus_model = AmadeusService(60)
#
#     new_components = amadeus_model.run_engine(MOCK_COMPONENTS_CLASS_DATA, 60)
#     new_components = asyncio.run(new_components)
#     expected = MOCK_COMPONENTS_CLASS_DATA
#     expected[0].energy_consumed = [0.0006266666667320001, 0.0012533333334640003]
#     expected[0].carbon_emitted = [0.15729333334973203, 0.31458666669946406]
#     self.assertEqual(new_components[0], expected[0])
