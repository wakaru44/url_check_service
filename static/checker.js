
// My functions to check remote URLs

function httpGet(theUrl)
{
	var xmlHttp = null;
	xmlHttp = new XMLHttpRequest();
	xmlHttp.open("GET", theUrl, false);
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
	//result =httpGet( checker_url ); //old, sync crap
	//TODO: This crap is not working
	var status_und_stuff;
	result = $.ajax( checker_url )
	//result.success( function(response_data, statusText, xhrObj)
			//{
				//console.log("then whatever");
				//console.log(response_data);
				//console.log(statusText);
				//console.log(xhrObj);
				//status_und_stuff = xhrObj.status;
				//return status_und_stuff;
			//})
		//.fail( function(a) { console.log("shit happens", a); } );
	//result.fail(function(data){console.log("failed"); console.log(data.status.toString()); status_und_stuff = data.status})
	//result.done(function(data){console.log("success"); console.log(200); status_und_stuff = 200})

	//console.log("this result should be a 200 or a 500 ")
	//console.log("status_und_stuff")
	//console.log(status_und_stuff)
	//console.log("reslut")
	//console.log(result)
	return result
}

function verify_url( spec, url )
{ // check that the url passes the test
	return checkRemoteUrlOnLocal(url); //check contais the .text and .status_code
//	code = check
//	if (check == spec)
//	{
//		return "Ok" //KISS
//	}
//	else
//	{
//		return "The result doesn't match Spec;\n " + "check: " + check + "spec: " + spec
//	}
}

function get_base_url()
{
	var http = location.protocol;
	var slashes = http.concat("//");
	//var host = slashes.concat(window.location.hostname);
	var host = slashes.concat(window.location.host); //host not hostname to include port if is not 80
	return host
}


