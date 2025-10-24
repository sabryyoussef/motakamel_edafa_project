/** @odoo-module **/

import { registry } from "@web/core/registry";
import { Component } from "@odoo/owl";

// Academic System Base JavaScript
export class AcademicBaseComponent extends Component {
    static template = "motakamel_edafa_base.AcademicBaseTemplate";
    
    setup() {
        super.setup();
        this.setupAcademicSystem();
    }
    
    setupAcademicSystem() {
        // Initialize academic system specific functionality
        this.initializeAcademicYear();
        this.setupAcademicNotifications();
    }
    
    initializeAcademicYear() {
        // Get current academic year and set it in the system
        const currentDate = new Date();
        const currentYear = currentDate.getFullYear();
        const academicYear = `${currentYear}-${currentYear + 1}`;
        
        // Store academic year in session storage
        sessionStorage.setItem('academic_year', academicYear);
    }
    
    setupAcademicNotifications() {
        // Setup academic system notifications
        this.env.services.notification.add("Academic system initialized", {
            type: 'info',
            sticky: false,
        });
    }
    
    // Academic system utility methods
    formatAcademicYear(year) {
        return year ? year.replace('-', ' - ') : '';
    }
    
    getCurrentAcademicYear() {
        return sessionStorage.getItem('academic_year') || '';
    }
    
    formatCurrency(amount, currency = 'USD') {
        return new Intl.NumberFormat('en-US', {
            style: 'currency',
            currency: currency
        }).format(amount);
    }
    
    formatDate(date) {
        return new Intl.DateTimeFormat('en-US', {
            year: 'numeric',
            month: 'long',
            day: 'numeric'
        }).format(new Date(date));
    }
}

// Register the component
registry.category("components").add("AcademicBaseComponent", AcademicBaseComponent);
