var gulp = require('gulp');
var sass = require('gulp-sass');

gulp.task('styles', function() {
  gulp.src('sass/index.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('./css/'));
});
// Watch Task
gulp.task('default',function() {
  gulp.watch('sass/**/*.scss',['styles']);
});
