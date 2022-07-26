"""
    Ledger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v1.7.0-beta.2
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
from ledgerclient.model.get_balances200_response import GetBalances200Response
from ledgerclient.model.get_balances_aggregated200_response import GetBalancesAggregated200Response
from ledgerclient.model.get_balances_aggregated400_response import GetBalancesAggregated400Response
from ledgerclient.model.list_accounts400_response import ListAccounts400Response


class BalancesApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.get_balances_endpoint = _Endpoint(
            settings={
                'response_type': (GetBalances200Response,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/{ledger}/balances',
                'operation_id': 'get_balances',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ledger',
                    'address',
                    'after',
                    'pagination_token',
                ],
                'required': [
                    'ledger',
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
                    'address':
                        (str,),
                    'after':
                        (str,),
                    'pagination_token':
                        (str,),
                },
                'attribute_map': {
                    'ledger': 'ledger',
                    'address': 'address',
                    'after': 'after',
                    'pagination_token': 'pagination_token',
                },
                'location_map': {
                    'ledger': 'path',
                    'address': 'query',
                    'after': 'query',
                    'pagination_token': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self.get_balances_aggregated_endpoint = _Endpoint(
            settings={
                'response_type': (GetBalancesAggregated200Response,),
                'auth': [
                    'basicAuth'
                ],
                'endpoint_path': '/{ledger}/aggregate/balances',
                'operation_id': 'get_balances_aggregated',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'ledger',
                    'address',
                ],
                'required': [
                    'ledger',
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
                    'address':
                        (str,),
                },
                'attribute_map': {
                    'ledger': 'ledger',
                    'address': 'address',
                },
                'location_map': {
                    'ledger': 'path',
                    'address': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def get_balances(
        self,
        ledger,
        **kwargs
    ):
        """Get the balances from a ledger's account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_balances(ledger, async_req=True)
        >>> result = thread.get()

        Args:
            ledger (str): Name of the ledger.

        Keyword Args:
            address (str): Filter balances involving given account, either as source or destination.. [optional]
            after (str): Pagination cursor, will return accounts after given address, in descending order.. [optional]
            pagination_token (str): Parameter used in pagination requests.  Set to the value of next for the next page of results.  Set to the value of previous for the previous page of results.. [optional]
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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            GetBalances200Response
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['ledger'] = \
            ledger
        return self.get_balances_endpoint.call_with_http_info(**kwargs)

    def get_balances_aggregated(
        self,
        ledger,
        **kwargs
    ):
        """Get the aggregated balances from selected accounts  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_balances_aggregated(ledger, async_req=True)
        >>> result = thread.get()

        Args:
            ledger (str): Name of the ledger.

        Keyword Args:
            address (str): Filter balances involving given account, either as source or destination.. [optional]
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
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            _request_auths (list): set to override the auth_settings for an a single
                request; this effectively ignores the authentication
                in the spec for a single request.
                Default is None
            async_req (bool): execute request asynchronously

        Returns:
            GetBalancesAggregated200Response
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
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['_request_auths'] = kwargs.get('_request_auths', None)
        kwargs['ledger'] = \
            ledger
        return self.get_balances_aggregated_endpoint.call_with_http_info(**kwargs)

