# GetModels3dIDResponse


## Fields

| Field                                                                                                   | Type                                                                                                    | Required                                                                                                | Description                                                                                             |
| ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                          | *str*                                                                                                   | :heavy_check_mark:                                                                                      | HTTP response content type for this operation                                                           |
| `status_code`                                                                                           | *int*                                                                                                   | :heavy_check_mark:                                                                                      | HTTP response status code for this operation                                                            |
| `raw_response`                                                                                          | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                   | :heavy_minus_sign:                                                                                      | Raw HTTP response; suitable for custom response parsing                                                 |
| `get_models_3d_id_200_application_json_object`                                                          | [Optional[GetModels3dID200ApplicationJSON]](../../models/operations/getmodels3did200applicationjson.md) | :heavy_minus_sign:                                                                                      | Responses for GET /api/rest/v1/models-3d/{id}                                                           |