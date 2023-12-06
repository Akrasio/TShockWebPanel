(function (namespace, $) {
	"use strict";

    var TShockDashboard = function () {
		// Create reference to this instance
		var o = this;
		// Initialize app when document is ready
		$(document).ready(function () {
			o.initialize();
		});

	};

    console.log("Starting collecting data for dashboard");
    var tshock = JSON.parse(Cookies.get('tshockweb'));
    var base_url = window.location.protocol + "//" + window.location.host + "/";
    var team_mapping = {0: "../../assets/img/terraria/team/white_noteam.png",
                        1: "../../assets/img/terraria/team/red.png",
                        2: "../../assets/img/terraria/team/green.png",
                        3: "../../assets/img/terraria/team/blue.png",
                        4: "../../assets/img/terraria/team/yellow.png",
                        5: "../../assets/img/terraria/team/purple.png"};

    // display general information about the server
    function load_general_information() {
        $.ajax({
            type: 'POST',
            url: base_url + "api/model/lists/server/get_server_information",
            data: JSON.stringify({token: tshock.token}),
            dataType: 'json',
            contentType: "application/json",
            success: function (data) {
                if (data.status == 200) {
                    $('#tshockweb_amountonserver').html(data.result.output.playercount + "/" + data.result.output.maxplayers);
                    $('#tshockweb_uptime').html(data.result.output.uptime);
                    $('#tshockweb_server').html(data.result.output.serverversion);
                    $('#tshockweb_world').html(data.result.output.world);
                } else {
                    var message = "Collecting data for server has failed: " + JSON.stringify(data);
                    toastr.error(message, '');
                    console.log(message);
                }
            }
        });
    }

    // display world information about the server
    function load_world_information() {
        $.ajax({
            type: 'POST',
            url: base_url + "api/model/lists/world/get_world_details",
            data: JSON.stringify({token: tshock.token}),
            dataType: 'json',
            contentType: "application/json",
            success: function (data) {
                if (data.status == 200) {
                    if (data.result.output.bloodmoon == true) {$('#tshockweb_bloodmoon').html("On");} else {$('#tshockweb_bloodmoon').html("Off");}
                    if (data.result.output.daytime == true) {$('#tshockweb_daytime').html("Day");} else {$('#tshockweb_daytime').html("Night");}
                } else {
                    var message = "Collecting data for world on server has failed: " + JSON.stringify(data);
                    toastr.error(message, '');
                    console.log(message);
                }
            }
        });
    }

    // display registered users in the database
    function load_registered_users() {
        $.ajax({
            type: 'POST',
            url: base_url + "api/model/lists/players/get_users_in_database",
            data: JSON.stringify({token: tshock.token}),
            dataType: 'json',
            contentType: "application/json",
            success: function (data) {
                if (data.status == 200) {
                    // empty registered users
                    $("#tshockweb_registeredusers").html("");
                    // fill registered users
                    var i;
                    for (i = 0; i < data.result.output.length; i++) {
                        $("#tshockweb_registeredusers").append("<li class='tile'><a class='tile-content ink-reaction'>" +
                            "<div class='tile-icon'>" +
                            "<img src='../../assets/img/terraria/user_logo.png' alt='' /></div>" +
                            "<div class='tile-text'>" + data.result.output[i].name + "<small>" +
                            "" + data.result.output[i].group + "</small></div>" +
                            "<a class='btn btn-flat ink-reaction tshockweb_remove' id='remove_"+data.result.output[i].name+"'><i class='fa fa-trash-o'></i></a></a></li>");
                    }
                } else {
                    var message = "Collecting data for registered users on server has failed: " + JSON.stringify(data);
                    toastr.error(message, '');
                    console.log(message);
                }
            }
        });
    }

    // display banned users in the database
    function load_banned_users() {
        $.ajax({
            type: 'POST',
            url: base_url + "api/model/lists/players/get_banned_players",
            data: JSON.stringify({token: tshock.token}),
            dataType: 'json',
            contentType: "application/json",
            success: function (data) {
                if (data.status == 200) {
                    // empty registered users
                    $("#tshockweb_bannedusers").html("");
                    // fill registered users
                    var i;
                    for (i = 0; i < data.result.output.length; i++) {
                        var ip = "no ip address supplied";
                        var username = data.result.output[i].name;
                        if (data.result.output[i].ip != ""){ip = data.result.output[i].ip}
                        $("#tshockweb_bannedusers").append("<li class='tile'><a class='tile-content ink-reaction'>" +
                            "<div class='tile-icon'>" +
                            "<img src='../../assets/img/terraria/user_logo.png' alt='' /></div>" +
                            "<div class='tile-text'>" + data.result.output[i].name + "<small>" +
                            "" + data.result.output[i].reason + ", " + ip + "</small></div>" +
                            "<a class='btn btn-flat ink-reaction tshockweb_unban' id='unban_"+username+"'>" +
                            "<i class='md md-favorite'></i></a></a></li>");
                    }
                } else {
                    var message = "Collecting data for registered users on server has failed: " + JSON.stringify(data);
                    toastr.error(message, '');
                    console.log(message);
                }
            }
        });
    }

    // display online users
    // display registered users in the database
    function load_online_users() {
        $.ajax({
            type: 'POST',
            url: base_url + "api/model/lists/players/get_current_players",
            data: JSON.stringify({token: tshock.token}),
            dataType: 'json',
            contentType: "application/json",
            success: function (data) {
                if (data.status == 200) {
                    // empty registered users
                    $("#tshockweb_onlineusers").html("");
                    // fill registered users
                    var i;
                    for (i = 0; i < data.result.output.length; i++) {
                        var username = data.result.output[i].nickname;
                        var group = data.result.output[i].group;
                        var team = data.result.output[i].team;
                        var registered = false;

                        // check if user is logged in or registered
                        if (data.result.output[i].username != "") {
                            registered = true;
                        }

                        $.ajax({
                            type: 'POST',
                            url: base_url + "api/model/lists/players/get_user_ip_in_world",
                            data: JSON.stringify({token: tshock.token, username: username}),
                            dataType: 'json',
                            contentType: "application/json",
                            success: function (sub_data) {
                                if (data.status == 200) {
                                    $("#tshockweb_onlineusers").append("<li class='tile'><a class='tile-content ink-reaction'" +
                                        "href='" + base_url + "webapps/html/pages/profile.html?username=" + username +"'>" +
                                        "<div class='tile-icon'>" +
                                        "<img src='"+team_mapping[team]+"' alt='' /></div>" +
                                        "<div class='tile-text'>" + username + "<small>" +
                                        "" + group + ", " + sub_data.result.output + "</small></div>" +
                                        "<a class='btn btn-flat ink-reaction tshockweb_kill' id='kill_"+username+"'><i class='md md-flash-on'></i></a>" +
                                        "<a class='btn btn-flat ink-reaction tshockweb_kick' id='kick_"+username+"'><i class='md md-report-problem'></i></a>" +
                                        "<a class='btn btn-flat ink-reaction tshockweb_ban' id='ban_"+username+"'><i class='md md-block'></i></a></a></li>");
                                        console.log(data)
                                } else {
                                    var message = "Collecting ip for online user on server has failed: " + JSON.stringify(data)
                                    toastr.error(message, '');
                                    console.log(message);
                                }
                            }
                        });
                    }
                } else {
                    var message = "Collecting data for online user on server has failed: " + JSON.stringify(data);
                    toastr.error(message, '');
                    console.log(message);
                }
            }
        });
    }

    $('#tshockweb_refresh_registeredusers').on('click', function (e) {
        load_registered_users();
        toastr.success('Successfully refreshed registered users!', '');
    });

    $('#tshockweb_refresh_onlineusers').on('click', function (e) {
        load_online_users();
        toastr.success('Successfully refreshed online users!', '');
    });

    $('#tshockweb_refresh_general').on('click', function (e) {
        load_general_information();
        load_world_information();
        toastr.success('Successfully refreshed general information!', '');
    });

    $('#tshockweb_refresh_bannedusers').on('click', function (e) {
        load_banned_users();
        toastr.success('Successfully refreshed banned users!', '');
    });

    $(document).on('click', '.tshockweb_unban',function (e) {
        var username = $(this).attr('id').split("_")[1];
        var raw_command = "/ban del " + username;
        if (window.confirm("Are you sure you want to unban " + username + "?")) {
            //unban user
            $.ajax({
                type: 'POST',
                url: base_url + "api/controllers/servercontroller/execute_cmd",
                data: JSON.stringify({token: tshock.token, command: raw_command}),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        load_banned_users();
                        toastr.success('Successfully unbanned user: ' + data.result.output, '');
                    } else {
                        var message = "Unbanning user on server has failed: " + JSON.stringify(data);
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

    $(document).on('click', '.tshockweb_ban',function (e) {
        var username = $(this).attr('id').split("_")[1];
        if (window.confirm("Are you sure you want to ban " + username + "?")) {
            // ban user
            $.ajax({
                type: 'POST',
                url: base_url + "api/controllers/playercontroller/ban_player_by_username",
                data: JSON.stringify({token: tshock.token, username: username,
                                      reason: "Banned by admin " + tshock.username}),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        load_online_users();
                        load_banned_users();
                        toastr.success('Successfully banned user: ' + username, '');
                    } else {
                        var message = "Banning user on server has failed: " + JSON.stringify(data);
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

    $(document).on('click', '.tshockweb_kick',function (e) {
        var username = $(this).attr('id').split("_")[1];
        if (window.confirm("Are you sure you want to kick " + username + "?")) {
            // kick user
            $.ajax({
                type: 'POST',
                url: base_url + "api/controllers/playercontroller/kick_player_by_username",
                data: JSON.stringify({token: tshock.token, username: username,
                                      reason: "Kicked by admin " + tshock.username}),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        load_online_users();
                        toastr.success('Successfully kicked user: ' + username, '');
                    } else {
                        var message = "Kicking user on server has failed: " + JSON.stringify(data);
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

    $(document).on('click', '.tshockweb_kill',function (e) {
        var username = $(this).attr('id').split("_")[1];
        if (window.confirm("Are you sure you want to kill " + username + "?")) {
            // kick user
            $.ajax({
                type: 'POST',
                url: base_url + "api/controllers/playercontroller/kill_player_by_username",
                data: JSON.stringify({token: tshock.token, username: username,
                                      reason: "Killed by admin " + tshock.username}),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        toastr.success('Successfully killed user: ' + username, '');
                    } else {
                        var message = "Killing user on server has failed: " + JSON.stringify(data);
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

    $(document).on('click', '.tshockweb_remove',function (e) {
        var username = $(this).attr('id').split("_")[1];
        if (window.confirm("Are you sure you want to delete the registered account of user " + username + "?")) {
            // remove registered user
            $.ajax({
                type: 'POST',
                url: base_url + "api/controllers/playercontroller/delete_player",
                data: JSON.stringify({token: tshock.token, username: username}),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        load_registered_users();
                        toastr.success('Successfully removed registered account of user: ' + username, '');
                    } else {
                        var message = "Removing registered account on server has failed: " + JSON.stringify(data);
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

    // execute when trying to enable/disable a bloodmoon
    $('#tshockweb_bloodmoon_toggle').on('click', function (e) {
        if (window.confirm("Are you sure you want to toggle the bloodmoon?")) {
            $.ajax({
                type: 'POST',
                url: window.location.protocol + "//" + window.location.host + "/" + "api/controllers/servercontroller/execute_cmd",
                data: JSON.stringify({token: tshock.token, command: "/bloodmoon"}),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        load_world_information();
                        toastr.success('Toggled bloodmoon!');
                    } else {
                        var message = "Toggling the bloodmoon failed: " + data.result;
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

    // execute when trying to drop a meteor
    $('#tshockweb_meteor_drop').on('click', function (e) {
        if (window.confirm("Are you sure you want to drop a meteor?")) {
            $.ajax({
                type: 'POST',
                url: window.location.protocol + "//" + window.location.host + "/" + "api/controllers/worldcontroller/drop_meteor",
                data: JSON.stringify({token: tshock.token}),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        toastr.success('Dropped the meteor!');
                    } else {
                        var message = "Dropping the meteor failed: " + data.result;
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

    // execute when trying to butcher npcs
    $('#tshockweb_butcher_npcs').on('click', function (e) {
        if (window.confirm("Are you sure you want to butcher ALL NPCs?")) {
            $.ajax({
                type: 'POST',
                url: window.location.protocol + "//" + window.location.host + "/" + "api/controllers/worldcontroller/butcher_npcs",
                data: JSON.stringify({token: tshock.token}),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        toastr.success(data.result.output + "!");
                    } else {
                        var message = "Dropping the meteor failed: " + data.result;
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

    // execute when trying to set the daytime (day/night)
    $('.tshockweb_daytime').on('click', function (e) {
        var daytime_status = $(this).attr('id').split("_")[2];
        if (window.confirm("Are you sure you want to set the daytime to "+daytime_status+"?")) {
            $.ajax({
                type: 'POST',
                url: window.location.protocol + "//" + window.location.host + "/" + "api/controllers/servercontroller/execute_cmd",
                data: JSON.stringify({token: tshock.token, command: "/time " + daytime_status}),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        load_world_information();
                        toastr.success("Successfully changed the daytime to: " + daytime_status);
                    } else {
                        var message = "Failed to changed the daytime: " + data.result;
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

    // execute when trying to save the world
    $('#tshockweb_world_save').on('click', function (e) {
        if (window.confirm("Are you sure you want to save the world? This can result in some lag...")) {
            $.ajax({
                type: 'POST',
                url: window.location.protocol + "//" + window.location.host + "/" + "api/controllers/worldcontroller/save_world",
                data: JSON.stringify({token: tshock.token}),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        toastr.success("World saved!");
                    } else {
                        var message = "Saving world failed: " + data.result;
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

    // execute when trying to reload config
    $('#tshockweb_server_reload').on('click', function (e) {
        if (window.confirm("Are you sure you want to reload the server config?")) {
            $.ajax({
                type: 'POST',
                url: window.location.protocol + "//" + window.location.host + "/" + "api/controllers/servercontroller/reload_server_configs",
                data: JSON.stringify({token: tshock.token}),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        toastr.success("Server config reloaded!");
                    } else {
                        var message = "Reloading server config failed: " + data.result;
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

    // execute when trying to set world autosave
    $('.tshockweb_world_autosave').on('click', function (e) {
        var autosave_status = ($(this).attr('id').split("_")[3] === 'true');
        if (window.confirm("Are you sure you want to set the world autosave status to "+autosave_status+"?")) {
            $.ajax({
                type: 'POST',
                url: window.location.protocol + "//" + window.location.host + "/" + "api/controllers/worldcontroller/set_autosave_world",
                data: JSON.stringify({token: tshock.token, status: autosave_status}),
                dataType: 'json',
                contentType: "application/json",
                success: function (data) {
                    if (data.status == 200) {
                        toastr.success("World autosave status set to: " + autosave_status);
                    } else {
                        var message = "Setting world autosave status failed: " + data.result;
                        toastr.error(message, '');
                        console.log(message);
                    }
                }
            });
        }
    });

    // load dashboard data
    load_general_information();
    load_world_information();
    load_online_users();
    load_registered_users();
    load_banned_users();

	namespace.TShockDashboard = new TShockDashboard;
}(this.materialadmin, jQuery)); // pass in (namespace, jQuery):
