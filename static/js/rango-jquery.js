$(document).ready( function() {
    $("#about-btn").click( function(event) {
    	
    });

    $('.btn-edit').click( function(event) {
    	var id = this.id.match(/\d/g).join("");
        alert("You clicked to edit item ".concat(id));
	});

    $('.btn-remove').click( function(event) {
    	var id = this.id.match(/\d/g).join("");
    	window.location.href= "/del/".concat(id)
    });
});