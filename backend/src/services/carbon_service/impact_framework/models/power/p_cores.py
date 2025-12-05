"""
PCores model that computes the power consumption of the requested cores from the application pods
"""

from backend.src.services.carbon_service.impact_framework.models.metadata import (
    Metadata,
)
from backend.src.services.carbon_service.impact_framework.models.model_utilities import (
    ModelUtilities,
)


class PCores(ModelUtilities):
    """
    Concrete class for the CPU power consumption model made with IF builtins
    """

    def __init__(self):
        config = {
            # resources-reserved = requested_cores,
            # cpu/thermal-design-power = Average Watts Per Core for Azure taken from CCF.
            "input-parameters": [
                "tdp-ratio",
                "cpu/thermal-design-power",
                "resources-reserved",
            ],
            "output-parameter": " = 'cpu/power' / 1000",
        }
        input_metadata = [
            Metadata("resources-reserved", "cores", "Requested cores", "sum", "sum")
        ]
        output_metadata = [
            Metadata("cpu/power", "kW", "CPU power consumption", "sum", "sum")
        ]
        super().__init__(
            "builtin",
            "Multiply",
            config,
            output_metadata=output_metadata,
            input_metadata=input_metadata,
        )
