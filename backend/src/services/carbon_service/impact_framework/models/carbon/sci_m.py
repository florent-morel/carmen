"""
sci-m model of IF
"""

from backend.src.services.carbon_service.impact_framework.models.metadata import (
    Metadata,
)
from backend.src.services.carbon_service.impact_framework.models.model_utilities import (
    ModelUtilities,
)


class SciM(ModelUtilities):
    """
    Adds the sci-m-cpu and the storage embodied emissions for the VMs
    """

    def __init__(self):
        config = {
            "input-parameters": ["carbon-embodied", "storage-embodied"],
            "output-parameter": "carbon-embodied",
        }
        output_metadata = [
            Metadata("carbon", "gCO2e", "Carbon embodied emissions", "sum", "sum")
        ]
        super().__init__("builtin", "Sum", config, output_metadata)
