# GetVariationByIDResponse


## Fields

| Field                                                                                                         | Type                                                                                                          | Required                                                                                                      | Description                                                                                                   |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| `content_type`                                                                                                | *str*                                                                                                         | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `status_code`                                                                                                 | *int*                                                                                                         | :heavy_check_mark:                                                                                            | N/A                                                                                                           |
| `raw_response`                                                                                                | [requests.Response](https://requests.readthedocs.io/en/latest/api/#requests.Response)                         | :heavy_minus_sign:                                                                                            | N/A                                                                                                           |
| `get_variation_by_id_200_application_json_object`                                                             | [Optional[GetVariationByID200ApplicationJSON]](../../models/operations/getvariationbyid200applicationjson.md) | :heavy_minus_sign:                                                                                            | Responses for GET /variations/{id}                                                                            |