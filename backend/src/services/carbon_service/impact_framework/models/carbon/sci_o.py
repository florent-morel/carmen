"""
sci-o model of IF
"""

from backend.src.schemas.compute_resource import ComputeResource
from backend.src.services.carbon_service.impact_framework.models.model_utilities import (
    ModelUtilities,
)


class SciO(ModelUtilities):
    """
    Concrete class for the Sci-O model of IF
    """

    def __init__(self):
        super().__init__('"@grnsft/if-plugins"', "SciO")

    # IMP: Cluster and VM specific not time!
    @staticmethod
    def fill_inputs(compute_resource: ComputeResource, time_index: int):
        """
        Fills the time point specific input values.
        """
        return {"grid/carbon-intensity": compute_resource.carbon_intensity}
