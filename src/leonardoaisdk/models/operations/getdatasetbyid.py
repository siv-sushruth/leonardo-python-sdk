"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import List, Optional


@dataclasses.dataclass
class GetDatasetByIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""The ID of the dataset to return."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DatasetImages:
    r"""columns and relationships of \\"dataset_images\\" """
    UNSET='__SPEAKEASY_UNSET__'
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is DatasetImages.UNSET }})
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDatasetByIDDatasets:
    r"""columns and relationships of \\"datasets\\" """
    UNSET='__SPEAKEASY_UNSET__'
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'exclude': lambda f: f is None }})
    dataset_images: Optional[List[DatasetImages]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('dataset_images'), 'exclude': lambda f: f is None }})
    description: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is GetDatasetByIDDatasets.UNSET }})
    id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is GetDatasetByIDDatasets.UNSET }})
    name: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name'), 'exclude': lambda f: f is None }})
    updated_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('updatedAt'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetDatasetByIDResponseBody:
    r"""Responses for GET /datasets/{id}"""
    UNSET='__SPEAKEASY_UNSET__'
    datasets_by_pk: Optional[GetDatasetByIDDatasets] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('datasets_by_pk'), 'exclude': lambda f: f is GetDatasetByIDResponseBody.UNSET }})
    r"""columns and relationships of \\"datasets\\" """
    



@dataclasses.dataclass
class GetDatasetByIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[GetDatasetByIDResponseBody] = dataclasses.field(default=None)
    r"""Responses for GET /datasets/{id}"""
    

