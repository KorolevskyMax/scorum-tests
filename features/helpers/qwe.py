from helpers.api_wrapper import Api

from helpers.json_validator import validate_schema

api = Api("https://rpc.scorum.com")
# api = Api("https://node3.scorum.com/jsonrpc")

resp = api.get_blocks(**{"block_id": 1})
validate_schema(resp.json(), 'get_blocks')
print (resp.json())
resp = api.get_blocks(**{"block_id": 2})
validate_schema(resp.json(), 'get_blocks')
print (resp.json())
resp = api.get_blocks(**{"block_id": -1})
# validate_schema(resp.json(), 'get_blocks')
print (resp.json())
resp = api.get_dynamic_global_properties()
validate_schema(resp.json(), 'get_dynamic_global_properties')
print (resp.json())
