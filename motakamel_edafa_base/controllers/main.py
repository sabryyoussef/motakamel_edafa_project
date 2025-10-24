# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request


class AcademicPortal(http.Controller):
    """
    Main controller for academic system portal
    """

    @http.route('/academic/portal', type='http', auth='user', website=True)
    def academic_portal(self, **kwargs):
        """Main academic portal page"""
        return request.render('motakamel_edafa_base.portal_academic_dashboard', {
            'page_name': 'academic_portal',
        })

    @http.route('/academic/student/dashboard', type='http', auth='user', website=True)
    def student_dashboard(self, **kwargs):
        """Student dashboard page"""
        return request.render('motakamel_edafa_base.portal_student_dashboard', {
            'page_name': 'student_dashboard',
        })

    @http.route('/academic/instructor/dashboard', type='http', auth='user', website=True)
    def instructor_dashboard(self, **kwargs):
        """Instructor dashboard page"""
        return request.render('motakamel_edafa_base.portal_instructor_dashboard', {
            'page_name': 'instructor_dashboard',
        })
