# PRICE CLIENT ARCHITECTURE
The PRICE client follows a common serialization/abstraction client architecture, where each client call requires a request model, a response model, and a single REST call to a predefined server. 

## Requirements
* **Python 3.6+**
* **Python Packages**: There a few external python packages that need to be installed for the client to be functional:
  * [Requests](https://requests.readthedocs.io/en/master/)
  * [PrettyTable](https://pypi.org/project/PrettyTable/) - [Tutorial/Documentation](http://zetcode.com/python/prettytable/) 
  
  These should be installed as part of the setup process, but currently, the setup process is not including these packages. (setup.py needs to be debugged; packages are listed, but are not being installed - _pip security/SSL Cert issues_? Chris will look into possible  --trusted-host configuration options.)
* **Access**: In order to be able to connect to the PRICE APIs, credentials, endpoints, and database IDs need to be provided to the user(s)/automation.

## Client Call Code Flow

The client will:
 * use the parameters provided via the client call to create a request model,
 * the request model will be used to populate the data for the HTTP URL & payload based on the specific call, 
 * establish a connection to the target server and transmit the request, 
 * receive a response from the server, 
 * marshall the JSON data portion of the REST response into a response model, and 
 * return the response data model to the user.

**High level overview of client workflow**: 

1) User makes an API SDK client call with the required data. 
1) Marshall the data into the request model and convert to request format: URL parameters, headers, payloads. 
1) Make a REST call to the target PRICE endpoint and receive the server response.
1) Deserialize the JSON response data into the corresponding response model.
1) Return the response model (object) to the user.

### Request Model
The request model is class that is instantiated based on the client call parameters. The request model will serialize the data and provide the necessary methods for transforming the parameters into the various formats required to make the REST call. Class methods will do one of the following:
 * Take the URL parameters and convert them to a dictionary for conversion to HTTP parameters:
 
        <url>?arg1=val1%arg2=val2
 
 * Take API-specific parameters and build a JSON blob to be sent as the request payload,
 * Take request-specific parameters and build a dictionary for conversion to an API request header:
 
       content_type: application/json
       compression:  application/bzip
 
### REST Call
The REST call is the actual HTTP request made to the server using Python's [Requests](https://requests.readthedocs.io/en/master/) 3rd party library on [pypi](https://pypi.org/). 
   
### Response Model
The response model class will deserialize the JSON-formatted API response into a corresponding response object. The object abstracts the specific JSON format from the consumer (e.g. - tests), so if the response format structure changes, the model logic will be updated but consumers of the model will not be required to modify their existing logic.  

* *response_model.response* 
   
   The actual requests Response object.

* *response_model.response.raw* 
   
   The Response object will also contain the raw HTTP response, for inspection as needed.

* *response_model.status*
 
   The response status from the REST call. This is also in the raw response (response_model.response.raw), but is exposed in the response_model for simplification/ease of use. 

# CODE ORGANIZATION
**NOTE**: Code organization is based on the hierarchy outlined in the [API documentation](https://confluence.pclender.com/display/technicalwiki/PRICE+API+User+Guide).
 * **Call domains**
 
    The client is organized as a primary client with various domain-specific clients instantiated within the primary client. The primary client is instantiated using either the server's IP address or the fully qualified domain name (FQDN), server port, and database id. The information will be passed to the domain-specific clients (although the domain-specific clients can be instantiated individually also).
    
    **Primary Client**:
        
        from APIs.loans.client import LoanClient
        my_client = LoanClient(base_url="https://my_server.foo.com", database=123456789, port=8080)

    **Domain-Specific Clients**: 
    
        my_client.loans.get_loan_detail()
    
    or 
    
        loan_client = my_client.loans
        loan_client.get_loan_detail()
         
     
 
 * **Implementation Directory Structure**
 
    The code is broken into `APIs`, `base` (common) modules, docs, and non-API specific modules, such as logging and tests.
    
    * **BASE model Modules** 
    
       The `base` modules contain the abstracted, base classes used to define most API calls and code that is common to the basic response model. The `base` classes include abstracted request and response models, clients, mocks (used for testing and replacing the  [Requests](https://requests.readthedocs.io/en/master/) model, when it was not available during the initial development effort, and to be leveraged during unit testing.)  
    
        *Note: There are two basic response models:*
    
      * _base.responses.base_response.BaseResponse()_
    
        This is the common response model: common routines required to marshall the request response into the response object and store various elements as attributes within the class model. All responses are based on this model. This model does not enforce a specific JSON response, but provides the foundation for creating any response from JSON.
        
      * _base.common.response.CommonResponse(BaseResponse)_
       
        Almost all **PRICE API** responses have a common set of JSON elements. This class defines that common response model, which can be supplemented with additional attributes (using Class level variables). In many cases, the API response model is fully defined by this model (without any additional augmentation).
      
    * **API definition Modules**
    
      * The first level of organization (directories) is by domain: _assets, company, fees, income, etc._
      
      * The second level of organization is by model/class purpose: _models, requests, and responses_. There is also a client.py that contains the definition of the domain client, using the models, requests, and responses, based on the specific API call.
      
        Within each directory are files containing the class definitions for each API method. The request and response model class names end with _request_ and _response_, to indicate the model's primary purpose.
        
    * **Docs**
    
       * This contains the package/module documents, such as _this_ document.
        
    * **Non-API-Specific Modules**
     
      * _logger.logger.logging.Logger()_ 

          This includes the logging module (used for output to logs/stdout; logging is based on message level (_fatal, critical, warning, info, debug_) )

      * _tests_.*
      
          Basic routines for data generation and payload validation. Used for testing only.          
       
    
 # REQUEST MODEL ARCHITECTURE
 * **Base Request Model**
   * **_Class_**:
   * **_Assumptions_**:
   * **_Usage_**:
   
 * **ModelKey Classes**
   * **_Class/Architecture_**: 
   * **_Usage_**:
 
# RESPONSE MODEL ARCHITECTURE
 * **Base Response Models**
 
     Most API responses, while specific and unique, have a common (core) set of attributes. (See the [API documentation](https://confluence.pclender.com/display/technicalwiki/PRICE+API+User+Guide).) This commonality forms the definition of the base response model.  
   * **Class: BaseResponse** (_PRICE.base.responses.base_response.BaseResponse_)
   
       * **_Description_**: This base class is for a single instance within the response (vs. a list context of elements). This class is architected to be generalized and abstracted; it is not meant to be instantiated directly. The base class should be a superclass (inherited from) for a given API response. The base class will create:
         
            * the common (base) set of attributes 
            * specific attributes provided to the class at instantiation (ADD_KEYS and SUB_MODELS lists). 

       * **_Assumptions_**: 
       
       * **_Usage_**: 
   
   * **Class: BaseListResponse** (_PRICE.base.responses.base_response.BaseListResponse_)
   
       * **_Description_**: This base class defined as a list context of common elements (models). This class is architected to be generalized and abstracted; it is not meant to be instantiated directly. The base class should be a superclass (inherited from) for a given API response. The base class will:
         
            * create a list context model,
            * populate the model with a common submodel as elements of the list. (SUB_MODEL - single model type)
        
       * **_Assumptions_**:
       * **_Usage_**:
     
 * **Specific Response Models**
    * **Class**:
    * **_Assumptions_**:
    * **_Usage_**:
     
 * **ModelKey Classes**
    * **_Class/Architecture_**:
    * **_Usage_**:
    
 * **Enumeration Classes**
    * **_Why ENUM Classes?_**
    
        [Enums](https://docs.python.org/3/library/enum.html) allow "enumeration" of data so that various data elements that have a numeric value can be "aliased" to a meaningful description, abstracting the value from the code. Enumeration also allows creating and separating specific behaviors and data manipulation to a given enumeration class, creating a better, abstracted DRY approach. (**DRY** - _Don't Repeat Yourself_)
    
        _Code Example_: [Class LoanLicenceDataFrom(Enum)](../APIs/loans/requests/get_loan_license_data.py)

        Please refer to the Enums link above to learn how to reference and manipulate ENUMs and  their data/values.

## CLIENT HIERARCHY AND ORGANIZATION  
* **Client Organization**
    * **_Primary Client_**:
    * **_Domain Client_**:
    * **_Subdomain Client_**:

-------------------------------------------------

* **_Instantiation_**

    The basic client call is used as follows:
    * Instantiate the client with the primary/base endpoint, database name, and port (optional). Additional arguments are available depending on usage; but for the simple case, the additional arguments are not required.

            from APIs.loans.client import LoanClient
        
            my_client = LoanClient(base_url="https://my_server.foo.com", database=123456789, port=8080)

    * Make the client call with required parameters. 

            my_response = my_client.loans.get_loan_details()

    * Get the marshalled response; the actual JSON response payload is marshalled (populated) into an object, but the original/raw JSON response is also available in the marshalled response object.

            print(my_response.Field1.Field2)   # Marshalled data based on the JSON payload format.
            print(my_response.status)          # HTTP Status code (200, 201, 404, 500, etc.)
            print(my_response.content)         # JSON-formatted response

    See the [Requests](https://requests.readthedocs.io/en/master/) documentation for additional information that is available in the response **my_response._response_** object.

---------------------------------------------

* _**Client Simplification**_:
  
     The client uses a hierarchical structure, based on the purpose of the calls:
     
        from APIs.loans.client import LoanClient
        my_client = LoanClient(base_url="https://my_server.foo.com", database=123456789, port=8080)
        
        my_client.loans.<methods>
        my_client.income.<methods>
        my_client.liability.<methods>
        
     For simplicity, if a majority of the sub-clients are not needed, the sub-client can be referenced directly:

        from APIs.loans.client import LoanClient
        my_client = LoanClient(base_url="https://my_server.foo.com", database=123456789, port=8080)
        loan_client = my_client.loans
        liab_client = my_client.liabaility
            
        loan_client.<methods>
        liab_client.<methods>
        

### Endpoints
In the code, the client has a specific resource endpoint, which is appended to the primary endpoint, port, and database:

Given a base endpoint and database that was provided during client instantiation: 
    
         base_url = https://my_server.foo.com
         port = 8088
         database = my_database

and the specific API endpoint:
    
         get_loan_details
         
The final endpoint will be:
    
         https://my_server.foo.com:8088/my_database/get_loan_details

# UNIT TESTS
**Organization and files**

The primary focus of the unittests is not verify the specific code implementation, but the behavior of the code, based on various inputs and outputs of the routines. The unittests do not required external sources, as Python's [Requests](https://requests.readthedocs.io/en/master/) library has been mocked (_PRICE.base.mocks.mock_requests.py_).

* **Execution**
 
    To execute the tests:
 
      python -m unittest <test_file_name.py> [<TestClassName>.<test_method>] [-v[v[v]]]

    Specific test classes or test methods can be executed (as shown above). 

    If those arguments are not provided, [unittest](https://docs.python.org/3.8/library/unittest.html) will scan the directories for any file with the **_test\<filename>_** file spec, instantiate any class with **_Test\<Class>_** name and all methods within the class that are named **_test_\<testname>**.
    
    _Verbosity_:
    
    `-v`: verbose ==> `-vv`: increased verbosity ==> `-vvv`: maximum verbosity

* **Issues**

    Currently, the tests are contained in the root/base directory. They should be in a unittest directory, but there are issues with imports in a Windows environment that are "_resolved_" by keeping them in the base directory.


* **Future Enhancements**
 
    TBD
