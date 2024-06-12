$(document).ready(function() {
    // Add a new list item when #add_item is clicked
    $('#add_item').click(function() {
        $('.my_list').append('<li>Item</li>');
    });

    // Remove the last list item when #remove_item is clicked
    $('#remove_item').click(function() {
        $('.my_list li:last-child').remove();
    });

    // Clear all list items when #clear_list is clicked
    $('#clear_list').click(function() {
        $('.my_list').empty();
    });
});
