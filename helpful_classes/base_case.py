import json.decoder
from requests import Response


#class BaseCase:

    # def get_json_value(self, response: Response, name):
    #     try:
    #         response_as_dict = response.json()
    #     except json.decoder.JSONDecodeError:
    #         assert False, f"Response is not in JSON format. Response text in '{response.text}'"
    #
    #     assert name in response_as_dict, f"Response JSON does not have key '{name}'"
    #
    #     return response_as_dict[name]
