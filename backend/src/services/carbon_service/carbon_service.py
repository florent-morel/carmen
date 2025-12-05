"""
This module defines the abstract base class for implementing carbon service functionality.
"""

from __future__ import annotations

from typing import Protocol
from backend.src.schemas.compute_resource import ComputeResource


class CarbonService(Protocol):
    """
    This interface defines the methods that should be implemented by carbon service classes
    to compute carbon and energy metrics for the given compute units and time intervals.
    """

    async def run_engine(
        self, compute_resources: list[ComputeResource]
    ) -> list[ComputeResource]:
        """
        This method computes the carbon and energy metrics for the given compute units over
        the specified time interval.

        Args:
            compute_resources: List of compute resources for which metrics are to be computed. App or Cluster
        """
        raise NotImplementedError("Subclasses must implement run_engine")
