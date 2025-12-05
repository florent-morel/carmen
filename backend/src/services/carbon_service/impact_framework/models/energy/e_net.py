"""
Network model of IF
"""

from backend.src.schemas.compute_resource import ComputeResource
from backend.src.services.carbon_service.impact_framework.models.model_utilities import (
    ModelUtilities,
)


class ENet(ModelUtilities):
    """
    Concrete class for the network model of IF
    """

    def __init__(self):
        super().__init__('"@grnsft/if-plugins"', "ENet")

    @staticmethod
    def fill_inputs(compute_resource: ComputeResource, time_index: int):
        """
        Fills the network input val. from the pod
        """
        # we summed the in-out value already at thanos, therefor initializing only one of the variables is fine,
        # IF doing the same in the following line:
        # https://github.com/Green-Software-Foundation/if-plugins/blob/5050060faf7b0ab860a889217599da2eb505f453/src/lib/e-net/index.ts#L59
        return {
            "network/data-in": compute_resource.network_io[time_index],
            "network/data-out": 0,
        }
