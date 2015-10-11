

a mockup for a URL checker on js that is ultra easy to implement.

In order to be able to request any url, overcoming the limitation of Access-Control-Allow-Origin in js, we will have to perform the request from the server, and then tell the answer to js from our own AJAX interface.

Ideally, we would like to keep configuration in one side (probably the js side of things) , provide an initial run before configuring and allow to configure afterwards.

# The goal

just a simple URL checker, that with a provided list of URL, it checks them on the press of a button, or in reload.

# The status

a mock to test how to check the url on js.

# Next features

- allow to specify multiple expectations (maybe it should fail and it means good)

- take the list of url from the html. Get the link from the href. Get the expectations of the results from the body of the a

- button to check on demand

- green/red colors
