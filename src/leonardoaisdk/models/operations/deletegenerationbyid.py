"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional



@dataclasses.dataclass
class DeleteGenerationByIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""The ID of the generation to delete."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeleteGenerationByID200ApplicationJSONGenerations:
    r"""columns and relationships of \\"generations\\" """
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class DeleteGenerationByID200ApplicationJSON:
    r"""Responses for DELETE /generations/{id}"""
    delete_generations_by_pk: Optional[DeleteGenerationByID200ApplicationJSONGenerations] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delete_generations_by_pk'), 'exclude': lambda f: f is None }})
    r"""columns and relationships of \\"generations\\" """
    




@dataclasses.dataclass
class DeleteGenerationByIDResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    delete_generation_by_id_200_application_json_object: Optional[DeleteGenerationByID200ApplicationJSON] = dataclasses.field(default=None)
    r"""Responses for DELETE /generations/{id}"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
