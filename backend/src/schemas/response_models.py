"""
This file contains response models to be used for the API returns.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class HardwareResponse(BaseModel):
    """
    Response model for the hardware as input API endpoint
    """

    energy_consumed: list[float] = Field(default_factory=list)
    carbon_operational: list[float] = Field(default_factory=list)
    carbon_embodied: list[float] = Field(default_factory=list)
    storage_energy: list[float] = Field(default_factory=list)
    storage_embodied: list[float] = Field(default_factory=list)
    cpu_energy: list[float] = Field(default_factory=list)
    total_carbon_operational: float = 0.0
    total_carbon_embodied: float = 0.0
    total_energy_consumed: float = 0.0
