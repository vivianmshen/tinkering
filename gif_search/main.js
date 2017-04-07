/* Get user search term */

var searchBar = document.querySelector("input");
var searchButton = document.querySelector("#button-id");

searchButton.addEventListener('click', function() {
	var searchText = document.querySelector("input").value;
	returnResults(searchText);
});

searchBar.addEventListener('keyup', function(e) {
	//Check if key pressed was enter
	if(e.which === 13) {
		var searchText = document.querySelector("input").value;
		returnResults(searchText);
	}
});


/* API */

function returnResults(searchText) {
	var staticUrlLHS = "http://api.giphy.com/v1/gifs/search?q=";
	var staticUrlRHS = "&api_key=dc6zaTOxFJmzC";
	var searchUrlTerms = searchText.replace(/\s+/g, '+');
	var url = staticUrlLHS + searchUrlTerms + staticUrlRHS;
	console.log(url);

	var GiphyAJAXCall = new XMLHttpRequest();
	GiphyAJAXCall.open('GET', url);
	GiphyAJAXCall.send();

	GiphyAJAXCall.addEventListener('load', function(e) {
		var data = e.target.response;
		pushToDOM(data);
	});
}


/* Return results for search */

function pushToDOM(data) {
	var displayContainer = document.querySelector(".js-container");
	var response = JSON.parse(data);

	var imgUrls = response.data

	imgUrls.forEach(function(imgObject) {
		imgUrl = imgObject.images.fixed_height.url;
		displayContainer.innerHTML += "<img src=\"" + imgUrl + "\" class=\"container-imgs\">";
	});
}
