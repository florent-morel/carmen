"""
Module to handle the cluster data retrieved from Argos.
"""

from __future__ import annotations

from pydantic import Field
from backend.src.schemas.compute_resource import ComputeResource
from backend.src.schemas.pod import Pod


class Cluster(ComputeResource):
    """
    Schema for Cluster specifics.
    """

    pods: list[Pod] = Field(default_factory=list)
    carbon_intensity: float = 0.0
