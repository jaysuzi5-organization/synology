"""
Synology Model and Pydantic Schema

This module defines:
- The SQLAlchemy ORM model for persisting Synology metrics.
- The Pydantic schema for validating API requests when creating/updating Synology.
"""

from sqlalchemy import Column, DateTime, Integer, String, Float, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from framework.db import Base
from datetime import datetime, UTC
from pydantic import BaseModel
from typing import Optional, List, Dict, Any


class Synology(Base):
    """
    SQLAlchemy ORM model representing a Synology NAS metrics record.
    """

    __tablename__ = "synology"

    id = Column(Integer, primary_key=True, index=True)

    # System Info
    model = Column(String(50), nullable=False)
    serial = Column(String(100), nullable=False, index=True)
    ram_mb = Column(Integer, nullable=True)
    dsm_version = Column(String(100), nullable=True)

    # Status
    temperature = Column(Integer, nullable=True)
    temperature_warn = Column(Boolean, default=False)

    # Uptime
    uptime_days = Column(Integer, nullable=False, default=0)
    uptime_hours = Column(Integer, nullable=False, default=0)
    uptime_minutes = Column(Integer, nullable=False, default=0)

    # Performance
    cpu_percent = Column(Float, nullable=True)
    memory_percent = Column(Float, nullable=True)

    # Network
    net_up = Column(Integer, nullable=True)     # bytes uploaded
    net_down = Column(Integer, nullable=True)   # bytes downloaded

    # Storage
    overall_percent_used = Column(Float, nullable=True)
    volumes = Column(JSONB, nullable=True)  # list of volume dicts
    disks = Column(JSONB, nullable=True)    # list of disk dicts

    # Timestamps
    create_date = Column(DateTime, default=lambda: datetime.now(UTC))
    update_date = Column(
        DateTime,
        default=lambda: datetime.now(UTC),
        onupdate=lambda: datetime.now(UTC)
    )

    def __repr__(self):
        return f"<Synology(id={self.id}, model='{self.model}', serial='{self.serial}')>"


# ---------------- Pydantic Schemas ----------------

class Volume(BaseModel):
    name: str
    id: str
    status: str
    percent_used: float
    size_total: float
    size_used: float


class Disk(BaseModel):
    id: str
    name: str
    status: str
    smart_status: str
    temperature: int


class SynologyCreate(BaseModel):
    model: str
    serial: str
    ram_mb: Optional[int] = None
    dsm_version: Optional[str] = None

    temperature: Optional[int] = None
    temperature_warn: Optional[bool] = False

    uptime_days: Optional[int] = 0
    uptime_hours: Optional[int] = 0
    uptime_minutes: Optional[int] = 0

    cpu_percent: Optional[float] = None
    memory_percent: Optional[float] = None

    net_up: Optional[int] = None
    net_down: Optional[int] = None

    overall_percent_used: Optional[float] = None
    volumes: Optional[List[Volume]] = None
    disks: Optional[List[Disk]] = None
