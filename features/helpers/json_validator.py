import json
import os
from jsonschema import validate


def validate_schema(response_json, json_schema_filename):
    here = os.path.abspath(os.path.dirname(__file__))
    with open(os.path.join(here, '../schemas/{}.json'.format(json_schema_filename))) as schema_file:
        schema = json.load(schema_file)
        validate(response_json, schema)
