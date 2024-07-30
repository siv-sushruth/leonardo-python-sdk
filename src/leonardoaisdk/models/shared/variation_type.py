"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class VariationType(str, Enum):
    r"""The type of variation."""
    OUTPAINT = 'OUTPAINT'
    INPAINT = 'INPAINT'
    UPSCALE = 'UPSCALE'
    UNZOOM = 'UNZOOM'
    NOBG = 'NOBG'
