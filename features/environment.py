import logging

from helpers.api_wrapper import Api
from helpers.configuration_parser import CustomConfigParser


def before_all(context):
    context.config_name = context.config.userdata.get('config_name', 'config.ini')
    context.confParser = CustomConfigParser(file_name=context.config_name)
    context.response = dict()
    context.responses = dict()
    context.endpoint_url = ""
    context.api = dict()
    for url in context.confParser['API_URL'].keys():
        context.responses[url] = dict()
        context.api[url] = Api(context.confParser['API_URL'][url])


def before_feature(context, feature):
    logging.info("Feature: {}".format(feature.name))


def before_scenario(context, scenario):
    logging.info("\tScenario: {}".format(scenario.name))
    context.payload = dict()
    context.response, context.endpoint_url = None, None
    context.test_data = dict()
    context.additional_data = dict()


def before_step(context, step):
    context.step_name = step.name
    logging.info("\t\tStep: {} {}".format(step.keyword, step.name))


def after_step(context, step):
    if step.status == "failed":
        url = ''
        request_method = ''
        token = ''
        http_code = ''
        payload = ''

        try:
            url = context.response.request.url
        except:
            pass

        try:
            payload = context.response.request.body
        except:
            pass

        try:
            response = context.response.json()
        except:
            response = str(context.response)

        try:
            request_method = context.response.request.method
        except:
            pass

        try:
            http_code = context.response.status_code
        except:
            pass

        try:
            token = context.api.token
        except:
            pass

        logging.error(
            "\t\t\tERROR OCCURED:"
            "\n** last response: HTTP {}"
            "\n** url: {}"
            "\n** method: {}"
            "\n** token: {}"
            "\n** payload: {}"
            "\n** response: {}"
                .format(
                http_code,
                url,
                request_method,
                token,
                payload,
                response,
            )
        )