# Python API client for Numary

No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1.7.1
- Package version: v1.7.1
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python >= 3.6

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/numary/numary-sdk-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/numary/numary-sdk-python.git`)

Then import the package:
```python
import ledgerclient
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import ledgerclient
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import time
import ledgerclient
from pprint import pprint
from ledgerclient.api import accounts_api
from ledgerclient.model.get_account200_response import GetAccount200Response
from ledgerclient.model.get_account400_response import GetAccount400Response
from ledgerclient.model.list_accounts200_response import ListAccounts200Response
from ledgerclient.model.list_accounts400_response import ListAccounts400Response
from ledgerclient.model.metadata import Metadata
# Defining the host is optional and defaults to https://.o.numary.cloud/ledger
# See configuration.py for a list of all supported configuration parameters.
configuration = ledgerclient.Configuration(
    host = "https://.o.numary.cloud/ledger"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure HTTP basic authorization: basicAuth
configuration = ledgerclient.Configuration(
    username = 'YOUR_USERNAME',
    password = 'YOUR_PASSWORD'
)


# Enter a context with an instance of the API client
with ledgerclient.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = accounts_api.AccountsApi(api_client)
    ledger = "ledger001" # str | Name of the ledger.
    address = "users:001" # str | Exact address of the account. It must match the following regular expressions pattern: ``` ^\\w+(:\\w+)*$ ``` 
    metadata = Metadata(
        key=None,
    ) # Metadata | metadata

    try:
        # Add metadata to an account.
        api_instance.add_metadata_to_account(ledger, address, metadata)
    except ledgerclient.ApiException as e:
        print("Exception when calling AccountsApi->add_metadata_to_account: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://.o.numary.cloud/ledger*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AccountsApi* | [**add_metadata_to_account**](docs/AccountsApi.md#add_metadata_to_account) | **POST** /{ledger}/accounts/{address}/metadata | Add metadata to an account.
*AccountsApi* | [**count_accounts**](docs/AccountsApi.md#count_accounts) | **HEAD** /{ledger}/accounts | Count the accounts from a ledger.
*AccountsApi* | [**get_account**](docs/AccountsApi.md#get_account) | **GET** /{ledger}/accounts/{address} | Get account by its address.
*AccountsApi* | [**list_accounts**](docs/AccountsApi.md#list_accounts) | **GET** /{ledger}/accounts | List accounts from a ledger.
*BalancesApi* | [**get_balances**](docs/BalancesApi.md#get_balances) | **GET** /{ledger}/balances | Get the balances from a ledger&#39;s account
*BalancesApi* | [**get_balances_aggregated**](docs/BalancesApi.md#get_balances_aggregated) | **GET** /{ledger}/aggregate/balances | Get the aggregated balances from selected accounts
*MappingApi* | [**get_mapping**](docs/MappingApi.md#get_mapping) | **GET** /{ledger}/mapping | Get the mapping of a ledger.
*MappingApi* | [**update_mapping**](docs/MappingApi.md#update_mapping) | **PUT** /{ledger}/mapping | Update the mapping of a ledger.
*ScriptApi* | [**run_script**](docs/ScriptApi.md#run_script) | **POST** /{ledger}/script | Execute a Numscript.
*ServerApi* | [**get_info**](docs/ServerApi.md#get_info) | **GET** /_info | Show server information.
*StatsApi* | [**read_stats**](docs/StatsApi.md#read_stats) | **GET** /{ledger}/stats | Get Stats
*TransactionsApi* | [**add_metadata_on_transaction**](docs/TransactionsApi.md#add_metadata_on_transaction) | **POST** /{ledger}/transactions/{txid}/metadata | Set the metadata of a transaction by its ID.
*TransactionsApi* | [**count_transactions**](docs/TransactionsApi.md#count_transactions) | **HEAD** /{ledger}/transactions | Count the transactions from a ledger.
*TransactionsApi* | [**create_transaction**](docs/TransactionsApi.md#create_transaction) | **POST** /{ledger}/transactions | Create a new transaction to a ledger.
*TransactionsApi* | [**create_transactions**](docs/TransactionsApi.md#create_transactions) | **POST** /{ledger}/transactions/batch | Create a new batch of transactions to a ledger.
*TransactionsApi* | [**get_transaction**](docs/TransactionsApi.md#get_transaction) | **GET** /{ledger}/transactions/{txid} | Get transaction from a ledger by its ID.
*TransactionsApi* | [**list_transactions**](docs/TransactionsApi.md#list_transactions) | **GET** /{ledger}/transactions | List transactions from a ledger.
*TransactionsApi* | [**revert_transaction**](docs/TransactionsApi.md#revert_transaction) | **POST** /{ledger}/transactions/{txid}/revert | Revert a ledger transaction by its ID.


## Documentation For Models

 - [Account](docs/Account.md)
 - [AccountWithVolumesAndBalances](docs/AccountWithVolumesAndBalances.md)
 - [AccountsBalances](docs/AccountsBalances.md)
 - [AggregatedVolumes](docs/AggregatedVolumes.md)
 - [AssetsBalances](docs/AssetsBalances.md)
 - [Config](docs/Config.md)
 - [ConfigInfo](docs/ConfigInfo.md)
 - [ConfigInfoResponse](docs/ConfigInfoResponse.md)
 - [Contract](docs/Contract.md)
 - [CreateTransaction400Response](docs/CreateTransaction400Response.md)
 - [CreateTransaction409Response](docs/CreateTransaction409Response.md)
 - [CreateTransactions400Response](docs/CreateTransactions400Response.md)
 - [Cursor](docs/Cursor.md)
 - [ErrorCode](docs/ErrorCode.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [GetAccount200Response](docs/GetAccount200Response.md)
 - [GetAccount400Response](docs/GetAccount400Response.md)
 - [GetBalances200Response](docs/GetBalances200Response.md)
 - [GetBalances200ResponseCursor](docs/GetBalances200ResponseCursor.md)
 - [GetBalances200ResponseCursorAllOf](docs/GetBalances200ResponseCursorAllOf.md)
 - [GetBalancesAggregated200Response](docs/GetBalancesAggregated200Response.md)
 - [GetBalancesAggregated400Response](docs/GetBalancesAggregated400Response.md)
 - [GetTransaction400Response](docs/GetTransaction400Response.md)
 - [GetTransaction404Response](docs/GetTransaction404Response.md)
 - [LedgerStorage](docs/LedgerStorage.md)
 - [ListAccounts200Response](docs/ListAccounts200Response.md)
 - [ListAccounts200ResponseCursor](docs/ListAccounts200ResponseCursor.md)
 - [ListAccounts200ResponseCursorAllOf](docs/ListAccounts200ResponseCursorAllOf.md)
 - [ListAccounts400Response](docs/ListAccounts400Response.md)
 - [ListTransactions200Response](docs/ListTransactions200Response.md)
 - [ListTransactions200ResponseCursor](docs/ListTransactions200ResponseCursor.md)
 - [ListTransactions200ResponseCursorAllOf](docs/ListTransactions200ResponseCursorAllOf.md)
 - [Mapping](docs/Mapping.md)
 - [MappingResponse](docs/MappingResponse.md)
 - [Metadata](docs/Metadata.md)
 - [Posting](docs/Posting.md)
 - [Script](docs/Script.md)
 - [ScriptResult](docs/ScriptResult.md)
 - [Stats](docs/Stats.md)
 - [StatsResponse](docs/StatsResponse.md)
 - [Transaction](docs/Transaction.md)
 - [TransactionData](docs/TransactionData.md)
 - [TransactionResponse](docs/TransactionResponse.md)
 - [Transactions](docs/Transactions.md)
 - [TransactionsResponse](docs/TransactionsResponse.md)
 - [Volume](docs/Volume.md)
 - [Volumes](docs/Volumes.md)


## Documentation For Authorization


## basicAuth

- **Type**: HTTP basic authentication


## Author

support@numary.com


## Notes for Large OpenAPI documents
If the OpenAPI document is large, imports in ledgerclient.apis and ledgerclient.models may fail with a
RecursionError indicating the maximum recursion limit has been exceeded. In that case, there are a couple of solutions:

Solution 1:
Use specific imports for apis and models like:
- `from ledgerclient.api.default_api import DefaultApi`
- `from ledgerclient.model.pet import Pet`

Solution 2:
Before importing the package, adjust the maximum recursion limit as shown below:
```
import sys
sys.setrecursionlimit(1500)
import ledgerclient
from ledgerclient.apis import *
from ledgerclient.models import *
```

