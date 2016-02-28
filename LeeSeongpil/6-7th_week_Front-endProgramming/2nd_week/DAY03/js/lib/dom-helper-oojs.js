/*! dom-helper.js © yamoo9.net, 2016 */
var DOM = (function(){

	// 생성자 함수
	// 팩토리 패턴	
	var Dom = function (selctor, context) {
		// new 강제화
		if (this === window) {
			return new Dom(selctor, context);
		}

		this.el = this.collection(selctor)
	};

	//인스턴스 속성 설정(라이브러리 객체 속성/메서드)
	Dom.fn = Dom.prototype = {
		'collection': function (selctor) {
			return document.querySelectorAll(selctor)
		},
		'css': function (prop, value) {
			if (value) {
				this.el
			}
		}
	};

	// 생성자 함수 반환
	return Dom;

})();