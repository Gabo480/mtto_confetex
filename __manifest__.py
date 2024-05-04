# -*- coding:utf-8 -*-
{
'name': 'Mantenimiento Confetex',
    'category': 'Manufacturing/Maintenance',
    'version': '1.0',
    'author': 'Gabriel Cortes Martinez',
    'summary': 'Módulo para ordenes de mantenimiento y control de máquinas y herramientas en grupo Confetex',
    'description': '''Modulo para un control de peticiones de mantenimiento y control de máquinas y herramienta con 
                      impresión de código QR en Odoo14''',
    'website': 'https://www.confetex.com',
    'depends': [
        'base',
        'sale_management',
        'account',
        'stock',
        'purchase',
        'hr',
        'maintenance',
        'contacts',
        'base_automation',
        'mail'
    ],
    'data': [
        'security\security.xml',
        'security\ir.model.access.csv',
        'data\secuencia.xml',
        'data\servidor_acciones.xml',
        'data\conf_maintenance_mtto_confetex.xml',
        'report\maintenance_reports.xml',
        'report\maintenance_templates.xml',
        'wizard\maintenance_equipment_loan_wizard_vw.xml',
        'views\maintenance_equiment_invw.xml',
        'views\maintenance_equipment_menu_vw.xml',
        'views\maintenance_equipment_section.xml',
        'views\maintenance_equipment_characteristics_vw.xml',
        'views\maintenance_equipment_document_type_vw.xml',
        'views\maintenance_equipment_document_vw.xml',
        'views\maintenance_channel_gd_vw.xml',
        'views\maintenance_equipment_category_inmo_jomiloro_vw.xml',
        'views\maintenance_equipment_review_vw.xml',
        'views\maintenance_equipment_loan_vw.xml',
        'views\maintenance_equipment_fault_code_vw.xml',
        'views\maintenance_request_vw.xml',
        'views\maintenance_request_fault_code_item.xml'




    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}