# VA Claims Analysis System v2.0 - WorkDrive Integration

Automated VA disability claims analysis using AI and Zoho WorkDrive integration.

## Updated Features
- AI-powered medical record analysis
- Automated report generation with WorkDrive hosting
- Public share links for client access
- Email notifications to clients
- CRM integration
- **NEW:** WorkDrive file management (replaces Sites)

## Setup
1. Deploy to Render
2. Set environment variables (WorkDrive instead of Sites)
3. Configure Zoho Flow webhook
4. Set up WorkDrive folder structure
5. Test with sample data

## API Endpoints
- `GET /` - Health check
- `POST /process-va-records` - Main processing endpoint
- `GET /test` - System status check

## Required Scopes
- WorkDrive.files.ALL
- WorkDrive.folders.ALL  
- ZohoCRM.modules.ALL
- ZohoMail.messages.CREATE
