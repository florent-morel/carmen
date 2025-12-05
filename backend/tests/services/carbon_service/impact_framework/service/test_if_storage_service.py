# pylint: disable=redefined-outer-name
"""
Unit tests for IFStorageService in impact framework.
"""
from unittest.mock import patch, MagicMock
import pytest

from backend.src.services.carbon_service.impact_framework.service.if_storage_service import (
    IFStorageService,
)
from backend.src.schemas.storage_resource import StorageResource
from backend.src.services.carbon_service.impact_framework.service.if_service import (
    IFService,
)


@pytest.fixture
def mock_storage_1():
    """
    Fixture to create a real storage resource object for testing.
    """
    return StorageResource(
        id="storage_1",
        name="Test Storage",
        storage_type="SSD",
        replication_type="LRS",
        size_gb=128.0,
        region="westeurope",
        carbon_intensity=253.0,
        time_points=["2021-01-01T00:00:00Z"],
        duration_seconds=86400,
    )


@patch.object(IFStorageService, "__init__", lambda self, duration: None)
@patch.object(IFStorageService, "run_if", autospec=True)
@patch.object(IFStorageService, "parse_if_output", autospec=True)
def test_run_engine_success(mock_parse_if_output, mock_run_if, mock_storage_1):
    """
    Test the run_engine method of IFStorageService with mock storage data.
    """
    service = IFStorageService(86400)

    result = service.run_engine([mock_storage_1])

    mock_run_if.assert_called_once_with(service, [mock_storage_1], 0)
    mock_parse_if_output.assert_called_once_with(service, [mock_storage_1], file_id=0)
    assert result == [mock_storage_1]


@patch.object(IFService, "get_models_info", autospec=True)
def test_get_models_info(mock_super_get_models_info):
    """
    Test the get_models_info method of IFStorageService.
    """
    service = IFStorageService(86400)
    data = {"hardware_models": {"p-storage": {}}}
    service.get_models_info(data)

    mock_super_get_models_info.assert_called_once()
    assert "p-storage" in service.data["hardware_models"]
    assert data["hardware_models"]["p-storage"]
