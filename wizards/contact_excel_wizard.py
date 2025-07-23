from odoo import models, fields, api  # type: ignore
import base64
import xlrd  # type: ignore
import logging

_logger = logging.getLogger(__name__)

class ContactExcelWizard(models.TransientModel):
    _name = 'contact.excel.wizard'
    _description = 'Wizard para importar contactos desde Excel'

    file = fields.Binary(string="Archivo Excel", required=True)
    file_name = fields.Char(string="Nombre del archivo")

    def action_import_excel(self):
        """Import contacts from Excel file"""
        try:
            # Decode the file
            file_data = base64.b64decode(self.file)
            
            # Open the Excel file
            workbook = xlrd.open_workbook(file_contents=file_data)
            sheet = workbook.sheet_by_index(0)
            
            # Process each row (skip header)
            for row_idx in range(1, sheet.nrows):
                row = sheet.row_values(row_idx)
                
                # Assuming columns: Name, Email, Phone, Company
                if len(row) >= 4:
                    partner_data = {
                        'name': row[0] or '',
                        'email': row[1] or '',
                        'phone': row[2] or '',
                        'company_type': 'company' if row[3] else 'person',
                    }
                    
                    # Create the partner
                    self.env['res.partner'].create(partner_data)
            
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Éxito',
                    'message': f'Se importaron {sheet.nrows - 1} contactos correctamente',
                    'type': 'success',
                }
            }
            
        except Exception as e:
            _logger.error(f"Error importing Excel: {str(e)}")
            return {
                'type': 'ir.actions.client',
                'tag': 'display_notification',
                'params': {
                    'title': 'Error',
                    'message': f'Error al importar: {str(e)}',
                    'type': 'danger',
                }
            }
