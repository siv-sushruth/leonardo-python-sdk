"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from dataclasses_json import Undefined, dataclass_json
from leonardoaisdk import utils
from typing import Optional


@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetUserSelf200ApplicationJSONUserDetailsUsers:
    r"""columns and relationships of \\"users\\" """
    id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('id'), 'exclude': lambda f: f is None }})
    username: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('username'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetUserSelf200ApplicationJSONUserDetails:
    r"""columns and relationships of \\"user_details\\" """
    show_nsfw: Optional[bool] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('showNsfw'), 'exclude': lambda f: f is None }})
    user: Optional[GetUserSelf200ApplicationJSONUserDetailsUsers] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user'), 'exclude': lambda f: f is None }})
    r"""columns and relationships of \\"users\\" """
    



@dataclass_json(undefined=Undefined.EXCLUDE)

@dataclasses.dataclass
class GetUserSelf200ApplicationJSON:
    r"""Responses for GET /me"""
    user_details: Optional[list[GetUserSelf200ApplicationJSONUserDetails]] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('user_details'), 'exclude': lambda f: f is None }})
    




@dataclasses.dataclass
class GetUserSelfResponse:
    content_type: str = dataclasses.field()
    status_code: int = dataclasses.field()
    get_user_self_200_application_json_object: Optional[GetUserSelf200ApplicationJSON] = dataclasses.field(default=None)
    r"""Responses for GET /me"""
    raw_response: Optional[requests_http.Response] = dataclasses.field(default=None)
    
