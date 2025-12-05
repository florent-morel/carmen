"""
PCpu model that computes the power consumption of the CPU
"""

from backend.src.services.carbon_service.impact_framework.models.model_utilities import (
    ModelUtilities,
)
from backend.src.services.carbon_service.impact_framework.models.metadata import (
    Metadata,
)


class PCpu(ModelUtilities):
    """
    Concrete class for the CPU power consumption model made with IF builtins
    """

    def __init__(self):
        config = {
            "input-parameters": ["tdp-ratio", "cpu/thermal-design-power"],
            "output-parameter": " = 'cpu/power' / 1000",
        }
        output_metadata = [
            Metadata("cpu/power", "kW", "CPU power consumption", "sum", "sum")
        ]
        super().__init__("builtin", "Multiply", config, output_metadata)
