# -*- coding:utf-8 -*-
import logging
from odoo import fields,models,api
from odoo.exceptions import UserError


logger=logging.getLogger(__name__)


class MaintenanceRequestInmo(models.Model):
    _inherit = 'maintenance.request'

    # Historial mantenimiento
    codigo_falla_ids = fields.One2many(
        comodel_name="maintenance.request.fault.code.item",
        inverse_name="request_id",
        string="Reporte de falla",
        required=False,
        copy=True
    )
    check_codigo_error = fields.Boolean(
        string="Check codigo error",
        store=True,
        related="category_id.check_codigo_error"
    )
    check_lista_chequeo = fields.Boolean(
        string="Check lista chequeo",
        store=True,
        related="category_id.check_lista_chequeo"
    )
    equipment_section_id = fields.Char(
        string="Sección",
        store=True,
        related="equipment_id.id_seccion.name"
    )
    equipment_department_id = fields.Char(
        string="Departamento",
        store=True,
        related="equipment_id.department_id.name"
    )
    equipment_numero_economico=fields.Char(
        string="Número economico",
        store=True,
        related="equipment_id.numero_economico"
    )
    equipment_codigo_interno=fields.Char(
        string="Código interno",
        store=True,
        related="equipment_id.codigo_interno"
    )


    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        args = args or []
        recs = self.browse()
        if not recs:
            recs = self.search(['|', ('codigo_falla', operator, name), ('name', operator, name)] +
                               args, limit=limit)
        return recs.name_get()




