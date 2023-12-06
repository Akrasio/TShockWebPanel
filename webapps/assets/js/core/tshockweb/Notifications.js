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

    console.log("Starting tshock notifications");
    var tshock = JSON.parse(Cookies.get('tshockweb'));
    var base_url = window.location.protocol + "//" + window.location.host + "/";

    // set settings for toastr
    toastr.options.closeButton = false;
    toastr.options.progressBar = false;
    toastr.options.debug = false;
    toastr.options.positionClass = 'toast-bottom-left';
    toastr.options.showDuration = 333;
    toastr.options.hideDuration = 333;
    toastr.options.timeOut = 4000;
    toastr.options.extendedTimeOut = 4000;
    toastr.options.showEasing = 'swing';
    toastr.options.hideEasing = 'swing';
    toastr.options.showMethod = 'slideDown';
    toastr.options.hideMethod = 'slideUp';

	namespace.TShockDashboard = new TShockDashboard;
}(this.materialadmin, jQuery)); // pass in (namespace, jQuery):
