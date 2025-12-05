"""
sci model of IF
"""

from backend.src.services.carbon_service.impact_framework.models.metadata import (
    Metadata,
)
from backend.src.services.carbon_service.impact_framework.models.model_utilities import (
    ModelUtilities,
)


class Sci(ModelUtilities):
    """
    Concrete class for the SCI model of IF
    """

    def __init__(self):
        config = {
            "input-parameters": ["carbon-operational", "carbon-embodied"],
            "output-parameter": "carbon",
        }
        input_metadata = [
            Metadata(
                "carbon-operational",
                "gCO2e",
                "Operational carbon emissions",
                "sum",
                "sum",
            ),
            Metadata(
                "carbon-embodied", "gCO2e", "Embodied carbon emissions", "sum", "sum"
            ),
        ]
        output_metadata = [
            Metadata("carbon", "gCO2e", "Carbon emissions", "sum", "sum")
        ]
        super().__init__("builtin", "Sum", config, output_metadata, input_metadata)
