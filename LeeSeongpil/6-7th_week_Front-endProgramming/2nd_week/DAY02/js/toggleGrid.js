var toggleBtn = $('.toggle-grid');


function toggleGrid(selector, className) {
	$(selector).classList.toggle(className);
	// if ( $(selector).classList.contains(className) ) {
	// 	$(selector).classList.remove(className);
	// } else {
	// 	$(selector).classList.add(className);
	// }
}

// DOM API를 사용해서 문서 객체를 동적으로 생성하는 방법
// 생성 및 설정(요소, 속성 설정)
// <a class="button toggle-grid fa fa-bars" href role="button" aria-label="Toggle Grid"></a>

var body = document.body,
	toggle_grid_btn = document.createElement('a');

// 속성 설정
toggle_grid_btn.setAttribute('class', 'button toggle-grid fa fa-bars');
toggle_grid_btn.setAttribute('href', '#');
toggle_grid_btn.setAttribute('role', 'button');
toggle_grid_btn.setAttribute('aria-label', 'Toggle Grid');

// 헬퍼함수를 사용할 경우,
// [SET] attr(el, prop, value)
// [GET] attr(el, prop)
function attr(el, prop, value) {
	
}



// 실제 문서에 생성한 요소노드 추가(append)
body.appendChild(toggle_grid_btn);

// console.log(toggle_grid_btn);

// 이벤트 핸들러
// toggleBtn.onclick = function() {
// 	toggleGrid('.container', 'grid');
// 	return false;
// };
var list = $('.list'),
	list_links = $('a', list); //html 컬렉션, NodeList 유사배열


//1. 문서 객체에 새로운 속성을 설정하여 값을 기억
// for (var i = 0,l=list_links.length, item; i  < list_links.length; i++) {
// 	item = list_links[i];
// 	item.index = i;
// 	item.onclick = function (event) {
// 		'use strict';
// 		event.preventDefault();
// 		console.log(this, this.index);
// 	}
// }

//2. 클로저
for (var i =0,l = list_links.length, item; i<l; i++) {
	list_links[i].onclick = (function(index){
		'use strict';
		return function() {
			console.log( this, index);
			return false;
		};
	})(i);
}

// function outerFn() {
// 	'use strict';
// 	var i = 0;
// 	function innerFn() {
// 		return ++i;
// 	}
// 	return innerFn;
// }
// 위의 것은  콘솔에 직접 counter = outerFn(); 입력
// 그리고 콘솔에 cunter() 반복 입력

//아래는 counter() 입력
// var counter = (function outerFn() {
// 	'use strict';
// 	var i = 0;
// 	function innerFn() {
// 		return ++i;
// 	}
// 	return innerFn;
// })();

// var counter2 = (function() {
// 	'use strict';

// 	var count = 0;

// 	function increse() {
// 		return ++i;
// 	}
// 	function decrease() {
// 		return --i;
// 	}

// 	return {
// 		"plus" : increse,
// 		"minus": decrease
// 	};

// })();