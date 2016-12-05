var gulp = require('gulp');
var sass = require('gulp-sass');
var concat = require('gulp-concat');
var rename = require('gulp-rename');
var uglify = require('gulp-uglify');

gulp.task('sass', function() {
    return gulp.src('sass/*.scss')
        .pipe(sass({outputStyle: 'compressed'}).on('error', sass.logError))
        .pipe(rename('admin-menu.min.css'))
        .pipe(gulp.dest('admin_menu/static/'));
});

gulp.task('javascript', function() {
    return gulp.src('js/**/*.js')
        .pipe(concat('admin-menu.js'))
        .pipe(rename('admin-menu.min.js'))
        .pipe(uglify())
        .pipe(gulp.dest('admin_menu/static/'));
});

gulp.task('default',function() {
    gulp.watch('sass/*.scss', ['sass']);
    gulp.watch('js/*.js', ['javascript']);
});
