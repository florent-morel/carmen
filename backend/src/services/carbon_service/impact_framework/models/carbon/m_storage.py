"""
Storage Services Embodied Emissions model for IF
"""

from backend.src.schemas.storage_resource import StorageResource
from backend.src.common.constants import STORAGE_EMBODIED_COEFFICIENT_MAPPING
from backend.src.services.carbon_service.impact_framework.models.metadata import (
    Metadata,
)
from backend.src.services.carbon_service.impact_framework.models.model_utilities import (
    ModelUtilities,
)


class MStorage(ModelUtilities):
    """
    Model for storage embodied emissions calculation.
    Input: storage size in GB
    Output: emissions in gCO2e
    """

    def __init__(self):
        config = {
            "input-parameters": [
                "storage/requested",
                "storage/embodied-coefficient",
                "duration/seconds",
            ],  # in GB
            "output-parameter": " = 'carbon-embodied' / 126230400",  # in gCO2e
        }
        output_metadata = [
            Metadata(
                "carbon-embodied", "gCO2e", "Storage embodied emissions", "sum", "sum"
            )
        ]
        super().__init__("builtin", "Multiply", config, output_metadata)

    @staticmethod
    def fill_inputs(storage_resource: StorageResource, time_index: int):
        """
        Fills the storage embodied inputs based on storage type.
        """
        # Get the embodied coefficient based on storage type
        embodied_coefficient = STORAGE_EMBODIED_COEFFICIENT_MAPPING.get(
            storage_resource.storage_type.upper(),
            STORAGE_EMBODIED_COEFFICIENT_MAPPING["UNKNOWN"],
        )

        return {"storage/embodied-coefficient": embodied_coefficient}
