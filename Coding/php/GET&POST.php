<!-- 
GET method:

The GET method is used to request data from a server.

It is an idempotent and safe method, meaning it should not have any side 
effects on the server and can be repeated without changing the server state.

In a GET request, the data is appended to the URL as query parameters.

The data sent using GET method is visible in the URL, making it less secure 
for sensitive information like passwords.

GET requests can be bookmarked, cached, and shared, as they have a direct 
impact on the URL.
 -->

<!-- 
POST method:

IT IS USED TO SEND ASCII AS WELL AS IMAGES AND DOCUMENTS !!!!!!
THE INFORMATION SHARED VIA POST METHOD IS SECURE !!!!

The POST method is used to submit data to be processed by the server.

It is not idempotent, as repeated POST requests can have different effects 
on the server.

In a POST request, the data is sent in the body of the request.

The data sent using POST method is not visible in the URL, providing better 
security for sensitive information.

POST requests are not bookmarked, cached, or shared directly through the URL.

Does not have any restriction an data size to be sent


 -->


In summary, the GET method is used to retrieve data from a server, while the 
POST method is used to send data to a server for processing. The choice between 
GET and POST depends on the nature of the data and the intended operation. 
GET requests are suitable for retrieving data, while POST requests are used for 
actions that modify server state or submit form data.
