# -*- coding:utf-8 -*-

from odoo import fields, models, api

class MaintenanceRequestFaultCodeItem(models.Model):
    _name = 'maintenance.request.fault.code.item'
    _description = "Códigos falla para equipos de mantenimiento"
    _order = 'name'

    name = fields.Many2one(
        comodel_name="maintenance.equipment.fault.code",
        string="Códigos de falla",
        required=True,
        index=True,
        copy=True
    )
    request_id = fields.Many2one(
        comodel_name="maintenance.request",
        string="Petición de mantenimiento",
        required=False,
        ondelete='cascade'
    )
    peticion_id_request= fields.Char(
        string="Petición",
        store=True,
        related="request_id.name"
    )
    equipment_id_request = fields.Char(
        string="Maquina",
        store=True,
        related="request_id.equipment_id.name"

    )
    seccion_id_request = fields.Char(
        string="Sección",
        store=True,
        related="request_id.equipment_section_id"
    )
    departamento_id_request = fields.Char(
        string="Departamento",
        store=True,
        related="request_id.equipment_department_id"
    )
    numero_economico_id_request = fields.Char(
        string="Número economico",
        store=True,
        related="request_id.equipment_numero_economico"
    )
    responsable_id_request = fields.Char(
        string="Responsable",
        store=True,
        related="request_id.user_id.name"
    )
    codigo_interno_id_request=fields.Char(
        string="Código interno",
        store=True,
        related="request_id.equipment_codigo_interno"
    )

    observaciones=fields.Text(String="Obsevaciones",required=False, copy=False)
    sequence = fields.Integer(string='Secuencia', default=1)
    active = fields.Boolean(String="Activo", default=True)
    folio = fields.Char(string="Folio", index=True, copy=False, readonly=True,default='Nuevo elemento de falla')

    @api.model
    def create(self, values):
        # Add code here
        values['folio'] = self.env['ir.sequence'].next_by_code('secuencia.folio.peticion.mantenimiento')
        return super(MaintenanceRequestFaultCodeItem, self).create(values)


    def name_get(self):
        res = []
        for rec in self:
            res.append((rec.id, '%s .- %s' % (rec.request_id, rec.name)))
            return res
