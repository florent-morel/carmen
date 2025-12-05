"""
Memory Power Consumption model made with IF builtins
"""

from backend.src.schemas.pod import Pod
from backend.src.services.carbon_service.impact_framework.models.metadata import (
    Metadata,
)
from backend.src.services.carbon_service.impact_framework.models.model_utilities import (
    ModelUtilities,
)


class PMem(ModelUtilities):
    """
    Concrete class for the Memory Power Consumption model made with IF builtins
    """

    def __init__(self):
        config = {
            "input-parameter": "memory/requested",
            "coefficient": 0.000392,  # 0.000392 kW/GB taken from CCF
            "output-parameter": "memory/power",
        }
        output_metadata = [
            Metadata("memory/power", "kW", "Memory Power consumption", "sum", "sum")
        ]
        super().__init__("builtin", "Coefficient", config, output_metadata)

    @staticmethod
    def fill_inputs(pod: Pod, time_index: int):
        """
        Fills the memory input. val. from the pod
        """
        return {"memory/requested": pod.requested_memory[time_index] / (10**9)}
