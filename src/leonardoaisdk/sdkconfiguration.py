"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""


import requests as requests_http
from .utils import utils
from .utils.retries import RetryConfig
from dataclasses import dataclass
from leonardoaisdk.models import shared
from typing import Callable, Dict, Tuple, Union


SERVERS = [
    'https://cloud.leonardo.ai/api/rest/v1',
    # Leonardo.Ai API server
]
"""Contains the list of servers available to the SDK"""

@dataclass
class SDKConfiguration:
    client: requests_http.Session
    security: Union[shared.Security,Callable[[], shared.Security]] = None
    server_url: str = ''
    server_idx: int = 0
    language: str = 'python'
    openapi_doc_version: str = 'v1.0.0'
    sdk_version: str = '5.0.2'
    gen_version: str = '2.272.7'
    user_agent: str = 'speakeasy-sdk/python 5.0.2 2.272.7 v1.0.0 Leonardo-Ai-SDK'
    retry_config: RetryConfig = None

    def get_server_details(self) -> Tuple[str, Dict[str, str]]:
        if self.server_url:
            return utils.remove_suffix(self.server_url, '/'), {}
        if self.server_idx is None:
            self.server_idx = 0

        return SERVERS[self.server_idx], {}
