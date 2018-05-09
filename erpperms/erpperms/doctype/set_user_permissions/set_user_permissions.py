# -*- coding: utf-8 -*-
# Copyright (c) 2018, DigitalPrizm Infotech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import flt, getdate, nowdate, fmt_money
from frappe import msgprint, _
from frappe.model.document import Document



class SetUserPermissions(Document):
	def get_user_permissions(self):
		# frappe.msgprint("hi")
		entries = frappe.db.sql("""select user, allow, for_value,
			apply_for_all_roles, name as user_perm_link_name 
			from 
				`tabUser Permission` 
			where
				user = '{0}'""".format(self.user), as_dict=1)

		# self.data1 = "pooja"
		self.set('user_permission', [])

		#print("\n\n")
		# return query

		for d in self.get('user_permission'):
			print("dkkkkk",d)

		for d in entries:
			doc_req = {
				"doctype": "User Perm Table",
				"user": d.user,
				"allow": d.allow,
				"for_value": d.for_value,
				"apply_for_all_roles": d.apply_for_all_roles,
				"user_perm_link_name": d.user_perm_link_name
			}
			self.append("user_permission", doc_req)
			# row = self.append('user_permission', {})
			# row.update(d)
			print(d,"\nl")
		# entries = sorted(list(query))
        # self.set('user_permission', [])

   #      for d in entries:
			# row = self.append('user_permission', {})
			# d.user = user
			# d.allow = allow
			# d.for_value = for_value
			# row.update(d)
