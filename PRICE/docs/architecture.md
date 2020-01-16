# PRICE CLIENT ARCHITECTURE
The PRICE client follows a common serialization/abstraction client architecture, where each client call requires a request model, a response model, and a single REST call to a predefined server. 

## Request Model
The request model is class that is instantiated based on the client call parameters. The request model will serialize the data and provide the necessary methods for transforming the parameters into the various formats required to make the REST call. Class methods will do one of the following:
 * take the URL parameters and convert them to a dictionary for conversion to HTTP parameters:
 
        <url>?arg1=val1%arg2=val2
 
 * take API-specific parameters and build a JSON blob to be sent as the request payload,
 * take request-specific parameters and build a dictionary for conversion to an API request header.
 
       content_type: application/JSON   
       compression:  application/bzip  
 
## REST Call
The REST call is the actual HTTP call to the server. The client will use the request model to populate the data for the HTTP call, establish a connection to the target server, transmit the data, and receive a response from the server. The client will take the JSON data portion of the response, instantiate a response model using the data, and return the response data model to the user.
 
  
## Response Model
The response model class will deserialize the JSON-formatted API response into a corresponding response object. The object abstracts the specific JSON format from the consumer (e.g. - tests), so if the response format structure changes, the model logic will be updated but consumers of the model will not be required to modify their existing logic.

# CODE ORGANIZATION
\[**NOTE**: Based on API documentation on confluence - provide doc link.]
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
    
* **Usage**
    * *Instantiation and intermediate use:*
     
          client.loans.get_loan() vs. loans.get_loan()
 
  

# UNIT TESTS
* **Organization and files**
* **Execution**
 
      python -m unittest \<file.py> [\<TestClassName>\<test_method>] [-v[v[v]]]
      
* **Issues**
* **Future Enhancements**
 