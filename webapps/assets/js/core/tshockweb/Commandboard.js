(function (namespace, $) {
	"use strict";

    var Commandboard = function () {
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

    $('#tshockweb_executecommandform').submit(function(e){
        e.preventDefault();
        var raw_command = $('#tshockweb_input').val();
        $.ajax({
            type: 'POST',
            url: base_url + "api/controllers/servercontroller/execute_cmd",
            data: JSON.stringify({token: tshock.token, command: raw_command}),
            dataType: 'json',
            contentType: "application/json",
            success: function (data) {
                if (data.status == 200) {
                    $("#tshockweb_executedcommands").prepend("<div class='col-xs-12'><p>" +
                        "<a class='text-medium text-lg text-primary' href='#'>Executed command & result:</a><br>" +
                        "<a class='opacity-75'>"+raw_command+"</a></p>" +
                        "<div class='contain-xs pull-left prettyprint'>"+String(data.result.output).replace(/</g, "&lt;").replace(/>/g, "&gt;")+"</div></div>");
                    $('#tshockweb_input').val("");
                } else {
                    console.log("Collecting data for amount of players on server has failed: "+JSON.stringify(data));
                }
            }
        });
    });

	namespace.Commandboard = new Commandboard;
}(this.materialadmin, jQuery)); // pass in (namespace, jQuery):
