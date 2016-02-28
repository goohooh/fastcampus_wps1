var canvas = $('.canvas');
var canvasBtn = $('.show_canvas_button');
var shadow = $('shadow');
var canvasClose = $('.close_canvas_button');

canvasBtn.onclick = function (e) {
	e.preventDefault()
	addClass('.canvas', 'canvas_on');
	addClass('.shadow', 'shadow_on');
}

canvasClose.onclick = function (e) {
	e.preventDefault();
	removeClass('.canvas', 'canvas_on');
	removeClass('.shadow', 'shadow_on')
}

function addClass(selector, className) {
	$(selector).className += ' ' + className;
}
function removeClass(selector, className) {
	var check = new RegExp("(\\s|^)" + className + "(\\s|$)");
 	$(selector).className = $(selector).className.replace(check, " ").trim();
}