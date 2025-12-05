"""
Module to handle the pods as parts of applications retrieved from Argos.
"""

from __future__ import annotations

from backend.src.schemas.compute_resource import ComputeResource


class Pod(ComputeResource):
    """
    Schema for Pod specifics.
    """

    app: str
    paas: str
    namespace: str
