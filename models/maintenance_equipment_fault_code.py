# -*- coding:utf-8 -*-

from odoo import fields, models, api

class MaintenanceEquipmentFaultCode(models.Model):
    _name = 'maintenance.equipment.fault.code'
    _description = "Elementos de códigos de falla en solicitud de mantenimiento"
    _order = 'codigo_falla'

    name = fields.Char(string="Nombre", required=True)
    codigo_falla = fields.Integer(string="Código", required=True, copy=True, index=True)
    descripcion_falla = fields.Text(string='Descripción de la falla')
    active = fields.Boolean(String="Activo", default=True)
    compañia=fields.Many2one(
        comodel_name="res.company",
        string="Compañia",
        required=False,
        index=True,
        copy=True
    )

    _sql_constraints = [
        ('nombre_codigo_falla_unique',
         'UNIQUE(codigo_falla)',
         "El codigo de falla debe de ser único, busque o vuelva " +
         "a intentarlo si no lo encuentra por favor verifique que el código de falla se encuentre activo."),
    ]


def copy(self, default=None):
    default = dict(default or {})
    default['name'] = self.name + ' (Copia)'
    return super(MaintenanceEquipmentFaultCode, self).copy(default)


def name_get(self):
    res = []
    for rec in self:
        res.append((rec.id, '%s .- %s' % (rec.codigo_falla, rec.name)))
        return res

