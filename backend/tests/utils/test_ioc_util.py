"""
Module containing unit tests for the IoC (Inversion of Control) utility functions.
"""

import unittest
from unittest.mock import patch
from contextlib import contextmanager
from backend.src.utils.ioc_util import IocRegistrationModel, resolve


class TestIocUtil(unittest.TestCase):
    """
    Test cases for the IoC utility functions.
    """

    def setUp(self):
        """
        Set up method to initialize common resources for the test cases.
        """
        self.registration_model = IocRegistrationModel("key", int, str)

    @contextmanager
    def _set_up_mocked_registration_models(self, models):
        """
        Context manager to set up mocked IoC registration models.
        """
        with patch("backend.src.utils.ioc_util.ioc_registered_models", models):
            yield

    def test_ioc_registration_model(self):
        """
        Test case for the IocRegistrationModel initialization.
        """
        self.assertEqual(self.registration_model.ioc_key, "key")
        self.assertEqual(self.registration_model.abstract_type, int)
        self.assertEqual(self.registration_model.concrete_type, str)

    def test_resolve_with_matching_abstract_type_and_ioc_key(self):
        """
        Test case for resolving with matching abstract type and IoC key.
        """
        with self._set_up_mocked_registration_models(
            [IocRegistrationModel("key", int, str)]
        ):
            resolved = resolve(int, "key", 60)
            self.assertEqual(resolved, "60")

    def test_resolve_with_non_matching_abstract_type(self):
        """
        Test case for resolving with non-matching abstract type.
        """
        with self._set_up_mocked_registration_models(
            [IocRegistrationModel("key", int, str)]
        ):
            resolved = resolve(float, "key", 60)
            self.assertIsNone(resolved)

    def test_resolve_with_non_matching_ioc_key(self):
        """
        Test case for resolving with non-matching IoC key.
        """
        with self._set_up_mocked_registration_models(
            [IocRegistrationModel("key", int, str)]
        ):
            resolved = resolve(int, "non_existing_key", 60)
            self.assertIsNone(resolved)

    def test_resolve_with_empty_registration_models(self):
        """
        Test case for resolving with empty registration models.
        """
        with self._set_up_mocked_registration_models([]):
            resolved = resolve(int, "key", 60)
            self.assertIsNone(resolved)


if __name__ == "__main__":
    unittest.main()
