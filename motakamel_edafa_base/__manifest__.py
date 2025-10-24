# -*- coding: utf-8 -*-
{
    'name': 'Motakamel Edafa - Academic Management System',
    'version': '18.0.1.0.0',
    'category': 'Education',
    'summary': 'Comprehensive academic management system for educational institutions',
    'description': """
        Motakamel Edafa Academic Management System
        =========================================
        
        A comprehensive academic management system built on Odoo 18 that includes:
        - Student Management (Admission, Enrollment, Progress Tracking)
        - Learning Management System (LMS)
        - Customer Relationship Management (CRM)
        - Accounting & Finance
        - Human Resources & Payroll
        - Inventory & Content Management
        - Loyalty & Gamification
        - Web Portal & Mobile Support
        - Payment Gateway Integrations
        - Reporting & Analytics
        
        This is the base module that provides the foundation for all other modules.
    """,
    'author': 'Motakamel Edafa',
    'website': 'https://www.motakamel-edafa.com',
    'license': 'LGPL-3',
    'depends': [
        'base',
        'web',
        'portal',
        'website',
    ],
    'data': [
        'security/ir.model.access.csv',
        'security/security_groups.xml',
        'data/ir_sequence_data.xml',
        'static/src/xml/academic_templates.xml',
    ],
    'demo': [
        'demo/demo_data.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'motakamel_edafa_base/static/src/css/base.css',
            'motakamel_edafa_base/static/src/js/base.js',
        ],
        'web.assets_frontend': [
            'motakamel_edafa_base/static/src/css/portal.css',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': True,
    'sequence': 1,
}
