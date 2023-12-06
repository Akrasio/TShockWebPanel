(function (namespace, $) {
	"use strict";

    var Profile = function () {
		// Create reference to this instance
		var o = this;
		// Initialize app when document is ready
		$(document).ready(function () {
			o.initialize();
		});

	};

    console.log("Starting collecting data for profile");

    var terraria_wiki_url = "http://terraria.gamepedia.com/";

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

    function filter_empty_entries(list) {
        var result = [];
        var i;
        var items = list.split(", ");
        for (i = 0; i < items.length; i++) {
            if (items[i] != "0:0" && items[i] != "0" && items[i] != ":0") {
                result.push(items[i]);
            }
        }
        return result;
    }

    function add_item_by_name(item_name, amount) {
        $.ajax({
            type: 'POST',
            url: base_url + "api/config/terraria/item/by_name",
            data: JSON.stringify({token: tshock.token, name: item_name}),
            dataType: 'json',
            contentType: "application/json",
            success: function (data) {
                var tsw_image_url;
                if (data.status == 200) {
                    tsw_image_url = base_url + "webapps/assets/img/terraria/player/items/Item_"+data.result+".png";
                    $("#tshockweb_inventory_overview").append("<li class='tile'>" +
                      "<a class='tile-content ink-reaction' href='"+terraria_wiki_url+item_name.replace(/ /g, "_")+"'><div class='tile-icon'>" +
                      "<img src='"+tsw_image_url+"' alt='' />" +
                      "</div><div class='tile-text'>"+item_name+"<small>Amount: " + amount +
                      "</small></div></a></li>");
                } else {
                    tsw_image_url = base_url + "webapps/assets/img/terraria/player/items/Item_0.png";
                    $("#tshockweb_inventory_overview").append("<li class='tile'>" +
                      "<a class='tile-content ink-reaction' href='"+terraria_wiki_url+item_name.replace(/ /g, "_")+"'><div class='tile-icon'>" +
                      "<img src='"+tsw_image_url+"' alt='' />" +
                      "</div><div class='tile-text'>"+item_name+"<small>Amount: " + amount +
                      "</small></div></a></li>");
                }
            }
        });
    }

    function add_buff_by_id(buff_id) {
        $.ajax({
            type: 'POST',
            url: base_url + "api/config/terraria/buff/by_id",
            data: JSON.stringify({token: tshock.token, id: buff_id}),
            dataType: 'json',
            contentType: "application/json",
            success: function (data) {
                var tsw_image_url;
                if (data.status == 200) {
                    tsw_image_url = base_url + "webapps/assets/img/terraria/player/buffs/"+data.result.replace(/ /g, "_")+".png";
                    $("#tshockweb_buffs_overview").append("<li class='tile'>" +
                      "<a class='tile-content ink-reaction' href='"+terraria_wiki_url+data.result.replace(/ /g, "_")+"'><div class='tile-icon'>" +
                      "<img src='"+tsw_image_url+"' alt='' />" +
                      "</div><div class='tile-text'>"+data.result+"<small>" +
                      "</small></div></a></li>");
                } else {
                    tsw_image_url = base_url + "webapps/assets/img/terraria/player/items/Item_0.png";
                    $("#tshockweb_buffs_overview").append("<li class='tile'>" +
                      "<a class='tile-content ink-reaction' href='"+terraria_wiki_url+data.result.replace(/ /g, "_")+"'><div class='tile-icon'>" +
                      "<img src='"+tsw_image_url+"' alt='' />" +
                      "</div><div class='tile-text'>"+data.result+"<small>" +
                      "</small></div></a></li>");
                }
            }
        });
    }

    function add_armor_by_id(item_id, bonus) {
        $.ajax({
            type: 'POST',
            url: base_url + "api/config/terraria/item/by_id",
            data: JSON.stringify({token: tshock.token, id: item_id}),
            dataType: 'json',
            contentType: "application/json",
            success: function (data) {
                var tsw_image_url;
                if (data.status == 200) {
                    tsw_image_url = base_url + "webapps/assets/img/terraria/player/items/Item_"+item_id+".png";
                    $("#tshockweb_armor_overview").append("<li class='tile'>" +
                      "<a class='tile-content ink-reaction' href='"+terraria_wiki_url+data.result.replace(/ /g, "_")+"'><div class='tile-icon'>" +
                      "<img src='"+tsw_image_url+"' alt='' />" +
                      "</div><div class='tile-text'>"+data.result+"<small>Bonus: " + bonus +
                      "</small></div></a></li>");
                } else {
                    tsw_image_url = base_url + "webapps/assets/img/terraria/player/items/Item_0.png";
                    $("#tshockweb_armor_overview").append("<li class='tile'>" +
                      "<a class='tile-content ink-reaction' href='"+terraria_wiki_url+data.result.replace(/ /g, "_")+"'><div class='tile-icon'>" +
                      "<img src='"+tsw_image_url+"' alt='' />" +
                      "</div><div class='tile-text'>"+data.result+"<small>Bonus: " + bonus +
                      "</small></div></a></li>");
                }
            }
        });
    }

    var tshock = JSON.parse(Cookies.get('tshockweb'));
    var base_url = window.location.protocol + "//" + window.location.host + "/";
    var url_params = get_url_parameters();
    var team_mapping = {0: "NO",
                        1: "RED",
                        2: "GREEN",
                        3: "BLUE",
                        4: "YELLOW",
                        5: "PURPLE"};

    function load_player_information() {
        $.ajax({
            type: 'POST',
            url: base_url + "api/model/lists/players/get_user_in_world",
            data: JSON.stringify({token: tshock.token, username: url_params.username}),
            dataType: 'json',
            contentType: "application/json",
            success: function (data) {
                if (data.status == 200) {
                    $("#tshockweb_username").html(data.result.output.username + "<br><small style='color:white'>" + data.result.output.group + "</small>");
                    var inventory_entries = filter_empty_entries(data.result.output.inventory);
                    var armor_entries = filter_empty_entries(data.result.output.armor);
                    var buff_entries = filter_empty_entries(data.result.output.buffs);
                    var registered = data.result.output.registered.split("T");

                    // clear & set user settings
                    console.log(data.result.output);
                    $("#tshockweb_profile_ip").html(data.result.output.ip);
                    $("#tshockweb_profile_position").html(data.result.output.position);
                    if (data.result.output.registered != "") {
                        $("#tshockweb_profile_registered").html(registered[0] + " " + registered[1] + " as " + data.result.output.username);
                    }
                    else {
                        $("#tshockweb_profile_registered").html("Not yet registered!");
                    }

                    $("#tshockweb_armor_overview").html("");
                    $("#tshockweb_buffs_overview").html("");
                    $("#tshockweb_inventory_overview").html("");

                    // add inventory
                    for (var i = 0; i < inventory_entries.length; i++) {
                        var item_entry = inventory_entries[i].split(":");
                        add_item_by_name(item_entry[0], item_entry[1]);
                    }
                    // add buffs
                    for (var b = 0; b < buff_entries.length; b++) {
                        var buff_entry = buff_entries[b].split(":");
                        add_buff_by_id(buff_entry[0]);
                    }
                    // add armor
                    for (var a = 0; b < armor_entries.length; a++) {
                        var armor_entry = armor_entries[a].split(":");
                        add_armor_by_id(armor_entry[0], armor_entry[1]);
                    }
                } else {
                    var message = "Collecting data for online user has failed: " + JSON.stringify(data);
                    toastr.error(message, '');
                    console.log(message);
                }
            }
        });
    }

    function load_player_team_information() {
        $.ajax({
            type: 'POST',
            url: base_url + "api/model/lists/players/get_current_players",
            data: JSON.stringify({token: tshock.token}),
            dataType: 'json',
            contentType: "application/json",
            success: function (data) {
                if (data.status == 200) {
                    console.log(data);
                    for (var i = 0; i < data.result.output.length; i++) {
                        if (data.result.output[i].nickname == url_params['username']) {
                            $("#tshockweb_profile_team").html(team_mapping[data.result.output[i].team] + " TEAM");
                            break;
                        }

                    }

                } else {
                    var message = "Collecting team for online user has failed: " + JSON.stringify(data);
                    toastr.error(message, '');
                    console.log(message);
                }
            }
        });
    }

    $('#tshockweb_refresh_general').on('click', function (e) {
        load_player_information();
        load_player_team_information();
        toastr.success('Successfully refreshed profile data!', '');
    });

    $('#tshockweb_whisper_send').on('click', function (e) {
        var whisper_message = $('#tshockweb_whisper').val();
        $.ajax({
            type: 'POST',
            url: base_url + "api/controllers/servercontroller/execute_cmd",
            data: JSON.stringify({token: tshock.token, command: "/whisper " + url_params.username + " " + whisper_message}),
            dataType: 'json',
            contentType: "application/json",
            success: function (data) {
                if (data.status == 200) {
                    $('#tshockweb_whisper').val("");
                    toastr.success("Successfully whispered `" + whisper_message + "` to user!", '');
                } else {
                    var message = "Sending whisper to user has failed: " + JSON.stringify(data);
                    toastr.error(message, '');
                    console.log(message);
                }
            }
        });
    });

    load_player_information();
    load_player_team_information();

	namespace.Profile = new Profile;
}(this.materialadmin, jQuery)); // pass in (namespace, jQuery):
