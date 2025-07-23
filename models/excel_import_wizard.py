from odoo import models, fields
from odoo.exceptions import UserError


class ExcelImportWizard(models.TransientModel):
    _name = 'excel.import.wizard'
    _description = 'Wizard para importar contactos desde Excel'

    excel_file = fields.Binary(string='Archivo Excel', required=True)
    filename = fields.Char(string='Nombre del archivo')
    
    def action_import_excel(self):
        """Import contacts from Excel file"""
        if not self.excel_file:
            raise UserError('Por favor seleccione un archivo Excel.')
        
        # For now, just show a success message
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'Éxito',
                'message': 'Archivo recibido correctamente',
                'type': 'success',
            }
        } 