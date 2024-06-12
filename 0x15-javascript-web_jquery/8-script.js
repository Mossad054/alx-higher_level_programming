$(document).ready(function() {
    $.ajax({
        url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
        method: 'GET',
        success: function(data) {
            // Iterate over each movie in the results
            $.each(data.results, function(index, movie) {
                // Append each movie title as a list item to the UL#list_movies
                $('#list_movies').append('<li>' + movie.title + '</li>');
            });
        },
        error: function(error) {
            console.log('Error fetching movies:', error);
        }
    });
});
