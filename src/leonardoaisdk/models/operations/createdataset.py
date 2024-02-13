"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateDatasetRequestBody:
    r"""Query parameters to be provided in the request body as a JSON object"""
    UNSET='__SPEAKEASY_UNSET__'
    name: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('name') }})
    r"""The name of the dataset."""
    description: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('description'), 'exclude': lambda f: f is CreateDatasetRequestBody.UNSET }})
    r"""A description for the dataset."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class Datasets:
    r"""columns and relationships of \\"datasets\\" """
    UNSET='__SPEAKEASY_UNSET__'
    id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is Datasets.UNSET }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateDatasetResponseBody:
    r"""Responses for POST /datasets"""
    UNSET='__SPEAKEASY_UNSET__'
    insert_datasets_one: Optional[Datasets] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('insert_datasets_one'), 'exclude': lambda f: f is CreateDatasetResponseBody.UNSET }})
    r"""columns and relationships of \\"datasets\\" """
    



@dataclasses.dataclass
class CreateDatasetResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[CreateDatasetResponseBody] = dataclasses.field(default=None)
    r"""Responses for POST /datasets"""
    

