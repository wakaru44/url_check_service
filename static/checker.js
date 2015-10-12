
// My functions to check remote URLs

function httpGet(theUrl)
{
	var xmlHttp = null;
	xmlHttp = new XMLHttpRequest();
	xmlHttp.open("GET", theUrl, false);
	//TODO: clarify if we need the below snippet or not
//	xmlHttp.onreadystatechange = function(){
//		if (xmlHttp.readyState === 4){
//			if (xmlHttp.status === 404 || xmlHttp.status === 500) {
//				return xmlHttp.status;
//				//alert("Oh no, it does not exist!");
//				//Should be "display the button in red" or smthng
//			}
//			if (xmlHttp.status === 200) {
//				return 200;
//				//alert("Yes, it exists");
//			}
//		}
//	};
	xmlHttp.send( null );
	return xmlHttp.status.toString()
	//return { //alt return with extra data
	//	text: xmlHttp.responseText,
	//	status_code: xmlHttp.status_code
	//};
}

function checkRemoteUrlOnLocal( url )
{
	// We will have to transform that url into a valid internal query to our backend
	base_url = get_base_url();
	checker_url = base_url + "/check?url=" + encodeURIComponent(url);
	result = httpGet( checker_url );
	return result
}

function verify_url( spec, url )
{ // check that the url passes the test
	check = checkRemoteUrlOnLocal(url); //check contais the .text and .status_code
	code = check
	if (check == spec)
	{
		return "Ok" //TODO: make a proper check of the result
	}
	else
	{
		return "The result doesn't match Spec" + "check: " + check + "spec: " + spec
	}
}

function get_base_url()
{
	var http = location.protocol;
	var slashes = http.concat("//");
	//var host = slashes.concat(window.location.hostname);
	var host = slashes.concat(window.location.host); //host not hostname to include port if is not 80
	return host
}


