"""
Storage Services Power Consumption model made with IF builtins based on disk type (SSD/HDD)
"""

from backend.src.schemas.storage_resource import StorageResource
from backend.src.common.constants import (
    STORAGE_POWER_COEFFICIENT_MAPPING,
    STORAGE_REPLICATION_FACTORS,
)
from backend.src.services.carbon_service.impact_framework.models.metadata import (
    Metadata,
)
from backend.src.services.carbon_service.impact_framework.models.model_utilities import (
    ModelUtilities,
)


class PStorage(ModelUtilities):
    """
    Concrete class for the Storage Power Consumption model made with IF builtins.

    Input units:
    - storage_size: GB
    Output units:
    - power: kW
    """

    def __init__(self):
        config = {
            "input-parameters": ["storage/requested", "power/coefficient"],
            "output-parameter": "storage/power",  # in kW
        }
        output_metadata = [
            Metadata("storage/power", "kW", "Storage Power consumption", "sum", "sum")
        ]
        super().__init__("builtin", "Multiply", config, output_metadata)

    @staticmethod
    def fill_inputs(storage_resource: StorageResource, time_index: int):
        """
        Fills the storage input values from the storage resource.

        Args:
            storage_resource: The storage resource containing data
            time_index: The time index for which to get the data

        Returns:
            Dict containing storage input in GB and the power coefficient based on storage type
        """
        # Get the power coefficient based on storage type
        power_coefficient = STORAGE_POWER_COEFFICIENT_MAPPING.get(
            storage_resource.storage_type.upper(),
            STORAGE_POWER_COEFFICIENT_MAPPING["UNKNOWN"],
        )

        # Get the replication factor
        replication_factor = STORAGE_REPLICATION_FACTORS.get(
            storage_resource.replication_type.upper(), 1
        )

        # Calculate the effective storage size (considering replication)
        effective_size = storage_resource.size_gb * replication_factor

        return {
            "storage/requested": effective_size,
            "power/coefficient": power_coefficient,
        }
