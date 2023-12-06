(function (namespace, $) {
	"use strict";

    var Authenticate = function () {
		// Create reference to this instance
		var o = this;
		// Initialize app when document is ready
		$(document).ready(function () {
			o.initialize();
		});

	};
    var base_url = window.location.protocol + "//" + window.location.host + "/";

    // triggers reboot of server
    $('#tshockweb_reboot').on('click', function (e) {
        if (window.confirm("Are you sure you want to reboot?")) {
            var tshock = JSON.parse(Cookies.get('tshockweb'));
            $.ajax({
                type: 'POST',
                url: base_url + "api/controllers/servercontroller/restart_server",
                data: JSON.stringify({
                    token: tshock.token,
                    message: "Rebooting terraria server by admin " + tshock.username
                }),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        toastr.success('Successfully triggered reboot!');
                        console.log("Success: " + data.result);
                        Cookies.remove('tshockweb');
                        window.location.replace(base_url + "webapps/html/pages/login.html");
                    } else {
                        var message = "Rebooting terraria server failed: " + data.result;
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

    // triggers stop of server
    $('#tshockweb_reboot').on('click', function (e) {
        if (window.confirm("Are you sure you want to shutdown?")) {
            var tshock = JSON.parse(Cookies.get('tshockweb'));
            $.ajax({
                type: 'POST',
                url: base_url + "api/controllers/servercontroller/stop_server",
                data: JSON.stringify({
                    token: tshock.token,
                    message: "Shutting down terraria server by admin " + tshock.username
                }),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        toastr.success('Successfully triggered shutdown!');
                        console.log("Success: " + data.result);
                        Cookies.remove('tshockweb');
                        window.location.replace(base_url + "webapps/html/pages/login.html");
                    } else {
                        var message = "Shutting down terraria server failed: " + data.result;
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

	namespace.Authenticate = new Authenticate;
}(this.materialadmin, jQuery)); // pass in (namespace, jQuery):
