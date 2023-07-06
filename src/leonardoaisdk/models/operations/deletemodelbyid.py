"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

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
class DeleteModelByID200ApplicationJSONCustomModels:
    r"""columns and relationships of \\"custom_models\\" """
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeleteModelByID200ApplicationJSON:
    r"""Responses for DELETE /models/{id}"""
    delete_custom_models_by_pk: Optional[DeleteModelByID200ApplicationJSONCustomModels] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delete_custom_models_by_pk'), 'exclude': lambda f: f is None }})
    r"""columns and relationships of \\"custom_models\\" """
    




@dataclasses.dataclass
class DeleteModelByIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_model_by_id_200_application_json_object: Optional[DeleteModelByID200ApplicationJSON] = dataclasses.field(default=None)
    r"""Responses for DELETE /models/{id}"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
