"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UploadDatasetImageRequestBody:
    r"""Query parameters provided in the request body as a JSON object"""
    extension: str = dataclasses.field(metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('extension') }})
    r"""Has to be png, jpg, jpeg, or webp."""
    



@dataclasses.dataclass
class UploadDatasetImageRequest:
    request_body: UploadDatasetImageRequestBody = dataclasses.field(metadata={'request': { 'media_type': 'application/json' }})
    r"""Query parameters provided in the request body as a JSON object"""
    dataset_id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'datasetId', 'style': 'simple', 'explode': False }})
    r"""_\\"datasetId\\" is required"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class DatasetUploadOutput:
    UNSET='__SPEAKEASY_UNSET__'
    fields: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fields'), 'exclude': lambda f: f is DatasetUploadOutput.UNSET }})
    id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is DatasetUploadOutput.UNSET }})
    key: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('key'), 'exclude': lambda f: f is DatasetUploadOutput.UNSET }})
    url: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is DatasetUploadOutput.UNSET }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class UploadDatasetImageResponseBody:
    r"""Responses for POST /datasets/{datasetId}/upload"""
    UNSET='__SPEAKEASY_UNSET__'
    upload_dataset_image: Optional[DatasetUploadOutput] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('uploadDatasetImage'), 'exclude': lambda f: f is UploadDatasetImageResponseBody.UNSET }})
    



@dataclasses.dataclass
class UploadDatasetImageResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[UploadDatasetImageResponseBody] = dataclasses.field(default=None)
    r"""Responses for POST /datasets/{datasetId}/upload"""
    

