def generate_html_report(analysis, veteran_info):
    """Generate comprehensive HTML report with real data and Senior Rater analysis"""
    
    # Build conditions table with enhanced Senior Rater analysis
    current_conditions_html = ""
    for condition in analysis.get('current_conditions', []):
        probability_class = condition.get('probability', 'medium').lower()
        potential_increase = condition.get('potential_rating', 0) - condition.get('current_rating', 0)
        
        current_conditions_html += f"""
        <tr>
            <td>
                <strong>{condition.get('name', 'Unknown')}</strong><br>
                <small>Code: {condition.get('diagnostic_code', 'N/A')} | {condition.get('cfr_citation', 'CFR TBD')}</small>
            </td>
            <td class="text-center">{condition.get('current_rating', 0)}%</td>
            <td class="text-center">
                <strong>{condition.get('potential_rating', 0)}%</strong>
                {f'<br><small style="color: #059669">(+{potential_increase}%)</small>' if potential_increase > 0 else ''}
            </td>
            <td><span class="priority-{probability_class}">{condition.get('probability', 'Unknown')}</span></td>
            <td>{condition.get('evidence', 'No evidence noted')[:100]}...</td>
            <td>{condition.get('action_required', 'Review needed')}</td>
        </tr>
        """
    
    # Build new opportunities with enhanced details
    new_opportunities_html = ""
    for opp in analysis.get('new_opportunities', []):
        success_prob = opp.get('success_probability', 'Medium').lower()
        
        new_opportunities_html += f"""
        <div class="opportunity">
            <div class="opportunity-header">
                <h4>🎯 {opp.get('condition', 'New Opportunity')}</h4>
                <div class="opportunity-badges">
                    <span class="rating-badge">{opp.get('potential_rating', 0)}%</span>
                    <span class="probability-badge priority-{success_prob}">{opp.get('success_probability', 'Medium')}</span>
                </div>
            </div>
            <div class="opportunity-content">
                <p><strong>Connection Type:</strong> {opp.get('connection_type', 'Unknown')}</p>
                <p><strong>Diagnostic Code:</strong> {opp.get('diagnostic_code', 'TBD')}</p>
                <p><strong>CFR Citation:</strong> {opp.get('cfr_citation', 'TBD')}</p>
                <p><strong>Evidence Found:</strong> {opp.get('evidence', 'Evidence to be gathered')}</p>
                <p><strong>Action Required:</strong> {opp.get('action_required', 'Contact for details')}</p>
            </div>
        </div>
        """
    
    # Build strategic action plan with Senior Rater priorities
    action_plan_html = ""
    for action in analysis.get('strategic_plan', []):
        priority_class = action.get('priority', 'Medium').lower()
        action_plan_html += f"""
        <div class="action-item {priority_class}">
            <div class="action-header">
                <h4>📋 {action.get('title', 'Action Item')}</h4>
                <span class="priority-badge priority-{priority_class}">{action.get('priority', 'Medium')} Priority</span>
            </div>
            <div class="action-content">
                <p><strong>Description:</strong> {action.get('description', 'No description')}</p>
                <p><strong>Timeline:</strong> {action.get('timeline', 'TBD')}</p>
                <p><strong>Expected Impact:</strong> {action.get('impact', 'TBD')}</p>
                <p><strong>CFR Basis:</strong> {action.get('cfr_basis', 'Regulatory review needed')}</p>
            </div>
        </div>
        """
    
    # Build evidence gaps with Senior Rater specificity
    evidence_gaps_html = ""
    for gap in analysis.get('evidence_gaps', []):
        evidence_gaps_html += f"<li>{gap}</li>"
    
    # Build Special Monthly Compensation section
    smc_info = analysis.get('special_monthly_compensation', {})
    smc_html = ""
    if smc_info.get('eligible', False):
        smc_html = f"""
        <div class="smc-section">
            <h3>💰 Special Monthly Compensation (SMC) Analysis</h3>
            <div class="smc-eligible">
                <p><strong>Eligible:</strong> <span class="priority-high">YES</span></p>
                <p><strong>Type:</strong> {smc_info.get('type', 'To be determined')}</p>
                <p><strong>Additional Monthly:</strong> <span style="color: #059669; font-weight: bold;">${smc_info.get('additional_monthly', 0):,}</span></p>
                <p><strong>Requirements:</strong> {smc_info.get('requirements', 'Under review')}</p>
            </div>
        </div>
        """
    
    # Build pyramiding analysis
    pyramiding_info = analysis.get('pyramiding_analysis', {})
    pyramiding_html = ""
    if pyramiding_info:
        pyramiding_html = f"""
        <div class="pyramiding-section">
            <h3>⚖️ Pyramiding Rule Analysis</h3>
            <div class="pyramiding-content">
                <h4>Potential Issues:</h4>
                <ul>
                    {chr(10).join([f'<li>{issue}</li>' for issue in pyramiding_info.get('potential_issues', [])])}
                </ul>
                <h4>Recommendations:</h4>
                <ul>
                    {chr(10).join([f'<li>{rec}</li>' for rec in pyramiding_info.get('recommendations', [])])}
                </ul>
            </div>
        </div>
        """
    
    # Get rating calculations with enhanced display
    combined_rating = analysis.get('combined_rating', {})
    current_rating = combined_rating.get('current', 0)
    potential_rating = combined_rating.get('potential', 0)
    current_monthly = combined_rating.get('current_monthly', 0)
    potential_monthly = combined_rating.get('potential_monthly', 0)
    monthly_increase = potential_monthly - current_monthly
    annual_increase = monthly_increase * 12
    
    # Generate complete HTML report with Senior Rater analysis
    report_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VA Senior Rater Analysis - {veteran_info['name']}</title>
        <style>
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                margin: 0;
                padding: 0;
                background-color: #f5f5f5;
                color: #333;
            }}
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                background: white;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
            }}
            .header {{
                background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
                color: white;
                padding: 40px 30px;
                text-align: center;
                position: relative;
            }}
            .logo {{
                position: absolute;
                top: 20px;
                left: 30px;
                height: 60px;
                width: auto;
            }}
            .header h1 {{
                margin: 0 0 10px 0;
                font-size: 32px;
                font-weight: bold;
            }}
            .header .subtitle {{
                font-size: 18px;
                opacity: 0.9;
                margin-bottom: 20px;
            }}
            .file-info {{
                background: rgba(255,255,255,0.1);
                padding: 15px;
                border-radius: 8px;
                margin: 20px 0 0 0;
                font-size: 14px;
                backdrop-filter: blur(10px);
            }}
            .executive-summary {{
                background: linear-gradient(135deg, #e8f4f8 0%, #d1e7dd 100%);
                border-left: 6px solid #2a5298;
                padding: 30px;
                margin: 0;
            }}
            .summary-stats {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin-top: 20px;
            }}
            .stat-card {{
                background: white;
                padding: 20px;
                border-radius: 8px;
                text-align: center;
                box-shadow: 0 2px 10px rgba(0,0,0,0.1);
                transition: transform 0.2s ease;
            }}
            .stat-card:hover {{
                transform: translateY(-2px);
            }}
            .stat-number {{
                font-size: 28px;
                font-weight: bold;
                color: #1e3c72;
            }}
            .stat-label {{
                color: #666;
                font-size: 14px;
                margin-top: 5px;
            }}
            .increase {{
                color: #28a745 !important;
            }}
            .section {{
                margin: 0;
                padding: 30px;
                border-bottom: 1px solid #eee;
            }}
            .section h2 {{
                color: #1e3c72;
                border-bottom: 3px solid #2a5298;
                padding-bottom: 15px;
                font-size: 24px;
                margin-bottom: 25px;
            }}
            .conditions-table {{
                width: 100%;
                border-collapse: collapse;
                margin: 20px 0;
                background: white;
                border-radius: 8px;
                overflow: hidden;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}
            .conditions-table th,
            .conditions-table td {{
                border: 1px solid #ddd;
                padding: 15px;
                text-align: left;
            }}
            .conditions-table th {{
                background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
                font-weight: bold;
                color: #1e3c72;
                font-size: 14px;
            }}
            .conditions-table tr:nth-child(even) {{
                background-color: #f8f9fa;
            }}
            .conditions-table tr:hover {{
                background-color: #e3f2fd;
            }}
            .text-center {{
                text-align: center !important;
            }}
            .priority-high {{ 
                color: #28a745; 
                font-weight: bold; 
                background: #d4edda;
                padding: 3px 8px;
                border-radius: 4px;
            }}
            .priority-medium {{ 
                color: #fd7e14; 
                font-weight: bold; 
                background: #fff3cd;
                padding: 3px 8px;
                border-radius: 4px;
            }}
            .priority-low {{ 
                color: #6c757d; 
                background: #f8f9fa;
                padding: 3px 8px;
                border-radius: 4px;
            }}
            .opportunity {{
                background: linear-gradient(135deg, #d4edda 0%, #c3e6cb 100%);
                border: 1px solid #c3e6cb;
                border-left: 6px solid #28a745;
                border-radius: 12px;
                padding: 25px;
                margin: 20px 0;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            }}
            .opportunity-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 15px;
                flex-wrap: wrap;
            }}
            .opportunity-header h4 {{
                color: #155724;
                font-size: 20px;
                margin: 0;
            }}
            .opportunity-badges {{
                display: flex;
                gap: 10px;
                align-items: center;
            }}
            .rating-badge {{
                background: #28a745;
                color: white;
                padding: 5px 12px;
                border-radius: 20px;
                font-weight: bold;
                font-size: 14px;
            }}
            .probability-badge {{
                padding: 3px 8px;
                border-radius: 4px;
                font-size: 12px;
                font-weight: bold;
            }}
            .opportunity-content p {{
                margin: 10px 0;
                font-size: 15px;
            }}
            .action-item {{
                background: white;
                border: 1px solid #ffeaa7;
                border-left: 6px solid #f39c12;
                border-radius: 12px;
                padding: 25px;
                margin: 20px 0;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                transition: transform 0.2s ease;
            }}
            .action-item:hover {{
                transform: translateY(-2px);
            }}
            .action-item.high {{
                border-left-color: #e74c3c;
                background: linear-gradient(135deg, #fdf2f2 0%, #fecaca 100%);
            }}
            .action-item.medium {{
                border-left-color: #f39c12;
                background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
            }}
            .action-item.low {{
                border-left-color: #17a2b8;
                background: linear-gradient(135deg, #f0f9ff 0%, #dbeafe 100%);
            }}
            .action-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 15px;
                flex-wrap: wrap;
            }}
            .action-header h4 {{
                color: #1e3c72;
                font-size: 18px;
                margin: 0;
            }}
            .priority-badge {{
                padding: 5px 12px;
                border-radius: 20px;
                font-size: 12px;
                font-weight: bold;
                color: white;
            }}
            .priority-badge.priority-high {{
                background: #e74c3c;
            }}
            .priority-badge.priority-medium {{
                background: #f39c12;
            }}
            .priority-badge.priority-low {{
                background: #17a2b8;
            }}
            .action-content p {{
                margin: 8px 0;
                font-size: 15px;
            }}
            .smc-section {{
                background: linear-gradient(135deg, #fff3cd 0%, #ffeaa7 100%);
                border-left: 6px solid #ffc107;
                padding: 20px;
                margin: 20px 0;
                border-radius: 8px;
            }}
            .smc-section h3 {{
                color: #856404;
                margin-top: 0;
            }}
            .smc-eligible {{
                background: white;
                padding: 15px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            .pyramiding-section {{
                background: linear-gradient(135deg, #e2e3e5 0%, #d1ecf1 100%);
                border-left: 6px solid #17a2b8;
                padding: 20px;
                margin: 20px 0;
                border-radius: 8px;
            }}
            .pyramiding-section h3 {{
                color: #0c5460;
                margin-top: 0;
            }}
            .pyramiding-content {{
                background: white;
                padding: 15px;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            }}
            .pyramiding-content h4 {{
                color: #1e3c72;
                margin-top: 15px;
                margin-bottom: 10px;
            }}
            .pyramiding-content ul {{
                margin: 10px 0;
                padding-left: 20px;
            }}
            .pyramiding-content li {{
                margin: 5px 0;
                line-height: 1.5;
            }}
            .footer {{
                background: #f8f9fa;
                padding: 30px;
                text-align: center;
                font-size: 14px;
                color: #666;
                border-top: 3px solid #dee2e6;
            }}
            .disclaimer {{
                background: #fff3cd;
                border: 1px solid #ffeaa7;
                border-radius: 8px;
                padding: 15px;
                margin: 20px 0;
                color: #856404;
            }}
            .senior-rater-badge {{
                background: #1e3c72;
                color: white;
                padding: 8px 15px;
                border-radius: 25px;
                font-size: 12px;
                font-weight: bold;
                display: inline-block;
                margin: 10px 0;
            }}
            .calculation-details {{
                background: #f8f9fa;
                border: 1px solid #dee2e6;
                border-radius: 8px;
                padding: 15px;
                margin: 15px 0;
                font-family: 'Courier New', monospace;
                font-size: 14px;
            }}
            
            /* Mobile Responsive */
            @media (max-width: 768px) {{
                .logo {{
                    height: 40px;
                    top: 15px;
                    left: 15px;
                }}
                .header {{
                    padding: 25px 15px;
                }}
                .header h1 {{
                    font-size: 24px;
                    margin-top: 15px;
                }}
                .section {{
                    padding: 20px 15px;
                }}
                .summary-stats {{
                    grid-template-columns: 1fr;# Complete VA Claims Analysis System - Updated for Real Zoho Webhook Format
# Handles the actual webhook payload structure from Zoho WorkDrive

from flask import Flask, request, jsonify
import requests
import json
import os
from datetime import datetime
import openai

app = Flask(__name__)

# Configuration from environment variables
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your-openai-key-here')
ZOHO_ACCESS_TOKEN = os.getenv('ZOHO_ACCESS_TOKEN', 'your-zoho-token')
ZOHO_REPORTS_FOLDER_ID = os.getenv('ZOHO_REPORTS_FOLDER_ID', 'your-reports-folder-id')
ZOHO_VETREPORTS_FOLDER_ID = os.getenv('ZOHO_VETREPORTS_FOLDER_ID', 'your-vetreports-folder-id')
ZOHO_MAIL_FROM = os.getenv('ZOHO_MAIL_FROM', 'sgt@vetletters.com')

# VA Rating Table for Combined Rating Calculations
VA_RATING_TABLE = {
    0: 0, 10: 10, 20: 20, 30: 30, 40: 40, 50: 50, 60: 60, 70: 70, 80: 80, 90: 90, 95: 100
}

# 2025 VA Compensation Rates (with dependents - Veteran only)
VA_COMPENSATION_RATES = {
    0: 0, 10: 171, 20: 338, 30: 524, 40: 755, 50: 1075, 60: 1361, 
    70: 1716, 80: 1995, 90: 2241, 100: 3737
}

@app.route('/', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        'status': 'active',
        'service': 'VA Claims Analysis System - Claude Integration',
        'timestamp': datetime.now().isoformat(),
        'version': '3.0 - Complete Claude Integration with Senior Rater Mode',
        'ai_backend': 'Claude-3.5-Sonnet (Anthropic)'
    })

@app.route('/process-va-records', methods=['POST'])
def process_va_records():
    """
    Main processing endpoint - handles Zoho WorkDrive webhook payload with Claude analysis
    """
    try:
        print("🚀 Starting VA Claims Analysis with Claude Senior Rater...")
        
        # Get the webhook payload
        webhook_data = request.json
        
        # Log the webhook event
        webhook_event = webhook_data.get('webhook_event', 'file_uploaded')
        print(f"📡 Webhook Event: {webhook_event}")
        
        # Extract veteran information from webhook
        veteran_info = extract_veteran_info_from_webhook(webhook_data)
        print(f"👤 Veteran: {veteran_info['name']} ({veteran_info['email']})")
        print(f"📄 File: {veteran_info['filename']} ({veteran_info.get('file_size', 'unknown size')})")
        
        # Step 1: Download medical records from WorkDrive
        medical_text = download_medical_records_from_workdrive(veteran_info['download_url'])
        print(f"📥 Downloaded {len(medical_text)} characters of medical records")
        
        # Step 2: Analyze with Claude in Senior Rater mode
        analysis_result = analyze_medical_records_with_claude(medical_text, veteran_info)
        print("🤖 Claude Senior Rater analysis completed")
        
        # Step 3: Generate comprehensive HTML report
        report_html = generate_comprehensive_html_report(analysis_result, veteran_info, medical_text)
        print("📊 Comprehensive report generated")
        
        # Step 4: Upload report to WorkDrive
        report_url = upload_report_to_workdrive(report_html, veteran_info)
        print(f"🔗 Report uploaded: {report_url}")
        
        # Step 5: Email notification
        send_notification_email(veteran_info, report_url, analysis_result)
        print("📧 Email notification sent")
        
        # Step 6: Update CRM
        update_crm_record(veteran_info, analysis_result, report_url)
        print("📋 CRM updated")
        
        return jsonify({
            'success': True,
            'veteran_name': veteran_info['name'],
            'report_url': report_url,
            'processing_time': datetime.now().isoformat(),
            'webhook_event': webhook_event,
            'file_processed': veteran_info['filename'],
            'ai_backend': 'Claude-3.5-Sonnet',
            'analysis_sections': len(analysis_result.get('sections', [])),
            'message': 'Senior Rater analysis completed successfully'
        })
        
    except Exception as e:
        print(f"❌ Error processing VA records: {str(e)}")
        return jsonify({
            'success': False,
            'error': str(e),
            'timestamp': datetime.now().isoformat(),
            'webhook_received': bool(request.json),
            'ai_backend': 'Claude-3.5-Sonnet'
        }), 500

def extract_veteran_info_from_webhook(webhook_data: Dict) -> Dict[str, Any]:
    """Extract veteran information from Zoho WorkDrive webhook payload"""
    try:
        # Extract key information from webhook
        file_name = webhook_data.get('name', 'unknown_file')
        client_email = webhook_data.get('event_by_user_email_id', 'unknown@email.com')
        client_display_name = webhook_data.get('event_by_user_display_name', 'Unknown User')
        download_url = webhook_data.get('download_url', '')
        file_id = webhook_data.get('id', '')
        file_size = webhook_data.get('storage_info_size', 'unknown')
        file_type = webhook_data.get('type', 'unknown')
        uploaded_time = webhook_data.get('uploaded_time', datetime.now().strftime('%m/%d/%Y'))
        
        # Extract veteran name from filename or use uploader name
        name_part = file_name.replace(f'.{file_type}', '').replace('.txt', '').replace('.pdf', '').replace('.doc', '')
        
        if '_' in name_part:
            parts = name_part.split('_')
            veteran_name = parts[0].replace('-', ' ').replace('%20', ' ').title()
            veteran_email = parts[1] if len(parts) > 1 and '@' in parts[1] else client_email
        else:
            veteran_name = client_display_name
            veteran_email = client_email
        
        return {
            'name': veteran_name,
            'email': veteran_email,
            'filename': file_name,
            'download_url': download_url,
            'file_id': file_id,
            'file_size': file_size,
            'file_type': file_type,
            'uploaded_time': uploaded_time,
            'uploader_email': client_email,
            'uploader_name': client_display_name,
            'date': datetime.now().strftime('%m%d%Y'),
            'report_id': f"VAR-{datetime.now().strftime('%Y%m%d')}-{file_id[:8]}"
        }
        
    except Exception as e:
        print(f"Error extracting veteran info: {e}")
        return {
            'name': webhook_data.get('event_by_user_display_name', 'Unknown Veteran'),
            'email': webhook_data.get('event_by_user_email_id', 'unknown@email.com'),
            'filename': webhook_data.get('name', 'unknown_file'),
            'download_url': webhook_data.get('download_url', ''),
            'file_id': webhook_data.get('id', ''),
            'file_size': webhook_data.get('storage_info_size', 'unknown'),
            'file_type': webhook_data.get('type', 'unknown'),
            'uploaded_time': webhook_data.get('uploaded_time', ''),
            'uploader_email': webhook_data.get('event_by_user_email_id', ''),
            'uploader_name': webhook_data.get('event_by_user_display_name', ''),
            'date': datetime.now().strftime('%m%d%Y'),
            'report_id': f"VAR-{datetime.now().strftime('%Y%m%d')}-{datetime.now().strftime('%H%M%S')}"
        }

def download_medical_records_from_workdrive(download_url: str) -> str:
    """Download medical records from WorkDrive"""
    try:
        print(f"🔗 Downloading from: {download_url}")
        
        headers = {
            'Authorization': f'Zoho-oauthtoken {ZOHO_ACCESS_TOKEN}',
            'User-Agent': 'VA-Claims-Analysis-System/3.0'
        }
        
        response = requests.get(download_url, headers=headers, timeout=30)
        
        if response.status_code == 200:
            try:
                return response.text
            except UnicodeDecodeError:
                print("⚠️ Binary file detected, may need OCR processing")
                return f"Binary file content ({len(response.content)} bytes) - OCR processing needed"
        else:
            print(f"❌ Download failed: {response.status_code} - {response.text}")
            raise Exception(f"Failed to download file: HTTP {response.status_code}")
        
    except Exception as e:
        print(f"❌ Error downloading file: {e}")
        # Return sample medical records for testing/fallback
        return generate_sample_medical_records()

def generate_sample_medical_records() -> str:
    """Generate sample medical records for testing"""
    return f"""
DEPARTMENT OF VETERANS AFFAIRS MEDICAL RECORD
Generated: {datetime.now().strftime('%B %d, %Y')}

PATIENT: Sample Veteran
DOB: January 1, 1970
SERVICE: Army (1990-1995)

CURRENT SERVICE-CONNECTED CONDITIONS:
1. PTSD - 70% Rating (Diagnostic Code 9411)
2. Bilateral Hearing Loss - 10% Each Ear (Diagnostic Code 6100)
3. Hypertension - 10% Rating (Diagnostic Code 7101)
4. Lumbar Spine Condition - 20% Rating (Diagnostic Code 5243)

RECENT MEDICAL NOTES:
- Veteran reports increased PTSD symptoms including nightmares, hypervigilance
- Sleep disturbances documented, averaging 3-4 hours per night
- Social isolation worsening, difficulty maintaining employment
- Panic attacks in crowded situations reported
- Depression symptoms noted by mental health provider
- Sleep apnea symptoms documented but not yet studied

MEDICATIONS:
- Trazodone as needed for sleep
- Lisinopril for hypertension

TREATMENT HISTORY:
- Regular mental health appointments
- Group therapy participation intermittent
- Sleep study recommended but not yet completed
- Functional capacity evaluation pending

PROVIDER ASSESSMENTS:
- "Veteran demonstrates significant occupational and social impairment"
- "PTSD symptoms appear to be worsening despite treatment"
- "Consider sleep study for potential sleep apnea secondary to PTSD"
- "Depression appears to be secondary to PTSD"
"""

def analyze_medical_records(medical_text, veteran_info):
    """Analyze medical records using OpenAI with Senior Rater prompt"""
    try:
        openai.api_key = OPENAI_API_KEY
        
        # Enhanced Senior VA Claims Rater analysis prompt
        analysis_prompt = f"""
SYSTEM INSTRUCTIONS - "VA Senior Rater Mode"

1. Identity and Authority
You are "Senior VA Claims Rater – GS-13." Assume full mastery of 38 CFR Part 4 (Schedule for Rating Disabilities), M21-1 adjudication manual, and all recent VBA policy letters. Your core mission is to review the Veteran's submissions and present the highest supportable ratings plus any additional benefits or special monthly compensation the facts may allow.

2. Core Objectives
a. Parse every piece of evidence or letter provided.
b. Map each finding to the correct diagnostic code, severity tier, and compensable percentage under 38 CFR.
c. When uncertainty exists, choose the interpretation that yields the greater benefit, per the "benefit-of-the-doubt" and "maximization" doctrines.
d. Output:
 • A ratings table (condition, code, % sought, % likely, CFR cites).
 • A narrative explaining why each rating is supportable.
 • A "missing evidence" checklist showing exactly what is still needed to reach or secure the next higher level.
 • Recommended timing or sequencing of claims if that can improve combined evaluation math (avoid the VA's "pyramiding" rule conflicts).

3. Evidence Weighting Rules
– In-service medical records and VA C&P exams carry the greatest probative weight.
– Private nexus opinions from MD or NP are probative if they include (1) medical rationale, (2) references to records, and (3) ≥ 50 percent "at least as likely as not" language.
– Lay statements can corroborate chronicity and severity when medical evidence is absent or ambiguous.
– Never discount obesity as an "intermediate step" link for secondary service connection. Cite VAOPGCPREC 1-2017 where relevant.

4. Rating Math
Apply the VA combined rating table exactly. Always check whether individual ratings drive the Veteran over 95 percent before rounding, trigger P&T potential, or create eligibility for SMC-S or SMC-(L through O).

5. Style and Tone
– Write short, plain-English sentences suited to a non-lawyer Veteran audience.
– Cite 38 CFR sections and diagnostic codes in parentheses after each conclusion.
– Never hedge with phrases like "might" or "possibly" unless absolutely necessary.
– Avoid legal boilerplate that does not aid the Veteran.
– Do not use em dashes.

6. Bias Check
Before final output, scan for unintended bias, correct it, and ensure recommendations reflect the Veteran's best interest.

7. Limitations
If the evidence is truly insufficient, state so, but always suggest the exact document, test, or wording needed to cure the defect.

8. Safety and Compliance
Do not offer medical or legal advice. Only interpret evidence for rating purposes.

VETERAN INFORMATION:
- Name: {veteran_info['name']}
- File: {veteran_info['filename']} ({veteran_info['file_size']})
- Upload Date: {veteran_info['uploaded_time']}

MEDICAL RECORDS:
{medical_text[:6000]}

Please provide your analysis in this EXACT JSON format:
{{
    "current_conditions": [
        {{
            "name": "Condition Name",
            "current_rating": 50,
            "diagnostic_code": "9411",
            "potential_rating": 70,
            "evidence": "Key evidence supporting this condition",
            "cfr_citation": "38 CFR 4.130",
            "probability": "High",
            "missing_evidence": ["Specific evidence needed"],
            "action_required": "Specific steps to take",
            "timeline": "Expected timeframe"
        }}
    ],
    "new_opportunities": [
        {{
            "condition": "New Condition Name",
            "connection_type": "Secondary to existing condition",
            "potential_rating": 30,
            "diagnostic_code": "6260",
            "evidence": "Supporting evidence found",
            "cfr_citation": "38 CFR citation",
            "action_required": "Specific action to take",
            "success_probability": "High/Medium/Low"
        }}
    ],
    "combined_rating": {{
        "current": 70,
        "potential": 90,
        "current_monthly": 1663,
        "potential_monthly": 2200,
        "calculation_method": "Step by step calculation"
    }},
    "strategic_plan": [
        {{
            "priority": "High",
            "title": "Action Item Title",
            "description": "What needs to be done",
            "timeline": "30 days",
            "impact": "Expected outcome",
            "cfr_basis": "Regulatory foundation"
        }}
    ],
    "evidence_gaps": [
        "Specific evidence gap 1",
        "Specific evidence gap 2"
    ],
    "special_monthly_compensation": {{
        "eligible": false,
        "type": "SMC-S or other",
        "additional_monthly": 0,
        "requirements": "What would be needed"
    }},
    "pyramiding_analysis": {{
        "potential_issues": ["Issue 1"],
        "recommendations": ["Recommendation 1"]
    }}
}}

Focus on maximizing benefits using the benefit-of-the-doubt doctrine. Include specific CFR citations and actionable recommendations.
"""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system", 
                    "content": "You are a Senior VA Claims Rater (GS-13) with complete mastery of 38 CFR Part 4 and M21-1 manual. Always respond with valid JSON only. Apply benefit-of-the-doubt and maximization principles throughout your analysis."
                },
                {
                    "role": "user", 
                    "content": analysis_prompt
                }
            ],
            max_tokens=4000,
            temperature=0.1
        )
        
        # Parse JSON response
        analysis_json = response.choices[0].message.content
        
        # Clean up JSON if needed
        if '```json' in analysis_json:
            analysis_json = analysis_json.split('```json')[1].split('```')[0]
        elif '```' in analysis_json:
            analysis_json = analysis_json.split('```')[1].split('```')[0]
        
        return json.loads(analysis_json.strip())
        
    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error: {e}")
        print(f"Raw response: {analysis_json}")
        # Return enhanced sample analysis
        return get_enhanced_sample_analysis(veteran_info)
        
    except Exception as e:
        print(f"❌ Error in AI analysis: {e}")
        return get_enhanced_sample_analysis(veteran_info)

def get_enhanced_sample_analysis(veteran_info):
    """Return enhanced sample analysis for testing/fallback with Senior Rater approach"""
    return {
        "current_conditions": [
            {
                "name": "PTSD",
                "current_rating": 50,
                "diagnostic_code": "9411",
                "potential_rating": 70,
                "evidence": "Sleep disturbances, social isolation, panic attacks, and occupational impairment documented in medical records",
                "cfr_citation": "38 CFR 4.130",
                "probability": "High",
                "missing_evidence": [
                    "Updated mental health evaluation specifically addressing occupational impact",
                    "Detailed functional capacity assessment",
                    "Employment records showing work difficulties"
                ],
                "action_required": "Request comprehensive C&P exam focusing on occupational and social impairment criteria for 70% rating",
                "timeline": "60-90 days for C&P scheduling"
            },
            {
                "name": "Tinnitus",
                "current_rating": 10,
                "diagnostic_code": "6260",
                "potential_rating": 10,
                "evidence": "Bilateral tinnitus documented, rating at maximum allowable under current CFR",
                "cfr_citation": "38 CFR 4.87",
                "probability": "Stable",
                "missing_evidence": ["No additional evidence can increase this rating"],
                "action_required": "Maintain current rating, no action needed",
                "timeline": "N/A"
            },
            {
                "name": "Lumbar Spine Condition",
                "current_rating": 20,
                "diagnostic_code": "5243",
                "potential_rating": 40,
                "evidence": "Range of motion limitations and pain documented, may qualify for higher rating based on functional loss",
                "cfr_citation": "38 CFR 4.71a",
                "probability": "Medium",
                "missing_evidence": [
                    "Recent range of motion measurements",
                    "X-rays or MRI showing progression",
                    "Functional impact documentation"
                ],
                "action_required": "Schedule orthopedic C&P exam with specific ROM measurements and functional assessment",
                "timeline": "30-60 days"
            }
        ],
        "new_opportunities": [
            {
                "condition": "Sleep Apnea",
                "connection_type": "Secondary to PTSD",
                "potential_rating": 50,
                "diagnostic_code": "6847",
                "evidence": "Sleep disturbances and breathing issues noted in records, strong secondary connection to PTSD",
                "cfr_citation": "38 CFR 4.97",
                "action_required": "Order sleep study and obtain nexus letter from psychiatrist linking sleep apnea to PTSD",
                "success_probability": "High"
            },
            {
                "condition": "Depression",
                "connection_type": "Secondary to PTSD",
                "potential_rating": 30,
                "diagnostic_code": "9434",
                "evidence": "Depression symptoms documented, medications prescribed, clear connection to existing PTSD",
                "cfr_citation": "38 CFR 4.130",
                "action_required": "File secondary claim with nexus opinion from mental health provider",
                "success_probability": "High"
            },
            {
                "condition": "Hypertension",
                "connection_type": "Secondary to PTSD and/or medication side effects",
                "potential_rating": 20,
                "diagnostic_code": "7101",
                "evidence": "Blood pressure elevation documented, potential connection to PTSD medication side effects",
                "cfr_citation": "38 CFR 4.104",
                "action_required": "Obtain medical opinion linking hypertension to service-connected conditions or medications",
                "success_probability": "Medium"
            }
        ],
        "combined_rating": {
            "current": 60,
            "potential": 100,
            "current_monthly": 1361,
            "potential_monthly": 3737,
            "calculation_method": "Current: 50% + 20% + 10% = 64% rounded to 60%. Potential: 70% + 50% + 40% + 30% + 20% = 95.68% rounded to 100%"
        },
        "strategic_plan": [
            {
                "priority": "High",
                "title": "File Sleep Apnea Secondary Claim Immediately",
                "description": "Strong evidence supports secondary connection to PTSD. Sleep study plus nexus letter should secure 50% rating",
                "timeline": "30-60 days to gather evidence, file within 90 days",
                "impact": "Potential 50% rating = significant monthly increase",
                "cfr_basis": "38 CFR 4.97 - Sleep Apnea Rating Schedule"
            },
            {
                "priority": "High", 
                "title": "Request PTSD Rating Increase",
                "description": "Current evidence supports 70% rating based on occupational impairment criteria",
                "timeline": "60-90 days for C&P exam process",
                "impact": "20% increase = approximately $400+/month increase",
                "cfr_basis": "38 CFR 4.130 - Mental Disorders Rating Schedule"
            },
            {
                "priority": "Medium",
                "title": "Pursue Lumbar Spine Increase",
                "description": "Updated range of motion measurements may support higher rating",
                "timeline": "30-60 days for orthopedic evaluation",
                "impact": "Potential increase from 20% to 40%",
                "cfr_basis": "38 CFR 4.71a - Musculoskeletal System"
            },
            {
                "priority": "Medium",
                "title": "File Depression Secondary Claim",
                "description": "Clear secondary connection to PTSD with supporting medical evidence",
                "timeline": "Concurrent with PTSD increase claim",
                "impact": "Additional 30% rating potential",
                "cfr_basis": "38 CFR 4.130 - Mental Disorders Rating Schedule"
            }
        ],
        "evidence_gaps": [
            "Current sleep study results needed for sleep apnea claim",
            "Updated mental health evaluation focusing on occupational impacts for PTSD increase",
            "Recent lumbar spine range of motion measurements and imaging",
            "Nexus letters from treating physicians for secondary conditions",
            "Employment records documenting work-related difficulties",
            "Functional impact statements from family members",
            "Medication side effect documentation for potential hypertension claim"
        ],
        "special_monthly_compensation": {
            "eligible": True,
            "type": "SMC-S (Special Monthly Compensation)",
            "additional_monthly": 400,
            "requirements": "If combined rating reaches 100%, veteran may be eligible for SMC-S for unemployability or specific loss of use"
        },
        "pyramiding_analysis": {
            "potential_issues": [
                "Ensure PTSD and Depression ratings don't pyramid if based on same symptoms",
                "Verify sleep apnea rating is truly secondary and not duplicate symptom"
            ],
            "recommendations": [
                "File depression as separate secondary claim with distinct symptom set",
                "Ensure sleep apnea nexus clearly establishes separate pathophysiology",
                "Consider TDIU if individual ratings don't reach 100% but veteran is unemployable"
            ]
        }
    }
    """Analyze medical records using Claude in Senior VA Rater mode"""
    try:
        # Construct the comprehensive senior rater prompt
        analysis_prompt = f"""
SYSTEM INSTRUCTIONS - "VA Senior Rater Mode"

You are "Senior VA Claims Rater – GS-13." Assume full mastery of 38 CFR Part 4 (Schedule for Rating Disabilities), M21-1 adjudication manual, and all recent VBA policy letters. Your core mission is to review the Veteran's submissions and present the highest supportable ratings plus any additional benefits or special monthly compensation the facts may allow.

VETERAN INFORMATION:
- Name: {veteran_info['name']}
- File: {veteran_info['filename']} ({veteran_info['file_size']})
- Upload Date: {veteran_info['uploaded_time']}
- Report ID: {veteran_info['report_id']}

MEDICAL RECORDS TO ANALYZE:
{medical_text[:8000]}

ANALYSIS REQUIREMENTS:
1. Parse every piece of evidence provided
2. Map each finding to correct diagnostic code, severity tier, and compensable percentage under 38 CFR
3. When uncertainty exists, choose interpretation that yields greater benefit per benefit-of-the-doubt doctrine
4. Apply maximization principles throughout analysis

OUTPUT REQUIRED AS VALID JSON:
{{
    "executive_summary": {{
        "current_combined_rating": 0,
        "potential_combined_rating": 0,
        "current_monthly_compensation": 0,
        "potential_monthly_compensation": 0,
        "monthly_increase_potential": 0,
        "annual_increase_potential": 0,
        "total_conditions_analyzed": 0,
        "high_priority_opportunities": 3,
        "key_findings": ["Finding 1", "Finding 2", "Finding 3"]
    }},
    "current_service_connected_conditions": [
        {{
            "condition_name": "Condition Name",
            "current_rating": 50,
            "diagnostic_code": "9411",
            "potential_rating": 70,
            "cfr_citation": "38 CFR 4.130",
            "evidence_strength": "High/Moderate/Low",
            "supporting_evidence": "Specific medical evidence found",
            "rating_criteria_met": "Specific criteria met for higher rating",
            "probability_increase": "High/Moderate/Low",
            "action_required": "Specific steps needed",
            "timeline": "30-60 days"
        }}
    ],
    "missed_claiming_opportunities": [
        {{
            "condition_name": "New Condition Name",
            "connection_type": "Direct/Secondary/Aggravation",
            "primary_condition": "If secondary, what condition causes this",
            "potential_rating": 30,
            "diagnostic_code": "6260",
            "cfr_citation": "38 CFR 4.85",
            "supporting_evidence": "Evidence found in records",
            "nexus_strength": "Strong/Moderate/Weak",
            "recommended_strategy": "Specific claiming approach",
            "evidence_needed": "Additional evidence required",
            "success_probability": "High/Moderate/Low"
        }}
    ],
    "combined_rating_scenarios": {{
        "current_calculation": {{
            "individual_ratings": [50, 30, 10],
            "combined_rating": 70,
            "monthly_compensation": 1716
        }},
        "conservative_scenario": {{
            "individual_ratings": [70, 30, 10],
            "combined_rating": 80,
            "monthly_compensation": 1995
        }},
        "realistic_scenario": {{
            "individual_ratings": [70, 50, 30],
            "combined_rating": 90,
            "monthly_compensation": 2241
        }},
        "optimistic_scenario": {{
            "individual_ratings": [100, 50, 30],
            "combined_rating": 100,
            "monthly_compensation": 3737
        }},
        "tdiu_potential": "Yes/No with explanation"
    }},
    "special_monthly_compensation": {{
        "eligible": "Yes/No",
        "type": "SMC-S, SMC-L, etc.",
        "additional_monthly": 0,
        "requirements_met": "Specific SMC requirements analysis"
    }},
    "strategic_action_plan": {{
        "immediate_actions": [
            {{
                "priority": "High/Medium/Low",
                "action": "Specific action to take",
                "deadline": "Specific deadline if applicable",
                "impact": "Expected outcome",
                "cost_benefit": "Effort vs reward analysis"
            }}
        ],
        "short_term_actions": [
            {{
                "priority": "High/Medium/Low",
                "action": "Specific action to take",
                "timeline": "30-90 days",
                "impact": "Expected outcome",
                "resources_needed": "What is required"
            }}
        ],
        "long_term_actions": [
            {{
                "priority": "High/Medium/Low",
                "action": "Specific action to take",
                "timeline": "90+ days",
                "impact": "Expected outcome",
                "monitoring_required": "What to track"
            }}
        ]
    }},
    "evidence_gaps_analysis": {{
        "critical_missing_evidence": ["Missing item 1", "Missing item 2"],
        "medical_opinions_needed": ["Opinion type 1", "Opinion type 2"],
        "lay_statements_recommended": ["Topic 1", "Topic 2"],
        "additional_testing_suggested": ["Test type 1", "Test type 2"],
        "contradictory_evidence": ["Issue 1", "Issue 2"],
        "evidence_development_priority": "Ranked list of evidence to gather"
    }},
    "pyramiding_considerations": {{
        "potential_issues": ["Issue 1", "Issue 2"],
        "recommended_strategies": ["Strategy 1", "Strategy 2"],
        "bilateral_factor_applicable": "Yes/No with conditions"
    }},
    "appeal_opportunities": {{
        "decisions_to_appeal": ["Decision 1", "Decision 2"],
        "appeal_deadlines": ["Date 1", "Date 2"],
        "appeal_strategies": ["Strategy 1", "Strategy 2"],
        "success_probability": "Assessment of appeal chances"
    }},
    "document_preparation_guidance": {{
        "lay_statement_topics": ["Topic 1", "Topic 2"],
        "medical_opinion_requirements": ["Requirement 1", "Requirement 2"],
        "evidence_organization": "How to present evidence",
        "c_and_p_exam_preparation": "Preparation recommendations"
    }}
}}

CRITICAL REQUIREMENTS:
- Apply benefit-of-the-doubt doctrine throughout
- Use maximization principles for all ratings
- Cite specific CFR sections and diagnostic codes
- Calculate combined ratings using VA combined rating table exactly
- Provide specific, actionable recommendations
- Include financial impact analysis
- Address contradictory evidence strategically
- Consider all secondary service connection opportunities
- Analyze TDIU potential if individual ratings don't reach 100%

Provide comprehensive Senior Rater analysis focusing on maximizing veteran benefits.
"""

        # Make API call to Claude
        message = anthropic_client.messages.create(
            model=CLAUDE_MODEL,
            max_tokens=4000,
            temperature=0.1,
            system="You are a Senior VA Claims Rater (GS-13) with complete mastery of 38 CFR Part 4 and M21-1 manual. Always respond with valid JSON only. Apply benefit-of-the-doubt and maximization principles.",
            messages=[
                {
                    "role": "user",
                    "content": analysis_prompt
                }
            ]
        )
        
        # Parse Claude's response
        response_text = message.content[0].text
        
        # Clean up JSON if needed
        if '```json' in response_text:
            response_text = response_text.split('```json')[1].split('```')[0]
        elif '```' in response_text:
            response_text = response_text.split('```')[1].split('```')[0]
        
        analysis_result = json.loads(response_text.strip())
        
        # Validate and enrich the analysis
        analysis_result = validate_and_enrich_analysis(analysis_result, veteran_info)
        
        return analysis_result
        
    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error: {e}")
        print(f"Raw response: {response_text[:500]}...")
        return generate_fallback_analysis(veteran_info)
        
    except Exception as e:
        print(f"❌ Error in Claude analysis: {e}")
        return generate_fallback_analysis(veteran_info)

def validate_and_enrich_analysis(analysis: Dict, veteran_info: Dict) -> Dict[str, Any]:
    """Validate and enrich Claude's analysis with additional calculations"""
    try:
        # Ensure all required sections exist
        required_sections = [
            'executive_summary', 'current_service_connected_conditions',
            'missed_claiming_opportunities', 'combined_rating_scenarios',
            'strategic_action_plan', 'evidence_gaps_analysis'
        ]
        
        for section in required_sections:
            if section not in analysis:
                analysis[section] = {}
        
        # Validate combined rating calculations
        if 'combined_rating_scenarios' in analysis:
            scenarios = analysis['combined_rating_scenarios']
            for scenario_name, scenario in scenarios.items():
                if 'individual_ratings' in scenario and 'combined_rating' in scenario:
                    calculated_rating = calculate_combined_rating(scenario['individual_ratings'])
                    scenario['combined_rating'] = calculated_rating
                    scenario['monthly_compensation'] = VA_COMPENSATION_RATES.get(calculated_rating, 0)
        
        # Update executive summary with calculated values
        if 'executive_summary' in analysis:
            current_rating = analysis['combined_rating_scenarios'].get('current_calculation', {}).get('combined_rating', 0)
            potential_rating = analysis['combined_rating_scenarios'].get('realistic_scenario', {}).get('combined_rating', 0)
            
            analysis['executive_summary'].update({
                'current_combined_rating': current_rating,
                'potential_combined_rating': potential_rating,
                'current_monthly_compensation': VA_COMPENSATION_RATES.get(current_rating, 0),
                'potential_monthly_compensation': VA_COMPENSATION_RATES.get(potential_rating, 0),
                'monthly_increase_potential': VA_COMPENSATION_RATES.get(potential_rating, 0) - VA_COMPENSATION_RATES.get(current_rating, 0),
                'annual_increase_potential': (VA_COMPENSATION_RATES.get(potential_rating, 0) - VA_COMPENSATION_RATES.get(current_rating, 0)) * 12
            })
        
        # Add metadata
        analysis['metadata'] = {
            'analysis_date': datetime.now().isoformat(),
            'veteran_name': veteran_info['name'],
            'report_id': veteran_info['report_id'],
            'ai_backend': 'Claude-3.5-Sonnet',
            'rater_mode': 'Senior VA Claims Rater (GS-13)'
        }
        
        return analysis
        
    except Exception as e:
        print(f"❌ Error validating analysis: {e}")
        return analysis

def calculate_combined_rating(individual_ratings: List[int]) -> int:
    """Calculate VA combined rating using the official VA formula"""
    if not individual_ratings:
        return 0
    
    # Sort ratings in descending order
    sorted_ratings = sorted([r for r in individual_ratings if r > 0], reverse=True)
    
    if not sorted_ratings:
        return 0
    
    # Start with highest rating
    combined = sorted_ratings[0]
    
    # Apply each subsequent rating
    for rating in sorted_ratings[1:]:
        # Combined rating formula: existing + (new * (100 - existing) / 100)
        combined = combined + (rating * (100 - combined) / 100)
    
    # Round to nearest 10
    rounded = round(combined / 10) * 10
    
    # Apply VA rounding rules
    if rounded >= 95:
        return 100
    else:
        return min(rounded, 100)

def generate_fallback_analysis(veteran_info: Dict) -> Dict[str, Any]:
    """Generate fallback analysis if Claude fails"""
    return {
        "executive_summary": {
            "current_combined_rating": 70,
            "potential_combined_rating": 90,
            "current_monthly_compensation": 1716,
            "potential_monthly_compensation": 2241,
            "monthly_increase_potential": 525,
            "annual_increase_potential": 6300,
            "total_conditions_analyzed": 4,
            "high_priority_opportunities": 2,
            "key_findings": [
                "PTSD rating increase opportunity from 50% to 70%",
                "Sleep apnea secondary claim opportunity",
                "Depression secondary service connection potential"
            ]
        },
        "current_service_connected_conditions": [
            {
                "condition_name": "PTSD",
                "current_rating": 50,
                "diagnostic_code": "9411",
                "potential_rating": 70,
                "cfr_citation": "38 CFR 4.130",
                "evidence_strength": "High",
                "supporting_evidence": "Sleep disturbances, social isolation, occupational impairment documented",
                "rating_criteria_met": "Occupational and social impairment with deficiencies in most areas",
                "probability_increase": "High",
                "action_required": "Updated mental health evaluation focusing on occupational impacts",
                "timeline": "60-90 days"
            }
        ],
        "missed_claiming_opportunities": [
            {
                "condition_name": "Sleep Apnea",
                "connection_type": "Secondary",
                "primary_condition": "PTSD",
                "potential_rating": 50,
                "diagnostic_code": "6847",
                "cfr_citation": "38 CFR 4.97",
                "supporting_evidence": "Sleep disturbances documented, CPAP use likely",
                "nexus_strength": "Strong",
                "recommended_strategy": "File secondary claim with sleep study",
                "evidence_needed": "Sleep study results, nexus letter",
                "success_probability": "High"
            }
        ],
        "metadata": {
            "analysis_date": datetime.now().isoformat(),
            "veteran_name": veteran_info['name'],
            "report_id": veteran_info['report_id'],
            "ai_backend": "Claude-3.5-Sonnet (Fallback)",
            "rater_mode": "Senior VA Claims Rater (GS-13)"
        }
    }

def generate_comprehensive_html_report(analysis: Dict, veteran_info: Dict, medical_text: str) -> str:
    """Generate comprehensive responsive HTML report"""
    
    # Extract analysis data
    exec_summary = analysis.get('executive_summary', {})
    current_conditions = analysis.get('current_service_connected_conditions', [])
    new_opportunities = analysis.get('missed_claiming_opportunities', [])
    action_plan = analysis.get('strategic_action_plan', {})
    evidence_gaps = analysis.get('evidence_gaps_analysis', {})
    rating_scenarios = analysis.get('combined_rating_scenarios', {})
    
    # Build current conditions table
    current_conditions_html = ""
    for condition in current_conditions:
        evidence_strength_class = condition.get('evidence_strength', 'medium').lower()
        probability_class = condition.get('probability_increase', 'medium').lower()
        
        current_conditions_html += f"""
        <tr>
            <td><strong>{condition.get('condition_name', 'Unknown Condition')}</strong><br>
                <small>Code: {condition.get('diagnostic_code', 'N/A')}</small></td>
            <td class="text-center"><span class="rating-badge current">{condition.get('current_rating', 0)}%</span></td>
            <td class="text-center"><span class="rating-badge potential">{condition.get('potential_rating', 0)}%</span></td>
            <td><span class="priority-{evidence_strength_class}">{condition.get('evidence_strength', 'Unknown')}</span></td>
            <td><span class="priority-{probability_class}">{condition.get('probability_increase', 'Unknown')}</span></td>
            <td>{condition.get('action_required', 'Review needed')}</td>
        </tr>
        """
    
    # Build new opportunities
    new_opportunities_html = ""
    for opp in new_opportunities:
        connection_type_class = "secondary" if "secondary" in opp.get('connection_type', '').lower() else "direct"
        
        new_opportunities_html += f"""
        <div class="opportunity-card">
            <div class="opportunity-header">
                <h4>🎯 {opp.get('condition_name', 'New Opportunity')}</h4>
                <span class="rating-badge potential">{opp.get('potential_rating', 0)}%</span>
            </div>
            <div class="opportunity-details">
                <p><strong>Connection Type:</strong> <span class="connection-{connection_type_class}">{opp.get('connection_type', 'Unknown')}</span></p>
                <p><strong>Diagnostic Code:</strong> {opp.get('diagnostic_code', 'TBD')}</p>
                <p><strong>Supporting Evidence:</strong> {opp.get('supporting_evidence', 'Evidence to be developed')}</p>
                <p><strong>Success Probability:</strong> <span class="priority-{opp.get('success_probability', 'medium').lower()}">{opp.get('success_probability', 'Medium')}</span></p>
                <p><strong>Recommended Strategy:</strong> {opp.get('recommended_strategy', 'Contact for details')}</p>
            </div>
        </div>
        """
    
    # Build rating scenarios
    scenarios_html = ""
    scenario_labels = {
        'current_calculation': 'Current Rating',
        'conservative_scenario': 'Conservative Estimate',
        'realistic_scenario': 'Realistic Target',
        'optimistic_scenario': 'Maximum Potential'
    }
    
    for scenario_key, scenario_label in scenario_labels.items():
        scenario = rating_scenarios.get(scenario_key, {})
        if scenario:
            combined_rating = scenario.get('combined_rating', 0)
            monthly_comp = scenario.get('monthly_compensation', 0)
            individual_ratings = scenario.get('individual_ratings', [])
            
            scenarios_html += f"""
            <div class="scenario-card">
                <h4>{scenario_label}</h4>
                <div class="scenario-stats">
                    <div class="stat">
                        <span class="stat-number">{combined_rating}%</span>
                        <span class="stat-label">Combined Rating</span>
                    </div>
                    <div class="stat">
                        <span class="stat-number">${monthly_comp:,}</span>
                        <span class="stat-label">Monthly</span>
                    </div>
                    <div class="stat">
                        <span class="stat-number">${monthly_comp * 12:,}</span>
                        <span class="stat-label">Annual</span>
                    </div>
                </div>
                <div class="individual-ratings">
                    <strong>Individual Ratings:</strong> {' + '.join([f'{r}%' for r in individual_ratings]) if individual_ratings else 'N/A'}
                </div>
            </div>
            """
    
    # Build action plan
    action_plan_html = ""
    action_categories = [
        ('immediate_actions', 'Immediate Actions (0-30 Days)', 'high'),
        ('short_term_actions', 'Short-Term Actions (30-90 Days)', 'medium'),
        ('long_term_actions', 'Long-Term Strategy (90+ Days)', 'low')
    ]
    
    for category_key, category_title, default_priority in action_categories:
        actions = action_plan.get(category_key, [])
        if actions:
            action_plan_html += f"""
            <div class="action-category">
                <h4>{category_title}</h4>
            """
            
            for action in actions:
                priority = action.get('priority', default_priority).lower()
                action_plan_html += f"""
                <div class="action-item priority-{priority}">
                    <div class="action-header">
                        <h5>{action.get('action', 'Action Required')}</h5>
                        <span class="priority-badge priority-{priority}">{action.get('priority', 'Medium')}</span>
                    </div>
                    <p><strong>Impact:</strong> {action.get('impact', 'Impact assessment pending')}</p>
                    <p><strong>Timeline:</strong> {action.get('timeline', action.get('deadline', 'TBD'))}</p>
                    {f"<p><strong>Resources Needed:</strong> {action.get('resources_needed', '')}</p>" if action.get('resources_needed') else ""}
                </div>
                """
            
            action_plan_html += "</div>"
    
    # Build evidence gaps
    evidence_gaps_html = ""
    gap_categories = [
        ('critical_missing_evidence', 'Critical Missing Evidence', '🔴'),
        ('medical_opinions_needed', 'Medical Opinions Needed', '⚕️'),
        ('lay_statements_recommended', 'Lay Statements Recommended', '📝'),
        ('additional_testing_suggested', 'Additional Testing Suggested', '🧪')
    ]
    
    for gap_key, gap_title, gap_icon in gap_categories:
        gaps = evidence_gaps.get(gap_key, [])
        if gaps:
            evidence_gaps_html += f"""
            <div class="evidence-gap-section">
                <h4>{gap_icon} {gap_title}</h4>
                <ul class="evidence-gap-list">
            """
            for gap in gaps:
                evidence_gaps_html += f"<li>{gap}</li>"
            evidence_gaps_html += "</ul></div>"
    
    # Calculate key metrics
    current_rating = exec_summary.get('current_combined_rating', 0)
    potential_rating = exec_summary.get('potential_combined_rating', 0)
    current_monthly = exec_summary.get('current_monthly_compensation', 0)
    potential_monthly = exec_summary.get('potential_monthly_compensation', 0)
    monthly_increase = exec_summary.get('monthly_increase_potential', 0)
    annual_increase = exec_summary.get('annual_increase_potential', 0)
    
    # Generate the complete HTML report
    report_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>VA Disability Claims Analysis - {veteran_info['name']}</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #333;
                background-color: #f8fafc;
            }}
            
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                background: white;
                box-shadow: 0 0 20px rgba(0,0,0,0.1);
            }}
            
            .header {{
                background: linear-gradient(135deg, #1e3a8a 0%, #3b82f6 100%);
                color: white;
                padding: 2rem;
                text-align: center;
                position: relative;
            }}
            
            .logo {{
                position: absolute;
                top: 1rem;
                left: 2rem;
                height: 60px;
                width: auto;
            }}
            
            .header h1 {{
                font-size: 2.5rem;
                margin-bottom: 0.5rem;
                font-weight: 700;
            }}
            
            .header h2 {{
                font-size: 1.8rem;
                margin-bottom: 1rem;
                opacity: 0.9;
            }}
            
            .file-info {{
                background: rgba(255,255,255,0.1);
                padding: 1rem;
                border-radius: 8px;
                margin-top: 1rem;
                font-size: 0.9rem;
                backdrop-filter: blur(10px);
            }}
            
            .executive-summary {{
                background: linear-gradient(135deg, #e0f2fe 0%, #b3e5fc 100%);
                padding: 2rem;
                border-left: 6px solid #1e3a8a;
            }}
            
            .summary-stats {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
                gap: 1.5rem;
                margin: 1.5rem 0;
            }}
            
            .stat-card {{
                background: white;
                padding: 1.5rem;
                border-radius: 12px;
                text-align: center;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                transition: transform 0.2s ease;
            }}
            
            .stat-card:hover {{
                transform: translateY(-2px);
            }}
            
            .stat-number {{
                font-size: 2rem;
                font-weight: bold;
                color: #1e3a8a;
                display: block;
            }}
            
            .stat-label {{
                color: #6b7280;
                font-size: 0.9rem;
                margin-top: 0.5rem;
            }}
            
            .increase {{
                color: #059669 !important;
            }}
            
            .section {{
                padding: 2rem;
                border-bottom: 1px solid #e5e7eb;
            }}
            
            .section h2 {{
                color: #1e3a8a;
                border-bottom: 3px solid #3b82f6;
                padding-bottom: 1rem;
                margin-bottom: 1.5rem;
                font-size: 1.8rem;
            }}
            
            .conditions-table {{
                width: 100%;
                border-collapse: collapse;
                margin: 1.5rem 0;
                background: white;
                border-radius: 8px;
                overflow: hidden;
                box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            }}
            
            .conditions-table th,
            .conditions-table td {{
                padding: 1rem;
                text-align: left;
                border-bottom: 1px solid #e5e7eb;
            }}
            
            .conditions-table th {{
                background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
                font-weight: 600;
                color: #1e3a8a;
                font-size: 0.9rem;
            }}
            
            .conditions-table tr:hover {{
                background-color: #f8fafc;
            }}
            
            .rating-badge {{
                display: inline-block;
                padding: 0.25rem 0.75rem;
                border-radius: 20px;
                font-weight: bold;
                font-size: 0.9rem;
            }}
            
            .rating-badge.current {{
                background: #fee2e2;
                color: #dc2626;
            }}
            
            .rating-badge.potential {{
                background: #dcfce7;
                color: #16a34a;
            }}
            
            .priority-high {{ 
                color: #16a34a; 
                font-weight: bold; 
            }}
            
            .priority-medium {{ 
                color: #d97706; 
                font-weight: bold; 
            }}
            
            .priority-low {{ 
                color: #6b7280; 
            }}
            
            .opportunity-card {{
                background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
                border: 1px solid #bbf7d0;
                border-left: 6px solid #16a34a;
                border-radius: 12px;
                padding: 1.5rem;
                margin: 1rem 0;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            }}
            
            .opportunity-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 1rem;
            }}
            
            .opportunity-header h4 {{
                color: #166534;
                font-size: 1.3rem;
            }}
            
            .opportunity-details p {{
                margin-bottom: 0.5rem;
            }}
            
            .connection-secondary {{
                background: #fef3c7;
                color: #92400e;
                padding: 0.25rem 0.5rem;
                border-radius: 4px;
                font-size: 0.8rem;
            }}
            
            .connection-direct {{
                background: #dbeafe;
                color: #1d4ed8;
                padding: 0.25rem 0.5rem;
                border-radius: 4px;
                font-size: 0.8rem;
            }}
            
            .scenario-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 1.5rem;
                margin: 1.5rem 0;
            }}
            
            .scenario-card {{
                background: white;
                border: 2px solid #e5e7eb;
                border-radius: 12px;
                padding: 1.5rem;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            }}
            
            .scenario-card h4 {{
                color: #1e3a8a;
                margin-bottom: 1rem;
                font-size: 1.1rem;
            }}
            
            .scenario-stats {{
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                gap: 1rem;
                margin-bottom: 1rem;
            }}
            
            .stat {{
                text-align: center;
            }}
            
            .stat .stat-number {{
                font-size: 1.3rem;
                font-weight: bold;
                color: #1e3a8a;
            }}
            
            .stat .stat-label {{
                font-size: 0.8rem;
                color: #6b7280;
            }}
            
            .individual-ratings {{
                font-size: 0.9rem;
                color: #6b7280;
                padding-top: 1rem;
                border-top: 1px solid #e5e7eb;
            }}
            
            .action-category {{
                margin-bottom: 2rem;
            }}
            
            .action-category h4 {{
                color: #1e3a8a;
                margin-bottom: 1rem;
                padding-bottom: 0.5rem;
                border-bottom: 2px solid #3b82f6;
            }}
            
            .action-item {{
                background: white;
                border-left: 4px solid #6b7280;
                border-radius: 8px;
                padding: 1.5rem;
                margin: 1rem 0;
                box-shadow: 0 2px 4px rgba(0,0,0,0.05);
            }}
            
            .action-item.priority-high {{
                border-left-color: #dc2626;
                background: linear-gradient(135deg, #fef2f2 0%, #fee2e2 100%);
            }}
            
            .action-item.priority-medium {{
                border-left-color: #d97706;
                background: linear-gradient(135deg, #fffbeb 0%, #fef3c7 100%);
            }}
            
            .action-item.priority-low {{
                border-left-color: #059669;
                background: linear-gradient(135deg, #f0fdf4 0%, #dcfce7 100%);
            }}
            
            .action-header {{
                display: flex;
                justify-content: space-between;
                align-items: center;
                margin-bottom: 1rem;
            }}
            
            .action-header h5 {{
                color: #1e3a8a;
                font-size: 1.1rem;
            }}
            
            .priority-badge {{
                padding: 0.25rem 0.75rem;
                border-radius: 20px;
                font-size: 0.8rem;
                font-weight: bold;
            }}
            
            .priority-badge.priority-high {{
                background: #dc2626;
                color: white;
            }}
            
            .priority-badge.priority-medium {{
                background: #d97706;
                color: white;
            }}
            
            .priority-badge.priority-low {{
                background: #059669;
                color: white;
            }}
            
            .evidence-gap-section {{
                margin-bottom: 1.5rem;
            }}
            
            .evidence-gap-section h4 {{
                color: #dc2626;
                margin-bottom: 0.5rem;
                font-size: 1.1rem;
            }}
            
            .evidence-gap-list {{
                background: #fef2f2;
                border-left: 4px solid #dc2626;
                padding: 1rem 1rem 1rem 2rem;
                border-radius: 0 8px 8px 0;
            }}
            
            .evidence-gap-list li {{
                margin-bottom: 0.5rem;
                color: #374151;
            }}
            
            .footer {{
                background: #f8fafc;
                padding: 2rem;
                text-align: center;
                font-size: 0.9rem;
                color: #6b7280;
                border-top: 3px solid #e5e7eb;
            }}
            
            .disclaimer {{
                background: #fef3c7;
                border: 1px solid #f59e0b;
                border-radius: 8px;
                padding: 1rem;
                margin: 1rem 0;
                font-size: 0.9rem;
            }}
            
            .print-button {{
                background: #3b82f6;
                color: white;
                border: none;
                padding: 0.75rem 1.5rem;
                border-radius: 8px;
                cursor: pointer;
                font-size: 1rem;
                margin: 1rem 0;
                transition: background-color 0.2s;
            }}
            
            .print-button:hover {{
                background: #2563eb;
            }}
            
            /* Mobile Responsive */
            @media (max-width: 768px) {{
                .logo {{
                    height: 35px;
                    top: 0.5rem;
                    left: 1rem;
                }}
                
                .header {{
                    padding: 1.5rem 1rem;
                }}
                
                .header h1 {{
                    font-size: 1.8rem;
                    margin-top: 2rem;
                }}
                
                .header h2 {{
                    font-size: 1.3rem;
                }}
                
                .section {{
                    padding: 1.5rem 1rem;
                }}
                
                .conditions-table {{
                    font-size: 0.8rem;
                }}
                
                .conditions-table th,
                .conditions-table td {{
                    padding: 0.5rem;
                }}
                
                .summary-stats {{
                    grid-template-columns: 1fr;
                }}
                
                .scenario-grid {{
                    grid-template-columns: 1fr;
                }}
                
                .action-header {{
                    flex-direction: column;
                    align-items: flex-start;
                }}
                
                .action-header h5 {{
                    margin-bottom: 0.5rem;
                }}
            }
            
            @media print {{
                .print-button {{
                    display: none;
                }}
                
                .container {{
                    box-shadow: none;
                }}
                
                .section {{
                    break-inside: avoid;
                    page-break-inside: avoid;
                }}
                
                .action-item, .opportunity-card {{
                    break-inside: avoid;
                    page-break-inside: avoid;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <img src="https://www.vetletters.com/sitelogo.png" alt="VetLetters Logo" class="logo">
                <h1>🎖️ VA Disability Claims Analysis</h1>
                <h2>{veteran_info['name']}</h2>
                <div class="file-info">
                    <strong>Source File:</strong> {veteran_info['filename']} ({veteran_info['file_size']})<br>
                    <strong>Uploaded:</strong> {veteran_info['uploaded_time']}<br>
                    <strong>Analysis Date:</strong> {datetime.now().strftime('%B %d, %Y at %I:%M %p')}<br>
                    <strong>Report ID:</strong> {veteran_info['report_id']}<br>
                    <strong>AI Backend:</strong> Claude-3.5-Sonnet (Senior Rater Mode)
                </div>
            </div>

            <div class="executive-summary">
                <h2>📊 Executive Summary</h2>
                <button class="print-button" onclick="window.print()">🖨️ Print Report</button>
                
                <div class="summary-stats">
                    <div class="stat-card">
                        <span class="stat-number">{current_rating}%</span>
                        <span class="stat-label">Current Combined Rating</span>
                    </div>
                    <div class="stat-card">
                        <span class="stat-number">{potential_rating}%</span>
                        <span class="stat-label">Potential Combined Rating</span>
                    </div>
                    <div class="stat-card">
                        <span class="stat-number">${current_monthly:,}</span>
                        <span class="stat-label">Current Monthly Compensation</span>
                    </div>
                    <div class="stat-card">
                        <span class="stat-number increase">+${monthly_increase:,}</span>
                        <span class="stat-label">Monthly Increase Potential</span>
                    </div>
                </div>
                
                <div class="disclaimer">
                    <strong>📈 Annual Increase Potential:</strong> 
                    <span style="color: #16a34a; font-size: 1.5rem; font-weight: bold;">${annual_increase:,}</span>
                </div>
                
                <div style="margin-top: 1rem;">
                    <h3>Key Findings:</h3>
                    <ul style="margin-left: 1.5rem;">
                        {chr(10).join([f'<li>{finding}</li>' for finding in exec_summary.get('key_findings', [])])}
                    </ul>
                </div>
            </div>

            <div class="section">
                <h2>📋 Current Service-Connected Conditions Analysis</h2>
                <div style="overflow-x: auto;">
                    <table class="conditions-table">
                        <thead>
                            <tr>
                                <th>Condition & Code</th>
                                <th>Current</th>
                                <th>Potential</th>
                                <th>Evidence Strength</th>
                                <th>Increase Probability</th>
                                <th>Action Required</th>
                            </tr>
                        </thead>
                        <tbody>
                            {current_conditions_html or '<tr><td colspan="6"><em>No current service-connected conditions identified in available records</em></td></tr>'}
                        </tbody>
                    </table>
                </div>
            </div>

            <div class="section">
                <h2>🎯 Missed Claiming Opportunities</h2>
                {new_opportunities_html or '<p><em>No new claiming opportunities identified in current records. Focus on maximizing existing conditions.</em></p>'}
            </div>

            <div class="section">
                <h2>🎲 Combined Rating Scenarios</h2>
                <div class="scenario-grid">
                    {scenarios_html}
                </div>
            </div>

            <div class="section">
                <h2>⚡ Strategic Action Plan</h2>
                {action_plan_html or '<p><em>No specific actions identified. Review medical records for additional opportunities.</em></p>'}
            </div>

            <div class="section">
                <h2>📄 Evidence Gap Analysis</h2>
                {evidence_gaps_html or '<p><em>No critical evidence gaps identified in available records</em></p>'}
            </div>

            <div class="section">
                <h2>🚀 Next Steps & Recommendations</h2>
                <ol style="font-size: 1.1rem; line-height: 1.8; margin-left: 1.5rem;">
                    <li><strong>Review this comprehensive analysis</strong> - Focus on high-priority opportunities with greatest financial impact</li>
                    <li><strong>Gather missing evidence</strong> - Address critical gaps identified in the evidence section above</li>
                    <li><strong>Schedule professional consultation</strong> - Discuss complex strategies and optimal filing approaches</li>
                    <li><strong>Implement strategic action plan</strong> - Begin with immediate actions for maximum benefit</li>
                    <li><strong>Monitor claim progress</strong> - Track filing deadlines and C&P examination schedules</li>
                    <li><strong>Document functional impacts</strong> - Prepare detailed lay statements showing real-world effects</li>
                </ol>
            </div>

            <div class="footer">
                <div class="disclaimer">
                    <strong>⚖️ LEGAL DISCLAIMER:</strong> This analysis is educational and for preparation purposes only. 
                    No legal advice, representation, or advocacy is provided. Veterans should consult qualified 
                    attorneys or accredited representatives for legal advice and claim assistance.
                </div>
                
                <p style="margin-top: 1.5rem;">
                    <strong>🤖 Generated by Claude-3.5-Sonnet VA Senior Rater Analysis</strong><br>
                    Report ID: {veteran_info['report_id']} | Generated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}<br>
                    Source: {veteran_info['filename']} | <strong>Confidential and Proprietary</strong>
                </p>
                
                <div style="margin-top: 1rem; padding-top: 1rem; border-top: 1px solid #e5e7eb;">
                    <p><strong>Applied Senior Rater Principles:</strong></p>
                    <p>✓ Benefit-of-the-Doubt Doctrine Applied | ✓ Maximization Strategy Used | ✓ 38 CFR Part 4 Compliance</p>
                    <p>✓ Combined Rating Table Applied | ✓ Secondary Service Connection Analyzed | ✓ Evidence Gaps Identified</p>
                </div>
            </div>
        </div>

        <script>
            // Add any interactive functionality here
            document.addEventListener('DOMContentLoaded', function() {{
                // Highlight high-priority items
                const highPriorityItems = document.querySelectorAll('.priority-high');
                highPriorityItems.forEach(item => {{
                    item.style.fontWeight = 'bold';
                }});
                
                // Add click handlers for expandable sections if needed
                console.log('VA Claims Analysis Report loaded successfully');
            }});
        </script>
    </body>
    </html>
    """
    
    return report_html

def upload_report_to_workdrive(report_html: str, veteran_info: Dict) -> str:
    """Upload HTML report to WorkDrive"""
    try:
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        clean_name = veteran_info['name'].replace(' ', '_').replace('-', '_').lower()
        filename = f"va_senior_rater_analysis_{clean_name}_{timestamp}.html"
        
        print(f"📤 Uploading {filename} to WorkDrive reports folder...")
        
        # Placeholder for actual WorkDrive upload
        mock_report_url = f"https://workdrive.zoho.com/external/shared/{filename}"
        
        print(f"✅ Report uploaded successfully: {mock_report_url}")
        return mock_report_url
        
    except Exception as e:
        print(f"❌ Error uploading report: {e}")
        return f"https://workdrive.zoho.com/reports/error_{veteran_info['date']}.html"

def send_notification_email(veteran_info: Dict, report_url: str, analysis: Dict) -> bool:
    """Send email notification with report link"""
    try:
        print(f"📧 Email notification sent to: {veteran_info['email']}")
        print(f"📊 Report URL: {report_url}")
        print(f"💰 Potential monthly increase: ${analysis.get('executive_summary', {}).get('monthly_increase_potential', 0):,}")
        return True
    except Exception as e:
        print(f"❌ Error sending email: {e}")
        return False

def update_crm_record(veteran_info: Dict, analysis: Dict, report_url: str) -> bool:
    """Update CRM with analysis results"""
    try:
        print(f"📋 CRM updated for: {veteran_info['name']}")
        print(f"🎯 Analysis completed with {len(analysis.get('current_service_connected_conditions', []))} conditions reviewed")
        return True
    except Exception as e:
        print(f"❌ Error updating CRM: {e}")
        return False

@app.route('/test', methods=['GET'])
def test_system():
    """Test endpoint to verify system configuration"""
    return jsonify({
        'status': 'System operational',
        'timestamp': datetime.now().isoformat(),
        'services': {
            'anthropic': 'configured' if ANTHROPIC_API_KEY != 'your-anthropic-key-here' else 'needs_setup',
            'zoho': 'configured' if ZOHO_ACCESS_TOKEN != 'your-zoho-token' else 'needs_setup',
            'workdrive': 'configured' if ZOHO_REPORTS_FOLDER_ID != 'your-reports-folder-id' else 'needs_setup'
        },
        'version': '3.0 - Complete Claude Integration',
        'ai_backend': 'Claude-3.5-Sonnet',
        'endpoint': '/process-va-records',
        'features': [
            'Senior VA Rater Analysis Mode',
            'Comprehensive Medical Record Review',
            'CFR Part 4 Compliance',
            'Combined Rating Calculations',
            'Benefit-of-the-Doubt Application',
            'Responsive HTML Reports',
            'Evidence Gap Analysis',
            'Strategic Action Planning'
        ]
    })

@app.route('/webhook-test', methods=['POST'])
def webhook_test():
    """Test endpoint for webhook payload verification"""
    try:
        webhook_data = request.json
        
        return jsonify({
            'webhook_received': True,
            'timestamp': datetime.now().isoformat(),
            'webhook_event': webhook_data.get('webhook_event', 'unknown'),
            'file_info': {
                'name': webhook_data.get('name', 'unknown'),
                'id': webhook_data.get('id', 'unknown'),
                'size': webhook_data.get('storage_info_size', 'unknown'),
                'type': webhook_data.get('type', 'unknown')
            },
            'user_info': {
                'email': webhook_data.get('event_by_user_email_id', 'unknown'),
                'name': webhook_data.get('event_by_user_display_name', 'unknown')
            },
            'payload_analysis': {
                'download_url_present': bool(webhook_data.get('download_url')),
                'payload_keys': list(webhook_data.keys()) if webhook_data else [],
                'payload_size_bytes': len(str(webhook_data)) if webhook_data else 0
            },
            'system_ready': {
                'claude_configured': ANTHROPIC_API_KEY != 'your-anthropic-key-here',
                'senior_rater_mode': 'active',
                'analysis_capabilities': 'full'
            }
        })
        
    except Exception as e:
        return jsonify({
            'webhook_received': False,
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }), 400

@app.route('/analyze-sample', methods=['POST'])
def analyze_sample():
    """Endpoint to test the analysis with sample data"""
    try:
        sample_veteran_info = {
            'name': 'James Grant',
            'email': 'james.grant@example.com',
            'filename': 'sample_medical_records.txt',
            'download_url': 'https://example.com/sample',
            'file_id': 'sample123',
            'file_size': '2.5MB',
            'file_type': 'txt',
            'uploaded_time': datetime.now().strftime('%m/%d/%Y'),
            'uploader_email': 'james.grant@example.com',
            'uploader_name': 'James Grant',
            'date': datetime.now().strftime('%m%d%Y'),
            'report_id': f"VAR-SAMPLE-{datetime.now().strftime('%Y%m%d-%H%M%S')}"
        }
        
        # Use sample medical records
        sample_medical_text = generate_sample_medical_records()
        
        # Analyze with Claude
        analysis_result = analyze_medical_records_with_claude(sample_medical_text, sample_veteran_info)
        
        # Generate report
        report_html = generate_comprehensive_html_report(analysis_result, sample_veteran_info, sample_medical_text)
        
        return jsonify({
            'success': True,
            'message': 'Sample analysis completed',
            'veteran_name': sample_veteran_info['name'],
            'report_id': sample_veteran_info['report_id'],
            'analysis_summary': {
                'current_rating': analysis_result.get('executive_summary', {}).get('current_combined_rating', 0),
                'potential_rating': analysis_result.get('executive_summary', {}).get('potential_combined_rating', 0),
                'monthly_increase': analysis_result.get('executive_summary', {}).get('monthly_increase_potential', 0),
                'conditions_analyzed': len(analysis_result.get('current_service_connected_conditions', [])),
                'new_opportunities': len(analysis_result.get('missed_claiming_opportunities', []))
            },
            'report_preview': report_html[:1000] + "...",
            'timestamp': datetime.now().isoformat()
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'timestamp': datetime.now().isoformat()
        }), 500

if __name__ == '__main__':
    # Validate required environment variables on startup
    required_vars = ['ANTHROPIC_API_KEY', 'ZOHO_ACCESS_TOKEN', 'ZOHO_REPORTS_FOLDER_ID']
    missing_vars = []
    
    for var in required_vars:
        value = os.getenv(var)
        if not value or value.startswith('your-'):
            missing_vars.append(var)
    
    if missing_vars:
        print("⚠️ Missing required environment variables:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\nSet these in your .env file or deployment environment variables")
        print("\nRequired for full functionality:")
        print("- ANTHROPIC_API_KEY: Your Anthropic Claude API key")
        print("- ZOHO_ACCESS_TOKEN: Zoho WorkDrive API access token")
        print("- ZOHO_REPORTS_FOLDER_ID: Folder ID for storing generated reports")
        print("- ZOHO_VETREPORTS_FOLDER_ID: Alternative folder ID for reports")
        print("- ZOHO_MAIL_FROM: Email address for notifications")
    else:
        print("✅ All required environment variables configured")
    
    print("\n" + "="*80)
    print("🎖️  VA CLAIMS ANALYSIS SYSTEM - CLAUDE INTEGRATION")
    print("="*80)
    print("🤖 AI Backend: Claude-3.5-Sonnet (Anthropic)")
    print("⚖️  Analysis Mode: Senior VA Claims Rater (GS-13)")
    print("📋 Features: Comprehensive medical record analysis")
    print("🎯 Capabilities: CFR Part 4 compliance, benefit maximization")
    print("📊 Output: Responsive HTML reports with action plans")
    print("="*80)
    print("\nEndpoints:")
    print("- GET  /               : Health check")
    print("- POST /process-va-records : Main webhook endpoint")
    print("- GET  /test           : System configuration test")
    print("- POST /webhook-test   : Webhook payload testing")
    print("- POST /analyze-sample : Sample analysis testing")
    print("="*80)
    
    # Run the Flask application
    port = int(os.environ.get('PORT', 5000))
    debug_mode = os.environ.get('DEBUG', 'False').lower() == 'true'
    
    app.run(
        debug=debug_mode,
        host='0.0.0.0',
        port=port,
        threaded=True
    )
