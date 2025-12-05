"""
Energy model in which sci-e value is multiplied by PUE value
"""

from backend.src.schemas.compute_resource import ComputeResource
from backend.src.services.carbon_service.impact_framework.models.metadata import (
    Metadata,
)
from backend.src.services.carbon_service.impact_framework.models.model_utilities import (
    ModelUtilities,
)


class SciEPue(ModelUtilities):
    """
    Concrete class for the Energy model with Power Usage Effectiveness value
    """

    def __init__(self):
        config = {"input-parameters": ["energy", "pue"], "output-parameter": "energy"}
        output_metadata = [
            Metadata(
                "energy", "kWh", "Energy consumption multiplied by PUE", "sum", "sum"
            )
        ]
        super().__init__("builtin", "Multiply", config, output_metadata)

    @staticmethod
    def fill_inputs(compute_resource: ComputeResource, time_index: int):
        """
        Fills the time point specific input values.
        """
        return {"pue": compute_resource.pue}
