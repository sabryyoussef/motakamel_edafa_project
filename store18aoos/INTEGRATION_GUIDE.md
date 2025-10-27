# Practical Integration Guide: OpenEduCat + Cybrosys Hybrid Solution

## Overview

This guide provides step-by-step instructions for implementing a hybrid educational ERP solution using OpenEduCat as the foundation with selective Cybrosys enhancements.

---

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Installation Strategy](#2-installation-strategy)
3. [Model Compatibility](#3-model-compatibility)
4. [Integration Bridge Module](#4-integration-bridge-module)
5. [Data Migration](#5-data-migration)
6. [Testing & Validation](#6-testing--validation)
7. [Troubleshooting](#7-troubleshooting)

---

## 1. Prerequisites

### 1.1 System Requirements

```bash
# Odoo 18.0
# PostgreSQL 12+
# Python 3.8+
# Minimum 4GB RAM
# 20GB free disk space
```

### 1.2 Database Setup

```bash
# Create database
createdb -U odoo educational_erp_test

# Or via psql
psql -U postgres
CREATE DATABASE educational_erp_test;
GRANT ALL PRIVILEGES ON DATABASE educational_erp_test TO odoo;
\q
```

### 1.3 Module Paths

```ini
# In odoo.conf
[options]
addons_path = /path/to/odoo/addons,
              /path/to/store18aoos/openeducat_erp-18.0.1.0,
              /path/to/store18aoos/cyprocys,
              /path/to/store18aoos/custom_modules
```

---

## 2. Installation Strategy

### 2.1 Phase 1: OpenEduCat Foundation (Week 1)

```bash
# Step 1: Install core
odoo-bin -c /etc/odoo.conf -d educational_erp_test -i openeducat_core --stop-after-init

# Step 2: Verify installation
odoo-bin -c /etc/odoo.conf -d educational_erp_test

# Access: http://localhost:8069
# Login as admin and verify Core menu appears
```

**Verification Checklist:**
- [ ] Students menu visible
- [ ] Faculty menu visible
- [ ] Course menu visible
- [ ] Batch menu visible
- [ ] Department menu visible
- [ ] No errors in logs

### 2.2 Phase 2: Infrastructure Modules (Week 1)

```bash
# Install infrastructure
odoo-bin -c /etc/odoo.conf -d educational_erp_test \
  -i openeducat_facility,openeducat_classroom \
  --stop-after-init
```

**Verification:**
- [ ] Facility menu appears
- [ ] Classroom menu appears
- [ ] Can create facility
- [ ] Can create classroom

### 2.3 Phase 3: Administrative Modules (Week 2)

```bash
# Install administrative modules
odoo-bin -c /etc/odoo.conf -d educational_erp_test \
  -i openeducat_admission,openeducat_fees,openeducat_parent \
  --stop-after-init
```

**Verification:**
- [ ] Admission menu appears
- [ ] Fees menu appears
- [ ] Parent menu appears
- [ ] Demo data loads correctly

### 2.4 Phase 4: Academic Modules (Week 2)

```bash
# Install academic modules
odoo-bin -c /etc/odoo.conf -d educational_erp_test \
  -i openeducat_timetable,openeducat_attendance,openeducat_assignment,openeducat_exam,openeducat_activity \
  --stop-after-init
```

**Verification:**
- [ ] Timetable menu appears
- [ ] Attendance menu appears
- [ ] Assignment menu appears
- [ ] Exam menu appears
- [ ] Activity menu appears

### 2.5 Phase 5: Resource Modules (Week 2)

```bash
# Install library
odoo-bin -c /etc/odoo.conf -d educational_erp_test \
  -i openeducat_library \
  --stop-after-init
```

### 2.6 Phase 6: Cybrosys Theme (Week 3)

**IMPORTANT:** Test in separate database first!

```bash
# Test database
createdb -U odoo educational_erp_theme_test
pg_dump -U odoo educational_erp_test | psql -U odoo educational_erp_theme_test

# Install theme in test database
odoo-bin -c /etc/odoo.conf -d educational_erp_theme_test \
  -i education_theme \
  --stop-after-init

# If successful, install in main database
odoo-bin -c /etc/odoo.conf -d educational_erp_test \
  -i education_theme \
  --stop-after-init
```

**Theme Compatibility Check:**
```python
# Run in Odoo shell
# odoo-bin shell -c /etc/odoo.conf -d educational_erp_theme_test

# Check for conflicts
env['ir.ui.view'].search([('name', 'ilike', 'education')])
env['ir.ui.menu'].search([('name', 'ilike', 'education')])

# If no duplicates, safe to proceed
```

### 2.7 Phase 7: Cybrosys Promotion Module (Week 3)

**CRITICAL:** High risk of conflicts! Test thoroughly.

```bash
# Create test database
createdb -U odoo educational_erp_promotion_test
pg_dump -U odoo educational_erp_test | psql -U odoo educational_erp_promotion_test

# Attempt installation
odoo-bin -c /etc/odoo.conf -d educational_erp_promotion_test \
  -i education_promotion \
  --stop-after-init

# Check logs for errors
tail -f /var/log/odoo/odoo.log
```

**Conflict Resolution:**

If models conflict, create bridge module (see Section 4).

---

## 3. Model Compatibility

### 3.1 Model Name Comparison

| Entity | OpenEduCat | Cybrosys | Compatible? |
|--------|------------|----------|-------------|
| Student | `op.student` | `education.student` | ❌ Different |
| Faculty | `op.faculty` | `education.faculty` | ❌ Different |
| Course | `op.course` | `education.class` | ❌ Different |
| Batch | `op.batch` | `education.class.division` | ❌ Different |
| Subject | `op.subject` | `education.subject` | ❌ Different |
| Exam | `op.exam` | `education.exam` | ❌ Different |

**Conclusion:** Cannot use both core modules together without bridge.

### 3.2 Compatible Modules (Safe to Mix)

| Module | Why Safe |
|--------|----------|
| `education_theme` | Only affects UI, no models |
| `education_promotion` | Can reference OpenEduCat models with modification |
| `educational_announcement` | Independent model, minimal conflicts |

### 3.3 Incompatible Modules (Conflicts)

| Module | Why Incompatible |
|--------|------------------|
| `education_core` | Core model conflicts with `openeducat_core` |
| `education_exam` | Exam model conflicts with `openeducat_exam` |
| `education_fee` | Fee model conflicts with `openeducat_fees` |
| `education_attendances` | Attendance conflicts with `openeducat_attendance` |

**Rule:** Use ONE core system, not both.

---

## 4. Integration Bridge Module

If you must use modules from both systems, create a bridge.

### 4.1 Create Bridge Module

```bash
mkdir -p /path/to/store18aoos/educational_bridge
cd /path/to/store18aoos/educational_bridge
```

### 4.2 Module Structure

```
educational_bridge/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── student_bridge.py
│   ├── faculty_bridge.py
│   └── course_bridge.py
├── security/
│   └── ir.model.access.csv
└── views/
    └── bridge_views.xml
```

### 4.3 Manifest File

```python
# __manifest__.py
{
    'name': 'Educational Bridge',
    'version': '18.0.1.0.0',
    'category': 'Education',
    'summary': 'Bridge between OpenEduCat and Cybrosys modules',
    'depends': [
        'openeducat_core',
        # Add Cybrosys modules if needed
    ],
    'data': [
        'security/ir.model.access.csv',
        'views/bridge_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
```

### 4.4 Student Bridge Model

```python
# models/student_bridge.py
from odoo import models, fields, api

class StudentBridge(models.Model):
    _name = 'education.student.bridge'
    _description = 'Student Bridge Model'
    
    # Primary reference (OpenEduCat)
    openeducat_student_id = fields.Many2one(
        'op.student', 
        string='OpenEduCat Student',
        ondelete='cascade'
    )
    
    # Optional reference (if using Cybrosys promotion)
    cybrosys_reference = fields.Char(
        string='Cybrosys Reference',
        help='Reference ID for Cybrosys modules'
    )
    
    # Common fields
    name = fields.Char(
        related='openeducat_student_id.name',
        string='Student Name',
        readonly=True
    )
    
    registration_number = fields.Char(
        related='openeducat_student_id.gr_no',
        string='Registration Number',
        readonly=True
    )
    
    # Promotion fields (from Cybrosys)
    promotion_status = fields.Selection([
        ('pending', 'Pending'),
        ('promoted', 'Promoted'),
        ('detained', 'Detained'),
        ('failed', 'Failed')
    ], string='Promotion Status', default='pending')
    
    current_academic_year = fields.Many2one(
        'op.academic.year',
        string='Current Academic Year'
    )
    
    next_course = fields.Many2one(
        'op.course',
        string='Promoted To Course'
    )
    
    promotion_date = fields.Date('Promotion Date')
    
    # Methods
    @api.model
    def create_from_openeducat(self, student_id):
        """Create bridge record from OpenEduCat student"""
        return self.create({
            'openeducat_student_id': student_id
        })
    
    def action_promote_student(self):
        """Promote student to next course"""
        self.ensure_one()
        # Custom promotion logic
        self.write({
            'promotion_status': 'promoted',
            'promotion_date': fields.Date.today()
        })
        return True
```

### 4.5 Promotion Adapter

If you want to use Cybrosys promotion module with OpenEduCat:

```python
# models/promotion_adapter.py
from odoo import models, fields, api

class PromotionAdapter(models.Model):
    _name = 'education.promotion.adapter'
    _description = 'Promotion Adapter for OpenEduCat'
    
    name = fields.Char('Promotion Name', required=True)
    academic_year_id = fields.Many2one(
        'op.academic.year',
        string='Academic Year',
        required=True
    )
    from_course_id = fields.Many2one(
        'op.course',
        string='From Course',
        required=True
    )
    to_course_id = fields.Many2one(
        'op.course',
        string='To Course',
        required=True
    )
    promotion_date = fields.Date('Promotion Date', default=fields.Date.today)
    student_ids = fields.Many2many(
        'op.student',
        string='Students to Promote'
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('done', 'Done')
    ], default='draft')
    
    def action_confirm_promotion(self):
        """Confirm and execute promotion"""
        for promotion in self:
            for student in promotion.student_ids:
                # Update student course
                student_course = self.env['op.student.course'].search([
                    ('student_id', '=', student.id),
                    ('course_id', '=', promotion.from_course_id.id),
                    ('state', '=', 'running')
                ], limit=1)
                
                if student_course:
                    # Close old course
                    student_course.state = 'finished'
                    
                    # Create new course enrollment
                    self.env['op.student.course'].create({
                        'student_id': student.id,
                        'course_id': promotion.to_course_id.id,
                        'academic_years_id': promotion.academic_year_id.id,
                        'state': 'running'
                    })
            
            promotion.state = 'done'
        return True
```

### 4.6 Announcement Adapter

For using Cybrosys announcements with OpenEduCat:

```python
# models/announcement_adapter.py
from odoo import models, fields, api

class AnnouncementAdapter(models.Model):
    _name = 'education.announcement.adapter'
    _description = 'Announcement System for OpenEduCat'
    
    name = fields.Char('Announcement Title', required=True)
    description = fields.Html('Description')
    announcement_date = fields.Date(
        'Announcement Date',
        default=fields.Date.today
    )
    expiry_date = fields.Date('Expiry Date')
    
    # Target audience
    target_type = fields.Selection([
        ('all', 'All'),
        ('students', 'Students'),
        ('faculty', 'Faculty'),
        ('parents', 'Parents'),
        ('specific', 'Specific Users')
    ], string='Target Audience', default='all', required=True)
    
    student_ids = fields.Many2many(
        'op.student',
        string='Students'
    )
    faculty_ids = fields.Many2many(
        'op.faculty',
        string='Faculty'
    )
    course_ids = fields.Many2many(
        'op.course',
        string='Courses'
    )
    batch_ids = fields.Many2many(
        'op.batch',
        string='Batches'
    )
    
    # Status
    state = fields.Selection([
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('expired', 'Expired')
    ], default='draft')
    
    priority = fields.Selection([
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent')
    ], default='medium')
    
    attachment_ids = fields.Many2many(
        'ir.attachment',
        string='Attachments'
    )
    
    def action_publish(self):
        """Publish announcement and notify users"""
        self.ensure_one()
        
        # Get recipients
        recipients = self._get_recipients()
        
        # Send notification
        for recipient in recipients:
            self._send_notification(recipient)
        
        self.state = 'published'
        return True
    
    def _get_recipients(self):
        """Get list of users to notify"""
        recipients = self.env['res.users']
        
        if self.target_type == 'all':
            recipients = self.env['res.users'].search([])
        elif self.target_type == 'students':
            recipients = self.student_ids.mapped('user_id')
        elif self.target_type == 'faculty':
            recipients = self.faculty_ids.mapped('user_id')
        elif self.target_type == 'parents':
            # Get parents from students
            parents = self.env['op.parent'].search([])
            recipients = parents.mapped('user_id')
        
        return recipients.filtered(lambda u: u.id != self.env.uid)
    
    def _send_notification(self, user):
        """Send notification to user"""
        self.message_post(
            body=self.description,
            subject=self.name,
            partner_ids=[user.partner_id.id],
            subtype_xmlid='mail.mt_comment'
        )
    
    @api.model
    def _cron_check_expired(self):
        """Check and mark expired announcements"""
        today = fields.Date.today()
        expired = self.search([
            ('state', '=', 'published'),
            ('expiry_date', '<', today)
        ])
        expired.write({'state': 'expired'})
```

---

## 5. Data Migration

### 5.1 Migrate NTHub EMS to OpenEduCat

```python
# migration_script.py
import xmlrpc.client

# Connection settings
url = 'http://localhost:8069'
db = 'educational_erp_test'
username = 'admin'
password = 'admin'

# Authenticate
common = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/common')
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy(f'{url}/xmlrpc/2/object')

# Migrate students
def migrate_students():
    """Migrate students from nthub_ems to openeducat"""
    
    # Get NTHub students
    nthub_students = models.execute_kw(
        db, uid, password,
        'student.student', 'search_read',
        [[]],
        {'fields': ['name', 'date_of_birth', 'gender', 'email']}
    )
    
    # Create OpenEduCat students
    for student in nthub_students:
        # Split name
        name_parts = student['name'].split()
        first_name = name_parts[0] if name_parts else ''
        last_name = name_parts[-1] if len(name_parts) > 1 else ''
        
        # Create partner first
        partner_id = models.execute_kw(
            db, uid, password,
            'res.partner', 'create',
            [{
                'name': student['name'],
                'email': student['email'],
                'is_student': True
            }]
        )
        
        # Create student
        student_id = models.execute_kw(
            db, uid, password,
            'op.student', 'create',
            [{
                'partner_id': partner_id,
                'first_name': first_name,
                'last_name': last_name,
                'birth_date': student['date_of_birth'],
                'gender': 'm' if student['gender'] == 'male' else 'f',
            }]
        )
        
        print(f"Migrated student: {student['name']} (ID: {student_id})")

# Migrate departments
def migrate_departments():
    """Migrate departments"""
    nthub_depts = models.execute_kw(
        db, uid, password,
        'department', 'search_read',
        [[]],
        {'fields': ['name', 'code']}
    )
    
    for dept in nthub_depts:
        dept_id = models.execute_kw(
            db, uid, password,
            'op.department', 'create',
            [{
                'name': dept['name'],
                'code': dept['code']
            }]
        )
        print(f"Migrated department: {dept['name']}")

# Migrate marks
def migrate_marks():
    """Migrate marks/grades"""
    # Custom logic based on your mark structure
    pass

if __name__ == '__main__':
    migrate_departments()
    migrate_students()
    migrate_marks()
```

---

## 6. Testing & Validation

### 6.1 Integration Tests

```python
# tests/test_integration.py
from odoo.tests import TransactionCase

class TestEducationalIntegration(TransactionCase):
    
    def setUp(self):
        super().setUp()
        self.student_model = self.env['op.student']
        self.course_model = self.env['op.course']
        
    def test_student_creation(self):
        """Test student creation in OpenEduCat"""
        partner = self.env['res.partner'].create({
            'name': 'Test Student',
            'email': 'test@example.com'
        })
        
        student = self.student_model.create({
            'partner_id': partner.id,
            'first_name': 'Test',
            'last_name': 'Student',
            'birth_date': '2005-01-01',
            'gender': 'm'
        })
        
        self.assertTrue(student.id)
        self.assertEqual(student.first_name, 'Test')
    
    def test_promotion_adapter(self):
        """Test promotion adapter functionality"""
        if self.env['ir.module.module'].search([
            ('name', '=', 'educational_bridge'),
            ('state', '=', 'installed')
        ]):
            promotion = self.env['education.promotion.adapter'].create({
                'name': 'Test Promotion',
                # Add required fields
            })
            self.assertTrue(promotion.id)
```

### 6.2 UI Testing Checklist

- [ ] All menus accessible
- [ ] Forms load correctly
- [ ] Lists display data
- [ ] Search works
- [ ] Filters work
- [ ] Actions execute
- [ ] Reports generate
- [ ] No console errors
- [ ] Theme applied correctly
- [ ] Mobile responsive

---

## 7. Troubleshooting

### 7.1 Common Issues

#### Issue 1: Module Installation Fails

```bash
# Error: Module not found
# Solution: Check addons_path
grep addons_path /etc/odoo.conf

# Update module list
# Settings > Technical > Modules > Update Apps List
```

#### Issue 2: Model Conflicts

```python
# Error: Model 'education.student' already exists
# Solution: Don't install both core modules

# Check installed modules
SELECT name, state FROM ir_module_module 
WHERE name LIKE '%education%' OR name LIKE '%openeducat%';

# Uninstall conflicting module
odoo-bin -c /etc/odoo.conf -d db_name -u module_name --stop-after-init
```

#### Issue 3: Theme Not Applied

```bash
# Clear browser cache
# Ctrl+Shift+R (hard refresh)

# Regenerate assets
# Settings > Technical > User Interface > Views
# Debug mode > Regenerate Assets Bundles
```

#### Issue 4: Permission Errors

```sql
-- Check security groups
SELECT name FROM res_groups WHERE name LIKE '%education%';

-- Grant access
-- Settings > Users & Companies > Users
-- Edit user > Add to appropriate groups
```

### 7.2 Debugging Tools

```python
# Enable developer mode
# URL: http://localhost:8069/web?debug=1

# Check logs
tail -f /var/log/odoo/odoo.log

# Odoo shell
odoo-bin shell -c /etc/odoo.conf -d db_name

# In shell:
env['op.student'].search_count([])  # Check student count
env['ir.module.module'].search([('state', '=', 'installed')])  # List installed
```

---

## 8. Production Deployment

### 8.1 Pre-Production Checklist

- [ ] All modules tested in development
- [ ] Data migration scripts tested
- [ ] Backups configured
- [ ] Security groups configured
- [ ] User training completed
- [ ] Documentation prepared
- [ ] Rollback plan ready

### 8.2 Deployment Steps

```bash
# 1. Backup production database
pg_dump -U odoo production_db > backup_$(date +%Y%m%d).sql

# 2. Deploy to production
odoo-bin -c /etc/odoo-production.conf -d production_db \
  -i openeducat_core,openeducat_facility,... \
  --stop-after-init

# 3. Verify
odoo-bin -c /etc/odoo-production.conf -d production_db

# 4. Monitor logs
tail -f /var/log/odoo/odoo-production.log
```

---

## 9. Maintenance

### 9.1 Regular Tasks

```bash
# Weekly: Update demo data
# Monthly: Check for module updates
# Quarterly: Performance review
# Annually: Security audit
```

### 9.2 Backup Strategy

```bash
# Daily backup script
#!/bin/bash
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_DIR="/backup/odoo"

# Database backup
pg_dump -U odoo educational_erp > $BACKUP_DIR/db_$DATE.sql

# Filestore backup
tar -czf $BACKUP_DIR/filestore_$DATE.tar.gz /opt/odoo/.local/share/Odoo/filestore/

# Keep only last 30 days
find $BACKUP_DIR -mtime +30 -delete
```

---

## 10. Support & Resources

### Documentation
- OpenEduCat: https://www.openeducat.org/documentation
- Cybrosys: Contact vendor
- Odoo: https://www.odoo.com/documentation/18.0

### Community
- Odoo Community: https://www.odoo.com/forum
- GitHub Issues: Module-specific repositories

---

**Document Version:** 1.0  
**Last Updated:** October 27, 2025  
**Author:** AI Assistant

**Related Documents:**
- `EDUCATIONAL_MODULES_COMPARISON.md` - Detailed comparison
- `QUICK_DECISION_GUIDE.md` - Quick decision guide
- `COMPARISON_SUMMARY.md` - Visual summary

