"""
VM Storage Power Consumption model made with IF builtins based on disk type (SSD/HDD)
"""

from backend.src.schemas.virtual_machine import VirtualMachine
from backend.src.common.constants import STORAGE_POWER_COEFFICIENT_MAPPING
from backend.src.services.carbon_service.impact_framework.models.metadata import (
    Metadata,
)
from backend.src.services.carbon_service.impact_framework.models.model_utilities import (
    ModelUtilities,
)


class PVmStorage(ModelUtilities):
    """
    Concrete class for the Storage Power Consumption model made with IF builtins.

    Input units:
    - storage_size: GB
    Output units:
    - power: kW
    """

    def __init__(self):
        config = {
            "input-parameter": "storage/requested",  # in GB and
            "coefficient": STORAGE_POWER_COEFFICIENT_MAPPING["UNKNOWN"],  # kW/GB
            "output-parameter": "storage/power",  # in kW
        }
        output_metadata = [
            Metadata("storage/power", "kW", "Storage Power consumption", "sum", "sum")
        ]
        super().__init__("builtin", "Coefficient", config, output_metadata)

    @staticmethod
    def fill_inputs(virtual_machine: VirtualMachine, time_index: int):
        """
        Fills the storage input values from the virtual machine.

        Args:
            virtual_machine: The virtual machine containing storage data
            time_index: The time index for which to get the data

        Returns:
            Dict containing storage input in GB
        """
        # Storage size in GB
        storage = virtual_machine.storage_size[time_index]
        return {"storage/requested": storage}
