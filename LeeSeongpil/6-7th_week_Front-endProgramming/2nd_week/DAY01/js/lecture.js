// JavaScript 기본 문법 정리
// 크라이언트 환경에서 문서에 접근/조작/처리 과정
// 문서에 존재하는 대상(요소)을 선택
// 선택된 대상에 조작을 가하거나 이벤트에 따라 프로그래밍 되도록 설계합니다

var html, head, body;

// Legacy DOM === DOM Level 0
// html = document.documentElement;
// head = document.head;
// body = document.body;


// DOM Level 1
// html = document.getElementsByTagName('html');
// head = document.getElementsByTagName('head');
// body = document.getElementsByTagName('body');

// console.log( 'html : ', html);  //.item[n] 메서드 가능
// console.log( 'head : ', head[0]);
// console.log( 'body : ', body);

// 문서에 존재하는 모든 Division 요소를 선택 변수에 참조
// var all_div = document.getElementsByTagName('div');

// console.log(all_div.length); // 배열이 아닌 유사배열, 아래 메서드가 없음

// 배열 데이터 유형이 가진 메소드
// .push(), .shift() ...


// var page = document.getElementById('page');
// var navigation = document.getElementById('navigation');
// var footer = document.getElementById('footer');

// console.log(page);
// console.log(navigation);
// console.log(footer);

// var container = document.getElementsByClassName('container'); // IE8 이하는 지원X

// console.log(container[0]);


// DOM Selection API
// var div = document.querySelector('div'); // 매치하는 첫번째 요소만 반환
// var divs = document.querySelectorAll('div'); // jQuery 보다 빠르게
// console.log(divs)
//GET
var first_child_of_body = document.querySelector('body *:first-child');
// console.log(first_child_of_body);

console.log(first_child_of_body.id);
console.log(first_child_of_body.className); // class가 예약어라 className

// debugger;

// SET
// Legacy
// first_child_of_body.id = 'document_page';
// first_child_of_body.className = 'wrapper';

// console.log(first_child_of_body.id);
// console.log(first_child_of_body.className);

var first_child_of_body_id = first_child_of_body.getAttribute('container');

var app_name = document.body.getAttribute('data-ng-app');
console.log(app_name);

document.body.setAttribute('data-ng-app',  'MemoryGameApp');

//body = document.querySelector('body')
var body = selector('body');
var divs = selector('div');
var links = selector('a');

addAttribute(body, 'data-module', 'dom-helper');

addAttribute(body, 'class', 'hi');
addAttribute(body, 'class', 'there');

//데이터 유형 체크
// 1. typeof, instanceof 둘다 엉망
// 2. constructor 정확
// 3. Object.prototype.toString 메소드 빌려쓰기 => 완전무결한 방식