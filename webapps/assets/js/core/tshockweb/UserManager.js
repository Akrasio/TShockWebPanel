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

    function get_url_parameters() {
        var result = {};
        var items = location.search.substr(1).split("&");
        var i;
        for (i = 0; i < items.length; i++) {
            var tmp = items[i].split("=");
            result[tmp[0]] = tmp[1];
        }
        return result;
    }

    var base_url = window.location.protocol + "//" + window.location.host + "/";
    var tshock = JSON.parse(Cookies.get('tshockweb'));
    var url_params = get_url_parameters();

    $(document).on('click', '#tshockweb_ban',function (e) {
        if (window.confirm("Are you sure you want to ban " + url_params.username + "?")) {
            // ban user
            $.ajax({
                type: 'POST',
                url: base_url + "api/controllers/playercontroller/ban_player_by_username",
                data: JSON.stringify({token: tshock.token, username: url_params.username,
                                      reason: "Banned by admin " + tshock.username}),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        toastr.success('Successfully banned user: ' + url_params.username, '');
                        window.location.replace(base_url + "webapps/html/dashboards/dashboard.html");
                    } else {
                        var message = "Banning user on server has failed: " + JSON.stringify(data);
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

    $(document).on('click', '#tshockweb_kick',function (e) {
        if (window.confirm("Are you sure you want to kick " + url_params.username + "?")) {
            // kick user
            $.ajax({
                type: 'POST',
                url: base_url + "api/controllers/playercontroller/kick_player_by_username",
                data: JSON.stringify({token: tshock.token, username: url_params.username,
                                      reason: "Kicked by admin " + tshock.username}),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        toastr.success('Successfully kicked user: ' + url_params.username, '');
                        window.location.replace(base_url + "webapps/html/dashboards/dashboard.html");
                    } else {
                        var message = "Kicking user on server has failed: " + JSON.stringify(data);
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

    $(document).on('click', '#tshockweb_kill',function (e) {
        if (window.confirm("Are you sure you want to kill " + url_params.username + "?")) {
            // kick user
            $.ajax({
                type: 'POST',
                url: base_url + "api/controllers/playercontroller/kill_player_by_username",
                data: JSON.stringify({token: tshock.token, username: url_params.username,
                                      reason: "Killed by admin " + tshock.username}),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        toastr.success('Successfully killed user: ' + url_params.username, '');
                    } else {
                        var message = "Killing user on server has failed: " + JSON.stringify(data);
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

    $(document).on('click', '#tshockweb_mute',function (e) {
        if (window.confirm("Are you sure you want to mute " + url_params.username + "?")) {
            // mute user
            $.ajax({
                type: 'POST',
                url: base_url + "api/controllers/playercontroller/mute_player_by_username",
                data: JSON.stringify({token: tshock.token, username: url_params.username,
                                      reason: "Muted by admin " + tshock.username}),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        toastr.success('Successfully muted user: ' + url_params.username, '');
                    } else {
                        var message = "Muting user on server has failed: " + JSON.stringify(data);
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

    $(document).on('click', '#tshockweb_unmute',function (e) {
        if (window.confirm("Are you sure you want to unmute " + url_params.username + "?")) {
            // unmute user
            $.ajax({
                type: 'POST',
                url: base_url + "api/controllers/playercontroller/unmute_player_by_username",
                data: JSON.stringify({token: tshock.token, username: url_params.username,
                                      reason: "Unmuted by admin " + tshock.username}),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        toastr.success('Successfully unmuted user: ' + url_params.username, '');
                    } else {
                        var message = "Unmuting user on server has failed: " + JSON.stringify(data);
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

	namespace.Authenticate = new Authenticate;
}(this.materialadmin, jQuery)); // pass in (namespace, jQuery):
