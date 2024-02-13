"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclasses.dataclass
class DeleteDatasetByIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""The ID of the dataset to delete."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteDatasetByIDDatasets:
    r"""columns and relationships of \\"datasets\\" """
    UNSET='__SPEAKEASY_UNSET__'
    id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is DeleteDatasetByIDDatasets.UNSET }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DeleteDatasetByIDResponseBody:
    r"""Responses for DELETE /datasets/{id}"""
    UNSET='__SPEAKEASY_UNSET__'
    delete_datasets_by_pk: Optional[DeleteDatasetByIDDatasets] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('delete_datasets_by_pk'), 'exclude': lambda f: f is DeleteDatasetByIDResponseBody.UNSET }})
    r"""columns and relationships of \\"datasets\\" """
    



@dataclasses.dataclass
class DeleteDatasetByIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[DeleteDatasetByIDResponseBody] = dataclasses.field(default=None)
    r"""Responses for DELETE /datasets/{id}"""
    

