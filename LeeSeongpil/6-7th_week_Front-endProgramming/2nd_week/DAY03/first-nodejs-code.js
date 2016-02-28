// File System 모듈 호출
// Node.js 서버사이드 환경에서 모듈 호출시, 
//CommonJS 진영의 모듈로더 사용 require()
var fs = require('fs');

fs.readFile('./index.html', function (err, data) {
	if (err) {
		console.error(err.meassge);
	}
});

console.log(data);