"""
sci-e model of IF
"""

from backend.src.services.carbon_service.impact_framework.models.metadata import (
    Metadata,
)
from backend.src.services.carbon_service.impact_framework.models.model_utilities import (
    ModelUtilities,
)


class SciE(ModelUtilities):
    """
    Abstract class for sci-e model of IF, indicating it shouldn't be instantiated directly
    without a subclass providing an implementation of fill_inputs.
    """

    def __init__(self):
        config = {
            "input-parameters": ["cpu/energy", "memory/energy", "storage/energy"],
            "output-parameter": "energy",
        }
        output_metadata = [
            Metadata("energy", "kWh", "Energy consumption", "sum", "sum")
        ]
        super().__init__("builtin", "Sum", config, output_metadata)
