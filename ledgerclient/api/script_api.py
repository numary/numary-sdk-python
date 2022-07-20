"""
    Ledger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.6.1
    Contact: support@numary.com
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from ledgerclient.api_client import ApiClient, Endpoint as _Endpoint
from ledgerclient.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from ledgerclient.model.script import Script
from ledgerclient.model.script_result import ScriptResult


class ScriptApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.run_script_endpoint = _Endpoint(
            settings={
                'response_type': (ScriptResult,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/{ledger}/script',
                'operation_id': 'run_script',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'ledger',
                    'script',
                    'preview',
                ],
                'required': [
                    'ledger',
                    'script',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'ledger':
                        (str,),
                    'script':
                        (Script,),
                    'preview':
                        (bool,),
                },
                'attribute_map': {
                    'ledger': 'ledger',
                    'preview': 'preview',
                },
                'location_map': {
                    'ledger': 'path',
                    'script': 'body',
                    'preview': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def run_script(
        self,
        ledger,
        script,
        **kwargs
    ):
        """Execute a Numscript.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.run_script(ledger, script, async_req=True)
        >>> result = thread.get()

        Args:
            ledger (str): Name of the ledger.
            script (Script):

        Keyword Args:
            preview (bool): Set the preview mode. Preview mode doesn't add the logs to the database or publish a message to the message broker.. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ScriptResult
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', True
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', True
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['ledger'] = \
            ledger
        kwargs['script'] = \
            script
        return self.run_script_endpoint.call_with_http_info(**kwargs)

