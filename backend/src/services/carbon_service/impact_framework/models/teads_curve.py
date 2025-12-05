"""
CPU model of IF
"""

from backend.src.schemas.compute_resource import ComputeResource
from backend.src.services.carbon_service.impact_framework.models.model_utilities import (
    ModelUtilities,
)


class TeadsCurve(ModelUtilities):
    """
    Concrete class for teads-curve model of IF to be used in CPU energy calculation
    """

    def __init__(self):
        config = {
            "method": "linear",
            # teads-curve data points
            "x": [0, 10, 50, 100],  # x-axis represents cpu/utilization (in %)
            "y": [0.12, 0.32, 0.75, 1.02],  # y-axis represents the tdp ratio (no unit)
            "input-parameter": "cpu/utilization",
            "output-parameter": "tdp-ratio",
        }
        super().__init__("builtin", "Interpolation", config)

    @staticmethod
    def fill_inputs(compute_resource: ComputeResource, time_index: int):
        """
        Fills the teads-curve input val. from the pod
        """
        return {
            "timestamp": compute_resource.time_points[time_index],
            "cpu/utilization": min(compute_resource.cpu_util[time_index] * 100, 100),
        }
