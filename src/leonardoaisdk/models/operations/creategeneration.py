"""Code generated by Speakeasy (https://speakeasyapi.dev). DO NOT EDIT."""

from __future__ import annotations
import dataclasses
import requests as requests_http
from ...models.shared import controlnet_type as shared_controlnet_type
from ...models.shared import element_input as shared_element_input
from ...models.shared import sd_generation_schedulers as shared_sd_generation_schedulers
from ...models.shared import sd_generation_style as shared_sd_generation_style
from ...models.shared import sd_versions as shared_sd_versions
from dataclasses_json import Undefined, dataclass_json
from enum import Enum
from leonardoaisdk import utils
from typing import List, Optional

class TransparencyType(str, Enum):
    r"""Which type of transparency this image should use"""
    DISABLED = 'disabled'
    FOREGROUND_ONLY = 'foreground_only'


@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateGenerationRequestBody:
    r"""Query parameters to be provided in the request body as a JSON object"""
    UNSET='__SPEAKEASY_UNSET__'
    alchemy: Optional[bool] = dataclasses.field(default=True, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('alchemy'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""Enable to use Alchemy. Note: The appropriate Alchemy version is selected for the specified model. For example, XL models will use Alchemy V2."""
    contrast_ratio: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('contrastRatio'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""Contrast Ratio to use with Alchemy. Must be a float between 0 and 1 inclusive."""
    control_net: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('controlNet'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""Enable to use ControlNet. Requires an init image to be provided. Requires a model based on SD v1.5"""
    control_net_type: Optional[shared_controlnet_type.ControlnetType] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('controlNetType'), 'exclude': lambda f: f is None }})
    r"""The type of ControlNet to use."""
    elements: Optional[List[shared_element_input.ElementInput]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('elements'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    expanded_domain: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('expandedDomain'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""Enable to use the Expanded Domain feature of Alchemy."""
    fantasy_avatar: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('fantasyAvatar'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""Enable to use the Fantasy Avatar feature."""
    guidance_scale: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('guidance_scale'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""How strongly the generation should reflect the prompt. 7 is recommended. Must be between 1 and 20."""
    height: Optional[int] = dataclasses.field(default=768, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('height'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""The input height of the images. Must be between 32 and 1024 and be a multiple of 8. Note: Input resolution is not always the same as output resolution due to upscaling from other features."""
    high_contrast: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('highContrast'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""Enable to use the High Contrast feature of Prompt Magic. Note: Controls RAW mode. Set to false to enable RAW mode."""
    high_resolution: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('highResolution'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""Enable to use the High Resolution feature of Prompt Magic."""
    image_prompt_weight: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('imagePromptWeight'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    image_prompts: Optional[List[str]] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('imagePrompts'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    init_generation_image_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('init_generation_image_id'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""The ID of an existing image to use in image2image."""
    init_image_id: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('init_image_id'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""The ID of an Init Image to use in image2image."""
    init_strength: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('init_strength'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""How strongly the generated images should reflect the original image in image2image. Must be a float between 0.1 and 0.9."""
    model_id: Optional[str] = dataclasses.field(default='b24e16ff-06e3-43eb-8d33-4416c2d75876', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('modelId'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""The model ID used for image generation. If not provided, uses sd_version to determine the version of Stable Diffusion to use. In-app, model IDs are under the Finetune Models menu. Click on the platform model or your custom model, then click View More. For platform models, you can also use the List Platform Models API."""
    negative_prompt: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('negative_prompt'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""The negative prompt used for the image generation"""
    num_images: Optional[int] = dataclasses.field(default=4, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('num_images'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""The number of images to generate. Must be between 1 and 8. If either width or height is over 768, must be between 1 and 4."""
    num_inference_steps: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('num_inference_steps'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""The Step Count to use for the generation. Must be between 10 and 60. Default is 15."""
    photo_real: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('photoReal'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""Enable the photoReal feature. Requires enabling alchemy and unspecifying modelId (for photoRealVersion V1)."""
    photo_real_strength: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('photoRealStrength'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""Depth of field of photoReal. Must be 0.55 for low, 0.5 for medium, or 0.45 for high. Defaults to 0.55 if not specified."""
    photo_real_version: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('photoRealVersion'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""The version of photoReal to use. Must be v1 or v2."""
    preset_style: Optional[shared_sd_generation_style.SdGenerationStyle] = dataclasses.field(default=shared_sd_generation_style.SdGenerationStyle.DYNAMIC, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('presetStyle'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""The style to generate images with. When photoReal is enabled, refer to the Guide section for a full list. When alchemy is disabled, use LEONARDO or NONE. When alchemy is enabled, use ANIME, CREATIVE, DYNAMIC, ENVIRONMENT, GENERAL, ILLUSTRATION, PHOTOGRAPHY, RAYTRACED, RENDER_3D, SKETCH_BW, SKETCH_COLOR, or NONE."""
    prompt: Optional[str] = dataclasses.field(default='A majestic cat in the snow', metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('prompt'), 'exclude': lambda f: f is None }})
    r"""The prompt used to generate images"""
    prompt_magic: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('promptMagic'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""Enable to use Prompt Magic."""
    prompt_magic_strength: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('promptMagicStrength'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""Strength of prompt magic. Must be a float between 0.1 and 1.0"""
    prompt_magic_version: Optional[str] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('promptMagicVersion'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""Prompt magic version v2 or v3, for use when promptMagic: true"""
    public: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('public'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""Whether the generated images should show in the community feed."""
    scheduler: Optional[shared_sd_generation_schedulers.SdGenerationSchedulers] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('scheduler'), 'exclude': lambda f: f is None }})
    r"""The scheduler to generate images with. Defaults to EULER_DISCRETE if not specified."""
    sd_version: Optional[shared_sd_versions.SdVersions] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sd_version'), 'exclude': lambda f: f is None }})
    r"""The base version of stable diffusion to use if not using a custom model. v1_5 is 1.5, v2 is 2.1, if not specified it will default to v1_5. Also includes SDXL and SDXL Lightning models"""
    seed: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('seed'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    tiling: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('tiling'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""Whether the generated images should tile on all axis."""
    transparency: Optional[TransparencyType] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('transparency'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""Which type of transparency this image should use"""
    unzoom: Optional[bool] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unzoom'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""Whether the generated images should be unzoomed (requires unzoomAmount and init_image_id to be set)."""
    unzoom_amount: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('unzoomAmount'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""How much the image should be unzoomed (requires an init_image_id and unzoom to be set to true)."""
    upscale_ratio: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('upscaleRatio'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""How much the image should be upscaled. (Enterprise Only)"""
    weighting: Optional[float] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('weighting'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""How much weighting to use for ControlNet. This parameter works with controlNet and controlNetType."""
    width: Optional[int] = dataclasses.field(default=1024, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('width'), 'exclude': lambda f: f is CreateGenerationRequestBody.UNSET }})
    r"""The input width of the images. Must be between 32 and 1024 and be a multiple of 8. Note: Input resolution is not always the same as output resolution due to upscaling from other features."""
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class SDGenerationOutput:
    UNSET='__SPEAKEASY_UNSET__'
    api_credit_cost: Optional[int] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('apiCreditCost'), 'exclude': lambda f: f is SDGenerationOutput.UNSET }})
    r"""API Credits Cost for Image Generation. Available for Production API Users."""
    generation_id: Optional[str] = dataclasses.field(default=None, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('generationId'), 'exclude': lambda f: f is None }})
    



@dataclass_json(undefined=Undefined.EXCLUDE)
@dataclasses.dataclass
class CreateGenerationResponseBody:
    r"""Responses for POST /generations"""
    UNSET='__SPEAKEASY_UNSET__'
    sd_generation_job: Optional[SDGenerationOutput] = dataclasses.field(default=UNSET, metadata={'dataclasses_json': { 'letter_case': utils.get_field_name('sdGenerationJob'), 'exclude': lambda f: f is CreateGenerationResponseBody.UNSET }})
    



@dataclasses.dataclass
class CreateGenerationResponse:
    content_type: str = dataclasses.field()
    r"""HTTP response content type for this operation"""
    status_code: int = dataclasses.field()
    r"""HTTP response status code for this operation"""
    raw_response: requests_http.Response = dataclasses.field()
    r"""Raw HTTP response; suitable for custom response parsing"""
    object: Optional[CreateGenerationResponseBody] = dataclasses.field(default=None)
    r"""Responses for POST /generations"""
    

