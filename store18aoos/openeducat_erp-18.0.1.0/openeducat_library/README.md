# OpenEduCat Library Module

## Overview
The OpenEduCat Library module provides comprehensive library management functionality for educational institutions. It handles library resources, media management, book circulation, library cards, and library operations. The module integrates with the activity and parent modules to provide complete library management from cataloging to circulation.

## Version
- **Version**: 18.0.1.0
- **License**: LGPL-3
- **Category**: Education
- **Sequence**: 3
- **Complexity**: Easy

## Dependencies
- `account` - Accounting system integration
- `base_automation` - Automated workflow management
- `openeducat_activity` - Activity management integration
- `openeducat_parent` - Parent module integration

## Key Features

### 1. Media Management
- **Media Cataloging**: Create and manage library media (books, journals, DVDs, etc.)
- **Media Types**: Define different types of media and their specifications
- **Media Units**: Manage individual copies of media items
- **Media Purchase**: Track media purchases and acquisitions

### 2. Library Operations
- **Media Issue**: Issue media items to students and faculty
- **Media Return**: Process media returns and renewals
- **Media Reservation**: Handle media reservations and holds
- **Media Queue**: Manage waiting lists for popular items

### 3. Library Cards
- **Library Card Management**: Create and manage library cards for users
- **Card Types**: Define different types of library cards
- **Card Validation**: Validate library cards and user privileges
- **Card Printing**: Generate library cards with barcodes

### 4. Circulation Management
- **Media Movement**: Track all media movements and transactions
- **Due Date Management**: Manage due dates and overdue items
- **Fine Management**: Calculate and manage library fines
- **Renewal Processing**: Handle media renewals and extensions

### 5. Library Administration
- **Library Setup**: Configure library settings and policies
- **User Management**: Manage library users and privileges
- **Inventory Management**: Track library inventory and stock
- **Library Reports**: Generate comprehensive library reports

## Data Models

### Core Models
- `op.media` - Main media records
- `op.media.unit` - Individual media units
- `op.media.movement` - Media circulation records
- `op.media.purchase` - Media purchase records
- `op.media.queue` - Media reservation queue
- `op.library` - Library management
- `op.author` - Author information
- `op.publisher` - Publisher information
- `op.tag` - Media tags and categories
- `op.media.type` - Media type definitions

### Media Model Structure
```python
class OpMedia(models.Model):
    _name = "op.media"
    _description = "Media"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    
    name = fields.Char('Title', required=True)
    isbn = fields.Char('ISBN')
    author_ids = fields.Many2many('op.author', string='Authors')
    publisher_id = fields.Many2one('op.publisher', 'Publisher')
    media_type_id = fields.Many2one('op.media.type', 'Media Type')
    tag_ids = fields.Many2many('op.tag', string='Tags')
    media_unit_ids = fields.One2many('op.media.unit', 'media_id', 'Media Units')
    active = fields.Boolean(default=True)
```

## Workflow

### Media Acquisition Workflow
1. **Media Purchase**
   - Create media purchase records
   - Define media specifications
   - Process purchase orders
   - Update inventory

2. **Media Cataloging**
   - Add media to library catalog
   - Assign media types and categories
   - Create media units
   - Generate barcodes

3. **Media Processing**
   - Process new media items
   - Update library inventory
   - Make media available for circulation
   - Notify users of new arrivals

### Circulation Workflow
1. **Media Issue**
   - Validate library card
   - Check media availability
   - Issue media to user
   - Set due date

2. **Media Return**
   - Process media returns
   - Check for damages
   - Calculate fines if applicable
   - Update circulation records

3. **Media Reservation**
   - Handle media reservations
   - Manage waiting lists
   - Notify users of availability
   - Process reservations

## Security & Access Control
- Role-based access control for library operations
- User-specific library privileges
- Media access restrictions
- Circulation policy enforcement

## Integration Points
- **Activity Module**: Library activity tracking
- **Parent Module**: Parent access to student library records
- **Account Module**: Library financial management
- **Base Automation**: Automated library workflows

## Configuration
- Library security configuration
- Circulation policies
- Fine calculation rules
- Media type definitions

## Views & Interface
- Media management forms
- Circulation interface
- Library card management
- Media search and catalog
- Library reports dashboard

## Reports Available
- Media Barcode Report
- Library Card Barcode Report
- Student Library Card Report
- Circulation Report
- Inventory Report

## Technical Specifications
- Built on Odoo 18.0 framework
- Uses PostgreSQL database
- Responsive web interface
- Barcode generation system
- Automated workflow engine

## Installation Requirements
- Odoo 18.0 or higher
- OpenEduCat Activity module
- OpenEduCat Parent module
- Account module
- Base Automation module
- PostgreSQL database
- Python 3.8+

## Usage Guidelines
1. **Initial Setup**: Configure library settings and policies
2. **Media Management**: Add media to library catalog
3. **User Management**: Create library cards for users
4. **Circulation**: Process media issues and returns
5. **Reporting**: Generate library reports and analytics
6. **Maintenance**: Regular library maintenance and updates

## Best Practices
- Consistent media cataloging standards
- Regular inventory management
- Clear circulation policies
- Proper fine management
- Regular library maintenance

## Troubleshooting
- **Media Issue Issues**: Check user privileges and media availability
- **Circulation Problems**: Verify library card validity and policies
- **Report Generation**: Check data completeness and report settings
- **Barcode Issues**: Verify barcode generation and printing

## Demo Data
The module includes demo data for:
- Media types
- Sample media
- Media units
- Library cards
- Circulation records
- Authors and publishers

## Migration Tools
- Data import/export capabilities
- Library history preservation
- Backup and restore functionality
- Bulk media processing

## Future Enhancements
- Digital library integration
- Mobile library access
- Automated inventory management
- AI-powered library analytics
- Integration with external systems

## Support & Documentation
- Official OpenEduCat documentation
- Community forums and support
- Technical documentation for developers
- User guides and tutorials

## API & Integration
- RESTful API for external integrations
- Webhook support for real-time updates
- Data export capabilities
- Third-party system integration

## Compliance & Regulations
- Library management standards
- Data privacy compliance
- Circulation policy compliance
- Educational institution library regulations
