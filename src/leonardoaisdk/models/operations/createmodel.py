"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import custom_model_type as shared_custom_model_type
from ...models.shared import sd_versions as shared_sd_versions
from ...models.shared import strength as shared_strength
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateModelRequestBody:
    r"""Query parameters to be provided in the request body as a JSON object"""
    UNSET='__SPEAKEASY_UNSET__'
    dataset_id: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('datasetId') }})
    r"""The ID of the dataset to train the model on."""
    instance_prompt: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('instance_prompt') }})
    r"""The instance prompt to use during training."""
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the model."""
    description: Optional[str] = dataclasses.field(default='', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is CreateModelRequestBody.UNSET }})
    r"""The description of the model."""
    model_type: Optional[shared_custom_model_type.CustomModelType] = dataclasses.field(default=shared_custom_model_type.CustomModelType.GENERAL, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelType'), 'exclude': lambda f: f is None }})
    r"""The category the most accurately reflects the model."""
    nsfw: Optional[bool] = dataclasses.field(default=False, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('nsfw'), 'exclude': lambda f: f is CreateModelRequestBody.UNSET }})
    r"""Whether or not the model is NSFW."""
    resolution: Optional[int] = dataclasses.field(default=512, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('resolution'), 'exclude': lambda f: f is CreateModelRequestBody.UNSET }})
    r"""The resolution for training. Must be 512 or 768."""
    sd_version: Optional[shared_sd_versions.SdVersions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sd_Version'), 'exclude': lambda f: f is None }})
    r"""The base version of stable diffusion to use if not using a custom model. v1_5 is 1.5, v2 is 2.1, if not specified it will default to v1_5."""
    strength: Optional[shared_strength.Strength] = dataclasses.field(default=shared_strength.Strength.MEDIUM, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('strength'), 'exclude': lambda f: f is None }})
    r"""When training using the PIXEL_ART model type, this influences the training strength."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SDTrainingOutput:
    UNSET='__SPEAKEASY_UNSET__'
    api_credit_cost: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiCreditCost'), 'exclude': lambda f: f is SDTrainingOutput.UNSET }})
    r"""API Credits Cost for Model Training. Available for Production API Users."""
    custom_model_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('customModelId'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateModelResponseBody:
    r"""Responses for POST /models"""
    UNSET='__SPEAKEASY_UNSET__'
    sd_training_job: Optional[SDTrainingOutput] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sdTrainingJob'), 'exclude': lambda f: f is CreateModelResponseBody.UNSET }})
    



@dataclasses.dataclass
class CreateModelResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[CreateModelResponseBody] = dataclasses.field(default=None)
    r"""Responses for POST /models"""
    

