

a mockup for a URL checker on js that is ultra easy to implement.

In order to be able to request any url, overcoming the limitation of Access-Control-Allow-Origin in js, we will have to perform the request from the server, and then tell the answer to js from our own AJAX interface.

Ideally, we would like to keep configuration in one side (probably the js side of things) , provide an initial run before configuring and allow to configure afterwards.

# The goal

just a simple URL checker, that with a provided list of URL, it checks them on the press of a button, or in reload.

# The status

a mock to test how to check the url on js.

0.1 - using Skeleton.css, it shows a page with 4 sample tests, 2 valid and 2 failing, for 2 different url, one that fails and one that succedes (Example of how to check if a URL fails).



# Next features

- a better way of configuring it is desirable 

	- getting the list from markdown in the page
	- supporting on the backend some kind of file saving

- make it Async, the way it is, is embarrasing

- make it verify that a string exists in the content

# Quirks

- I have to add the status code 600 when I check the remote URL in the server, so I can tell the difference between my results and the real ones. Using my status code as data is a big mistake

