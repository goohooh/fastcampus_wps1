var gulp = require('gulp'),
	autoprefixer = require('gulp-autoprefixer'),
	sass= require('gulp-sass'),
	sourcemaps = require('gulp-sourcemaps');

gulp.task('default', ['server', 'sass']);
// gulp.task('default', function() {
// 	gulp.start('sass');
// });

gulp.task('build', function() {
	
});

gulp.task('server', function() {
	
});

gulp.task('watch', function() {
	gulp.watch('src/sass/**/*.{sass,scss}', ['sass']);
});

gulp.task('sass', function() {
	gulp.src('src/sass/**/*.{sass,scss}')
		.pipe(sourcemaps.init())
		.pipe( sass( {'outputStyle': 'expanded'}).on('error', sass.logError))
		.pipe(autoprefixer())
		.pipe(write('./maps'))
		.pipe(gulp.dest('dist/css'));
});