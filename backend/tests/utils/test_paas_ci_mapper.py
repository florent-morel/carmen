# pylint: disable=protected-access
"""
This module contains tests for various functions in pass_ci_mapper file.
"""

import unittest
from unittest.mock import patch

from backend.src.utils.paas_ci_mapper import PaasCiMapper


class TestPaasCiMapper(unittest.TestCase):
    """
    Test cases for the `PaasCiMapper` class.
    """

    @patch("backend.src.utils.paas_ci_mapper.remove_unnecessary")
    def test_extract_zone_from_paas(self, mock_remove_unnecessary):
        """
        Checks if it gets the correct zone from the corresponding stack
        :return:
        """
        mock_remove_unnecessary.side_effect = lambda x: x
        result = PaasCiMapper._PaasCiMapper__extract_zone_from_paas("ngi-dev-eun1-c-1")
        assert result == "northeurope"

    @patch("backend.src.utils.paas_ci_mapper.remove_unnecessary")
    def test_extract_zone_no_match(self, mock_remove_unnecessary):
        """
        Tests the scenario where there's no match for the zone extraction.
        """
        mock_remove_unnecessary.return_value = "PAAS-UNKNOWN"
        result = PaasCiMapper._PaasCiMapper__extract_zone_from_paas("PaaS-Unknown")
        self.assertIsNone(result)

    @patch("backend.src.utils.paas_ci_mapper.remove_unnecessary")
    def test_extract_zone_direct_match(self, mock_remove_unnecessary):
        """
        Tests the scenario where the zone is directly matched.
        """
        mock_remove_unnecessary.return_value = "EUS"
        result = PaasCiMapper._PaasCiMapper__extract_zone_from_paas(
            "prd-eus2-hosobs01b"
        )
        assert result == "eastus"

    def test_calculate_ci_with_existing_zone(self):
        """
        Tests the calculate_ci method with an existing zone.
        """
        mock_zone = "eastus"
        result = PaasCiMapper.calculate_ci(mock_zone)
        assert result == 384

    def test_calculate_ci_with_missing_zone(self):
        """
        Tests the calculate_ci method with a missing zone.
        """
        mock_zone = "example_zone"
        result = PaasCiMapper.calculate_ci(mock_zone)
        assert result == 281

    @patch.object(
        PaasCiMapper,
        "_PaasCiMapper__extract_zone_from_paas",
        return_value="example_zone",
    )
    @patch.object(PaasCiMapper, "calculate_ci", return_value=1.0)
    def test_get_ci_from_paas(self, mock_calculate_ci, mock_extract_zone_from_paas):
        """
        Tests the get_ci_from_paas method.
        """
        mock_paas = "example_paas"
        _ = PaasCiMapper.get_ci_from_paas(mock_paas)
        mock_extract_zone_from_paas.assert_called_once_with("example_paas")
        mock_calculate_ci.assert_called_once_with("example_zone")
