"""
sci-m-cpu model of IF
"""

from backend.src.schemas.pod import Pod
from backend.src.services.carbon_service.impact_framework.models.model_utilities import (
    ModelUtilities,
)


class SciMcpu(ModelUtilities):
    """
    Concrete class for the Sci-M-CPU model of IF
    """

    def __init__(self):
        super().__init__('"@grnsft/if-plugins"', "SciM")

    @staticmethod
    def fill_inputs(pod: Pod, time_index: int):
        """
        Fills the sci-m-cpu input val. from the pod, returns an empty dict if there is no values
        """
        return {
            "resources-reserved": pod.requested_cpu[time_index],
            "resources-total": 66,
        }
