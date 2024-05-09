"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import universal_upscaler_style as shared_universal_upscaler_style
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateUniversalUpscalerJobRequestBody:
    r"""Query parameters are provided in the request body as a JSON object"""
    UNSET='__SPEAKEASY_UNSET__'
    creativity_strength: Optional[int] = dataclasses.field(default=5, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('creativityStrength'), 'exclude': lambda f: f is CreateUniversalUpscalerJobRequestBody.UNSET }})
    r"""The creativity strength of the universal upscaler, must be integer between 1 and 10"""
    generated_image_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generatedImageId'), 'exclude': lambda f: f is CreateUniversalUpscalerJobRequestBody.UNSET }})
    r"""The ID of the generated image"""
    init_image_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('initImageId'), 'exclude': lambda f: f is CreateUniversalUpscalerJobRequestBody.UNSET }})
    r"""The ID of the init image uploaded"""
    prompt: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt'), 'exclude': lambda f: f is CreateUniversalUpscalerJobRequestBody.UNSET }})
    r"""The prompt for the universal upscaler"""
    upscale_multiplier: Optional[float] = dataclasses.field(default=1.5, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('upscaleMultiplier'), 'exclude': lambda f: f is CreateUniversalUpscalerJobRequestBody.UNSET }})
    r"""The upscale multiplier of the universal upscaler, must be number between 1.00 and 2.00"""
    upscaler_style: Optional[shared_universal_upscaler_style.UniversalUpscalerStyle] = dataclasses.field(default=shared_universal_upscaler_style.UniversalUpscalerStyle.GENERAL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('upscalerStyle'), 'exclude': lambda f: f is CreateUniversalUpscalerJobRequestBody.UNSET }})
    r"""The style to upscale images using universal upscaler with."""
    variation_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('variationId'), 'exclude': lambda f: f is CreateUniversalUpscalerJobRequestBody.UNSET }})
    r"""The ID of the variation image"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UniversalUpscalerOutput:
    UNSET='__SPEAKEASY_UNSET__'
    api_credit_cost: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiCreditCost'), 'exclude': lambda f: f is UniversalUpscalerOutput.UNSET }})
    r"""API Credits Cost for Universal Upscaler Variation. Available for Production API Users."""
    id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is UniversalUpscalerOutput.UNSET }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateUniversalUpscalerJobResponseBody:
    r"""Responses for POST /variations/universal-upscaler"""
    universal_upscaler: Optional[UniversalUpscalerOutput] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('universalUpscaler'), 'exclude': lambda f: f is None }})
    



@dataclasses.dataclass
class CreateUniversalUpscalerJobResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[CreateUniversalUpscalerJobResponseBody] = dataclasses.field(default=None)
    r"""Responses for POST /variations/universal-upscaler"""
    

