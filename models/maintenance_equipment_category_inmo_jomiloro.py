from odoo import fields, models, api

class MaintenanceEquipmentCategoryInmoJomiloro(models.Model):
    _inherit = 'maintenance.equipment.category'

    check_codigo_error=fields.Boolean(
        String="Código error",
        required=True,
        default=False,
        copy=True,
        help="Activa códigos de fallon en peticiones de mantenimiento"

    )
    check_lista_chequeo=fields.Boolean(
        String="Lista de chequeo",
        required=True,
        default=False,
        copy=True,
        help="Activa lista de chequeo en peticiones de mantenimiento"
    )

    chanel_gd_id = fields.Many2one(
        comodel_name='maintenance.channel.gd',
        string='Canal Google Drive',
        required=False
    )
    url_carpeta_google_drive = fields.Char(string="URL Carpeta GD", store=True,
                                           related="chanel_gd_id.url_carpeta_google_drive", readonly=True)