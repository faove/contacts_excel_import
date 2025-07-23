from odoo import models  # type: ignore

class ResPartner(models.Model):
    _inherit = 'res.partner'

    # No additional methods needed - using menu action instead
