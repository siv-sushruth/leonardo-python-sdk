"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
from enum import Enum


class PricingCalculatorServices(str, Enum):
    r"""The services to be chosen for calculating the API credit cost."""
    IMAGE_GENERATION = 'IMAGE_GENERATION'
    FANTASY_AVATAR_GENERATION = 'FANTASY_AVATAR_GENERATION'
    MOTION_GENERATION = 'MOTION_GENERATION'
    LCM_GENERATION = 'LCM_GENERATION'
    MODEL_TRAINING = 'MODEL_TRAINING'
    TEXTURE_GENERATION = 'TEXTURE_GENERATION'
    UNIVERSAL_UPSCALER = 'UNIVERSAL_UPSCALER'
