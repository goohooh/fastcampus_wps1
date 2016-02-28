var gulp = require('gulp'),
	sass = require('gulp-sass');

// 기본 업무
gulp.task('default', function () {
	console.log('Gulp Task is Start...');
});

// 사용자 정의 업무
// 디텍토리에 파일을 다른 디텍토리로 이동
gulp.task('move', function () {
	gulp.src('bower_components/jquery/dist/jquery.min.js')
		.pipe( gulp.dest('js/lib'));
});

gulp.task('sass', function () {
	gulp.src('sass/**/*.(sass,scss)')
		.pipe( sass())
		.pipe(gulp.dest('css/'));
});

gulp.task('watch', function () {
	gulp.watch('sass/**/*.(sass,scss)', ['sass']);
});