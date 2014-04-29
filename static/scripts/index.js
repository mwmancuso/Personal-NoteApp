/*jslint browser:true*/
/*globals jQuery,$*/
$(document).ready(function () {
    'use strict';
    $('#register_selector').click(function (event) {
        $('#register_selector').css('color', '#10A057');
        $('#login_selector').css('color', '#51382c');
        $('#login').css('display', 'none');
        $('#register').css('display', 'block');
    });
    $('#login_selector').click(function (event) {
        $('#register_selector').css('color', '#51382c');
        $('#login_selector').css('color', '#10A057');
        $('#register').css('display', 'none');
        $('#login').css('display', 'block');
    });
});

$('#register_form').parsley();