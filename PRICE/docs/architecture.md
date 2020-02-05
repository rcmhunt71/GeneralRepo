# PRICE CLIENT ARCHITECTURE
The PRICE client follows a common serialization/abstraction client architecture, where each client call requires a request model, a response model, and a single REST call to a predefined server. 

## Client Call Code Flow

The client will:
 * use the parameters provided via the client call to create a request model,
 * the request model will be used to populate the data for the HTTP URL & payload based on the specific call, 
 * establish a connection to the target server and transmit the request, 
 * receive a response from the server, 
 * marshall the JSON data portion of the REST response into a response model, and 
 * return the response data model to the user.

### Request Model
The request model is class that is instantiated based on the client call parameters. The request model will serialize the data and provide the necessary methods for transforming the parameters into the various formats required to make the REST call. Class methods will do one of the following:
 * take the URL parameters and convert them to a dictionary for conversion to HTTP parameters:
 
        <url>?arg1=val1%arg2=val2
 
 * take API-specific parameters and build a JSON blob to be sent as the request payload,
 * take request-specific parameters and build a dictionary for conversion to an API request header.
 
       content_type: application/JSON   
       compression:  application/bzip  
 
### REST Call
The REST call is the actual HTTP request made to the server using Python's [Requests](https://requests.readthedocs.io/en/master/) 3rd party library on [pypi](https://pypi.org/). 
   
### Response Model
The response model class will deserialize the JSON-formatted API response into a corresponding response object. The object abstracts the specific JSON format from the consumer (e.g. - tests), so if the response format structure changes, the model logic will be updated but consumers of the model will not be required to modify their existing logic.  

*response_model.response* - The actual requests Response object.
*response_model.response.raw* - The Response object will also contain the raw HTTP response, for inspection as needed.
*response_model.status* - The response status from the REST call. This is also in the raw response (response_model.response.raw), but is exposed in the response_model for simplification/ease of use. 

# CODE ORGANIZATION
**NOTE**: Code organization is modeled after the [API documentation](https://confluence.pclender.com/display/technicalwiki/PRICE+API+User+Guide).
 * **Call domains (loans, assets, data, persons)**
 * **Directories**
    * *Models*
    * *Requests*
    * *Responses*
    * *Clients*
 
 # REQUEST MODEL ARCHITECTURE
 * **BaseRequest Model**
   * *Class*
   * *Assumptions*
   * *Usage*
   
 * **ModelKey Classes**
   * *Class/Architecture* 
   * *Usage*
 
# RESPONSE MODEL ARCHITECTURE
 * **BaseResponse Model** 
   * *Class*
   * *Assumptions*
   * *Usage*
   
 * **Common Response Model**
   * *Class*
   * *Assumptions*
   * *Usage*
   
 * **Specific Response Models**
    * *Class*
    * *Assumptions*
    * *Usage*
     
 * **ModelKey Classes**
    * *Class/Architecture*
    * *Usage*
    
 * **Enumeration Classes**
    * *Why ENUM Classes?*
    * *How to use*
 
## CLIENT HIERARCHY AND ORGANIZATION  
* **Client Organization**
    * *Primary Client*
    * *Domain Client*
    * *Subdomain Client*

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

* **Issues**

    Currently, the tests are contained in the root/base directory. They should be in a unittest directory, but there are issues with imports in a Windows environment that are "_resolved_" by keeping them in the base directory.


* **Future Enhancements**
 
    TBD
