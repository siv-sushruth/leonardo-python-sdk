"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclasses.dataclass
class GetInitImageByIDRequest:
    id: str = dataclasses.field(metadata={'path_param': { 'field_name': 'id', 'style': 'simple', 'explode': False }})
    r"""_\\"id\\" is required_"""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetInitImageByIDInitImages:
    r"""columns and relationships of \\"init_images\\" """
    UNSET='__SPEAKEASY_UNSET__'
    created_at: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('createdAt'), 'exclude': lambda f: f is None }})
    id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is GetInitImageByIDInitImages.UNSET }})
    url: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('url'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class GetInitImageByIDResponseBody:
    r"""Responses for GET /init-image/{id}"""
    UNSET='__SPEAKEASY_UNSET__'
    init_images_by_pk: Optional[GetInitImageByIDInitImages] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('init_images_by_pk'), 'exclude': lambda f: f is GetInitImageByIDResponseBody.UNSET }})
    r"""columns and relationships of \\"init_images\\" """
    



@dataclasses.dataclass
class GetInitImageByIDResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[GetInitImageByIDResponseBody] = dataclasses.field(default=None)
    r"""Responses for GET /init-image/{id}"""
    

