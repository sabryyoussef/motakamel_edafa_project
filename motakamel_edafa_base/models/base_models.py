# -*- coding: utf-8 -*-

from odoo import models, fields, api


class BaseAcademicModel(models.AbstractModel):
    """
    Abstract base model for all academic system models.
    Provides common fields and methods.
    """
    _name = 'base.academic.model'
    _description = 'Base Academic Model'

    # Common fields for all academic models
    name = fields.Char(string='Name', required=True, translate=True)
    active = fields.Boolean(string='Active', default=True)
    create_date = fields.Datetime(string='Created On', readonly=True)
    create_uid = fields.Many2one('res.users', string='Created By', readonly=True)
    write_date = fields.Datetime(string='Last Updated On', readonly=True)
    write_uid = fields.Many2one('res.users', string='Last Updated By', readonly=True)
    
    # Academic system specific fields
    academic_year = fields.Char(string='Academic Year', help='Academic year this record belongs to')
    notes = fields.Text(string='Notes', help='Additional notes or comments')
    
    @api.model
    def _get_current_academic_year(self):
        """Get current academic year based on system date"""
        import datetime
        current_year = datetime.datetime.now().year
        return f"{current_year}-{current_year + 1}"


class AcademicConfig(models.Model):
    """
    Configuration model for academic system settings
    """
    _name = 'academic.config'
    _description = 'Academic System Configuration'
    _inherit = 'base.academic.model'

    # System Configuration
    institution_name = fields.Char(string='Institution Name', required=True)
    institution_code = fields.Char(string='Institution Code', required=True)
    current_academic_year = fields.Char(string='Current Academic Year', required=True)
    system_version = fields.Char(string='System Version', default='18.0.1.0.0')
    
    # Academic Settings
    max_students_per_course = fields.Integer(string='Max Students per Course', default=50)
    min_students_per_course = fields.Integer(string='Min Students per Course', default=5)
    course_duration_days = fields.Integer(string='Default Course Duration (Days)', default=30)
    
    # Financial Settings
    currency_id = fields.Many2one('res.currency', string='Default Currency', required=True)
    payment_terms = fields.Text(string='Payment Terms', help='Default payment terms for courses')
    
    # Contact Information
    email = fields.Char(string='Institution Email')
    phone = fields.Char(string='Institution Phone')
    website = fields.Char(string='Institution Website')
    address = fields.Text(string='Institution Address')
    
    @api.model
    def get_config(self):
        """Get system configuration, create default if not exists"""
        config = self.search([], limit=1)
        if not config:
            config = self.create({
                'institution_name': 'Motakamel Edafa Academy',
                'institution_code': 'MEA',
                'current_academic_year': self._get_current_academic_year(),
                'currency_id': self.env.ref('base.USD').id,
            })
        return config
