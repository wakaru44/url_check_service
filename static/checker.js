
// My functions to check remote URLs

function checkRemoteUrlOnLocal( url )
{
	// We will have to transform that url into a valid internal query to our backend
	base_url = get_base_url();
	checker_url = base_url + "/check?url=" + encodeURIComponent(url);
	//TODO: This crap is not working
	var status_und_stuff;
	result = $.ajax( checker_url )

	return result
}


function get_base_url()
{
	var http = location.protocol;
	var slashes = http.concat("//");
	var host = slashes.concat(window.location.host); //host not hostname to include port if is not 80
	return host
}


function pass_the_test( spec, responseObject, obj)
{
	if (responseObject.status == spec)
	{ //If the test failed, do magic and paint button red
		obj.style.backgroundColor = "green";
		obj.style.color = "white";

		console.log("We have succeded the test");
		console.log(responseObject);

		result_display = "Ok"
	} else {
		//if passes, paint it green
		obj.style.backgroundColor = "red";
		obj.style.color = "white";

		console.log("We have failed the test?")
		console.log(responseObject)
		console.log(obj)
		result_display = $(obj).attr("href") + " test failed: \n Expected: " + spec + "; Got: " + responseObject.status;
	}

	return result_display;
}
