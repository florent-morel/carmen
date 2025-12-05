"""
Base Resource schema for carbon calculations.

Defines the base Resource class containing common fields for all resource types
including energy consumption and carbon emission tracking capabilities.
"""

from __future__ import annotations

from abc import ABC
from pydantic import BaseModel, Field


class Resource(ABC, BaseModel):
    """
    Base schema for all resource types (compute, storage, network, etc.).

    Contains common fields for energy consumption and carbon emission tracking
    that are shared across all resource types.
    """

    id: str  # Unique identifier for the resource
    name: str | None = None
    energy_consumed: list[float] = Field(default_factory=list)
    carbon_operational: list[float] = Field(default_factory=list)
    carbon_embodied: list[float] = Field(default_factory=list)
    carbon_emitted: list[float] = Field(default_factory=list)
    time_points: list = Field(
        default_factory=list
    )  # time for VM, timestamp for Pod/App
    total_energy_consumed: float = 0.0
    total_carbon_operational: float = 0.0
    total_carbon_embodied: float = 0.0
    total_carbon_emitted: float = 0.0
