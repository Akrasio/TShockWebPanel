(function (namespace, $) {
	"use strict";

    var Web = function () {
		// Create reference to this instance
		var o = this;
		// Initialize app when document is ready
		$(document).ready(function () {
			o.initialize();
		});

	};

    // execute when trying to login
    $('#tshockweb_login').on('click', function (e) {
        var username = $("#tshockweb_username").val();
        var password = $("#tshockweb_password").val();

        $.ajax({
            type: 'POST',
            url: window.location.protocol + "//" + window.location.host + "/" + "api/login",
            data: JSON.stringify({ username: username, password: password }),
            dataType: 'json',
            contentType: "application/json",
            success: function (data) {
                if (data.status == 200) {
                    console.log("Success: " + data.result.token);
                    Cookies.set('tshockweb', { token: data.result.token, username: username }, { expires: 2 }); // expires in 2 days
                    // add username/password if remember me is checked and login successful
                    // remove the cookie if remember me is unchecked
                    if ($('#tshockweb_rememberme').is(":checked")) {
                        Cookies.set('tshockweb_login', { username: username, password: password });
                    } else {
                        Cookies.remove('tshockweb_login');
                    }
                    // redirect to dashboard
                    window.location.replace(window.location.protocol + "//" + window.location.host + "/" + "webapps/html/dashboards/dashboard.html");
                } else {
                    var message = "Login failed: " + data.result;
                    toastr.error(message, '');
                    console.log(message);
                }
            }
        });
    });

    // execute when loading the login page
    if (Cookies.get('tshockweb_login') != undefined) {
        var login_creds = JSON.parse(Cookies.get('tshockweb_login'));
        $("#tshockweb_username").val(login_creds.username).addClass("dirty");
        $("#tshockweb_password").val(login_creds.password).addClass("dirty");
        $('#tshockweb_rememberme').prop('checked', true);
    }

    // go directly to dashboard if a valid token is present in the cookie
    if (Cookies.get('tshockweb') != undefined) {
        var tshock = JSON.parse(Cookies.get('tshockweb'));
        $.ajax({
            type: 'POST',
            url: window.location.protocol + "//" + window.location.host + "/" + "api/validation",
            data: JSON.stringify({token: tshock.token}),
            dataType: 'json',
            contentType: "application/json",
            success: function (data) {
                if (data.status == 200) {
                    // redirect to dashboard
                    console.log("Existing token is valid, redirecting!");
                    window.location.replace(window.location.protocol + "//" + window.location.host + "/" + "webapps/html/dashboards/dashboard.html");
                } else {
                    console.log("Present token is invalid, deleting it...");
                    Cookies.remove('tshockweb');
                }
            }
        });
    }

	namespace.Web = new Web;
}(this.materialadmin, jQuery)); // pass in (namespace, jQuery):
