// Copyright (c) 2018, DigitalPrizm Infotech and contributors
// For license information, please see license.txt

frappe.ui.form.on('Set User Permissions', {
	refresh: function(frm) {
		frm.disable_save();
	},

	get_user_permissions: function(frm) {
		return frappe.call({
			method: "get_user_permissions",
			doc: frm.doc,
			callback: function(r, rt) {
				frm.refresh_field("user_permission");
				frm.refresh_fields();
				// frappe.msgprint("hii");
			}
		});
	}	
});
