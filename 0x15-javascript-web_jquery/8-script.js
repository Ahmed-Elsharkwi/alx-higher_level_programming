$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (data) {
	for (let i = 0; i < data.results.length; i++){
		$('#list_movies').append($("<li></li>").text(data.results[i].title))
	}
});