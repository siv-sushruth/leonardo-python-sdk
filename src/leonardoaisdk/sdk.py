"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

import requests as requests_http
from .dataset import Dataset
from .elements import Elements
from .image import Image
from .init_images import InitImages
from .models_ import Models
from .motion import Motion
from .pricing_calculator import PricingCalculator
from .prompt import Prompt
from .realtime_canvas import RealtimeCanvas
from .sdkconfiguration import SDKConfiguration
from .texture import Texture
from .threed_model_assets import ThreeDModelAssets
from .user import User
from .utils.retries import RetryConfig
from .variation import Variation
from leonardoaisdk import utils
from leonardoaisdk._hooks import SDKHooks
from leonardoaisdk.models import shared
from typing import Callable, Dict, Optional, Union

class LeonardoAiSDK:
    r"""Rest Endpoints: Leonardo.Ai API OpenAPI specification."""
    dataset: Dataset
    elements: Elements
    image: Image
    realtime_canvas: RealtimeCanvas
    motion: Motion
    texture: Texture
    init_images: InitImages
    user: User
    models: Models
    three_d_model_assets: ThreeDModelAssets
    pricing_calculator: PricingCalculator
    prompt: Prompt
    variation: Variation

    sdk_configuration: SDKConfiguration

    def __init__(self,
                 bearer_auth: Union[str, Callable[[], str]],
                 server_idx: Optional[int] = None,
                 server_url: Optional[str] = None,
                 url_params: Optional[Dict[str, str]] = None,
                 client: Optional[requests_http.Session] = None,
                 retry_config: Optional[RetryConfig] = None
                 ) -> None:
        """Instantiates the SDK configuring it with the provided parameters.

        :param bearer_auth: The bearer_auth required for authentication
        :type bearer_auth: Union[str, Callable[[], str]]
        :param server_idx: The index of the server to use for all operations
        :type server_idx: int
        :param server_url: The server URL to use for all operations
        :type server_url: str
        :param url_params: Parameters to optionally template the server URL with
        :type url_params: Dict[str, str]
        :param client: The requests.Session HTTP client to use for all operations
        :type client: requests_http.Session
        :param retry_config: The utils.RetryConfig to use globally
        :type retry_config: RetryConfig
        """
        if client is None:
            client = requests_http.Session()

        if callable(bearer_auth):
            def security():
                return shared.Security(bearer_auth = bearer_auth())
        else:
            security = shared.Security(bearer_auth = bearer_auth)

        if server_url is not None:
            if url_params is not None:
                server_url = utils.template_url(server_url, url_params)
    

        self.sdk_configuration = SDKConfiguration(
            client,
            security,
            server_url,
            server_idx,
            retry_config=retry_config
        )

        hooks = SDKHooks()

        current_server_url, *_ = self.sdk_configuration.get_server_details()
        server_url, self.sdk_configuration.client = hooks.sdk_init(current_server_url, self.sdk_configuration.client)
        if current_server_url != server_url:
            self.sdk_configuration.server_url = server_url

        # pylint: disable=protected-access
        self.sdk_configuration.__dict__['_hooks'] = hooks

        self._init_sdks()


    def _init_sdks(self):
        self.dataset = Dataset(self.sdk_configuration)
        self.elements = Elements(self.sdk_configuration)
        self.image = Image(self.sdk_configuration)
        self.realtime_canvas = RealtimeCanvas(self.sdk_configuration)
        self.motion = Motion(self.sdk_configuration)
        self.texture = Texture(self.sdk_configuration)
        self.init_images = InitImages(self.sdk_configuration)
        self.user = User(self.sdk_configuration)
        self.models = Models(self.sdk_configuration)
        self.three_d_model_assets = ThreeDModelAssets(self.sdk_configuration)
        self.pricing_calculator = PricingCalculator(self.sdk_configuration)
        self.prompt = Prompt(self.sdk_configuration)
        self.variation = Variation(self.sdk_configuration)
