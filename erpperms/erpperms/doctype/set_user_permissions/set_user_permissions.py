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
		query = frappe.db.sql("""select user, allow, for_value 
			from 
				`tabUser Permission` 
			where
				user = '{0}'""".format(self.user), as_dict=1)
		print(self.user,"\n\n")

		print(query)

		self.user_permission = {}
		self.set('user_permission', {})
		#print("\n\n")
		# return query

		entries = sorted(list(query))
        # self.set('user_permission', [])

   #      for d in entries:
			# row = self.append('user_permission', {})
			# d.user = user
			# d.allow = allow
			# d.for_value = for_value
			# row.update(d)
