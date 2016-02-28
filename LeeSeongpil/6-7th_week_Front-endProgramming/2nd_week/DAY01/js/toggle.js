var btn = selector('.toggle-canvas');
btn.onclick = function (e) {
    e.preventDefault();
    toggleGrid('.canvas', 'on');
}

function toggleGrid(el, className) {
    selector(el).classList.toggle(className);
}
    