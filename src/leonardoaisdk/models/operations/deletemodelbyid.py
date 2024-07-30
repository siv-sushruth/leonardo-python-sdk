"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclasses.dataclass
class DeleteModelByIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""The ID of the model to delete."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CustomModels:
    r"""columns and relationships of \\"custom_models\\" """
    UNSET='__SPEAKEASY_UNSET__'
    id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is CustomModels.UNSET }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteModelByIDResponseBody:
    r"""Responses for DELETE /models/{id}"""
    UNSET='__SPEAKEASY_UNSET__'
    delete_custom_models_by_pk: Optional[CustomModels] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delete_custom_models_by_pk'), 'exclude': lambda f: f is DeleteModelByIDResponseBody.UNSET }})
    r"""columns and relationships of \\"custom_models\\" """
    



@dataclasses.dataclass
class DeleteModelByIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[DeleteModelByIDResponseBody] = dataclasses.field(default=None)
    r"""Responses for DELETE /models/{id}"""
    

