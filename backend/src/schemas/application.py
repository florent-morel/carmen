"""
Module to handle the app data retrieved from Argos.
"""

from __future__ import annotations

from pydantic import Field
from backend.src.schemas.compute_resource import ComputeResource
from backend.src.schemas.pod import Pod


class Application(ComputeResource):
    """
    Schema for Application specifics.
    """

    # IMP: Application class would have a list of clusters, only if we plan to display the selected clusters'
    # computation of the selected app from the UI
    pods: list[Pod] = Field(default_factory=list)
