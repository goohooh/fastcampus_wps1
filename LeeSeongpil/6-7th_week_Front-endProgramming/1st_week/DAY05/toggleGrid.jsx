#target photoshop

// 선택한 레이어를 토글
// Photoshop DOM 기업 문서객체
// 첫번쨰 레이어의 visible상태를 분기로 토글

var first_layer = app.activeDocument.layers[0];
first_layer.visible = !first_layer.visible;