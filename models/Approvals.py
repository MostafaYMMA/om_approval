from odoo import api, fields, models, _

from odoo.exceptions import  ValidationError

class ApprovalsInherit(models.Model):
    _inherit = "approval.request"

    employee=fields.Many2one("hr.employee" , string="Employee")


