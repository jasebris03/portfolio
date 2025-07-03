#!/usr/bin/env python3
"""
Detailed script to extract comprehensive information from the CV document.
"""

import json
from docx import Document
import re
from typing import Dict, List, Any

def extract_detailed_cv_info(cv_path: str) -> Dict[str, Any]:
    """Extract detailed information from the CV document."""
    doc = Document(cv_path)
    
    # Extract all text with more structure
    full_text = []
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            full_text.append(paragraph.text.strip())
    
    # Join all text
    cv_text = '\n'.join(full_text)
    print("Full CV text:")
    print(cv_text)
    print("\n" + "="*50 + "\n")
    
    # Initialize info structure
    info = {
        'name': '',
        'title': '',
        'summary': '',
        'experience': [],
        'skills': [],
        'education': [],
        'contact': {},
        'certifications': [],
        'languages': []
    }
    
    # Split into lines for better parsing
    lines = [line.strip() for line in cv_text.split('\n') if line.strip()]
    
    # Extract name (usually first line)
    if lines:
        info['name'] = lines[0]
        print(f"Name: {info['name']}")
    
    # Extract title (usually second line or after name)
    if len(lines) > 1:
        # Look for title in first few lines
        for i in range(1, min(5, len(lines))):
            line = lines[i]
            if any(keyword in line.lower() for keyword in ['engineer', 'developer', 'architect', 'specialist', 'consultant', 'manager']):
                info['title'] = line
                print(f"Title: {info['title']}")
                break
    
    # Extract contact information
    contact_patterns = [
        r'(\w+@\w+\.\w+)',  # Email
        r'(\+?\d{1,3}[-.\s]?\d{3}[-.\s]?\d{3}[-.\s]?\d{4})',  # Phone
        r'(linkedin\.com/in/\w+)',  # LinkedIn
        r'(github\.com/\w+)'  # GitHub
    ]
    
    for pattern in contact_patterns:
        matches = re.findall(pattern, cv_text, re.IGNORECASE)
        for match in matches:
            if '@' in match:
                info['contact']['email'] = match
            elif 'linkedin' in match:
                info['contact']['linkedin'] = f"https://www.{match}"
            elif 'github' in match:
                info['contact']['github'] = f"https://www.{match}"
            elif any(char.isdigit() for char in match):
                info['contact']['phone'] = match
    
    # Extract summary
    summary_keywords = ['summary', 'profile', 'objective', 'about']
    for keyword in summary_keywords:
        pattern = rf'{keyword}[:\s]*(.*?)(?=\n\n|\n[A-Z][A-Z\s]+:|$)'
        match = re.search(pattern, cv_text, re.IGNORECASE | re.DOTALL)
        if match:
            summary = match.group(1).strip()
            if len(summary) > 20:  # Only use if it's substantial
                info['summary'] = summary
                print(f"Summary found: {summary[:100]}...")
                break
    
    # Extract skills more comprehensively
    skills_sections = ['skills', 'technical skills', 'technologies', 'tools', 'languages']
    for section in skills_sections:
        pattern = rf'{section}[:\s]*(.*?)(?=\n\n|\n[A-Z][A-Z\s]+:|$)'
        match = re.search(pattern, cv_text, re.IGNORECASE | re.DOTALL)
        if match:
            skills_text = match.group(1)
            # Split by various delimiters
            skills = re.split(r'[,•·\n;]+', skills_text)
            skills = [skill.strip() for skill in skills if skill.strip() and len(skill.strip()) > 1]
            if skills:
                info['skills'].extend(skills)
                print(f"Skills found in {section}: {skills}")
    
    # Extract experience
    experience_patterns = [
        r'experience[:\s]*(.*?)(?=\n\n|\n[A-Z][A-Z\s]+:|$)',
        r'work history[:\s]*(.*?)(?=\n\n|\n[A-Z][A-Z\s]+:|$)',
        r'employment[:\s]*(.*?)(?=\n\n|\n[A-Z][A-Z\s]+:|$)'
    ]
    
    for pattern in experience_patterns:
        match = re.search(pattern, cv_text, re.IGNORECASE | re.DOTALL)
        if match:
            experience_text = match.group(1)
            # Split into individual experiences
            experiences = re.split(r'\n(?=[A-Z][a-z]+\s+\d{4}|\d{4}-\d{4}|\d{4}\s*-\s*present)', experience_text)
            for exp in experiences:
                if exp.strip() and len(exp.strip()) > 20:
                    info['experience'].append(exp.strip())
                    print(f"Experience: {exp.strip()[:100]}...")
    
    # Extract education
    education_patterns = [
        r'education[:\s]*(.*?)(?=\n\n|\n[A-Z][A-Z\s]+:|$)',
        r'academic[:\s]*(.*?)(?=\n\n|\n[A-Z][A-Z\s]+:|$)'
    ]
    
    for pattern in education_patterns:
        match = re.search(pattern, cv_text, re.IGNORECASE | re.DOTALL)
        if match:
            education_text = match.group(1)
            educations = re.split(r'\n(?=[A-Z][a-z]+\s+\d{4}|\d{4}-\d{4})', education_text)
            for edu in educations:
                if edu.strip() and len(edu.strip()) > 10:
                    info['education'].append(edu.strip())
                    print(f"Education: {edu.strip()[:100]}...")
    
    # Extract certifications
    cert_patterns = [
        r'certifications[:\s]*(.*?)(?=\n\n|\n[A-Z][A-Z\s]+:|$)',
        r'certificates[:\s]*(.*?)(?=\n\n|\n[A-Z][A-Z\s]+:|$)'
    ]
    
    for pattern in cert_patterns:
        match = re.search(pattern, cv_text, re.IGNORECASE | re.DOTALL)
        if match:
            cert_text = match.group(1)
            certs = re.split(r'[,•·\n]+', cert_text)
            certs = [cert.strip() for cert in certs if cert.strip()]
            info['certifications'].extend(certs)
            print(f"Certifications: {certs}")
    
    return info

def main():
    """Main function to extract detailed CV info."""
    cv_path = "CVs/JM Platform Engineer Resume 20250618.docx"
    
    try:
        cv_info = extract_detailed_cv_info(cv_path)
        
        # Create comprehensive portfolio data
        portfolio_data = {
            'personal_info': cv_info,
            'social_links': {
                'linkedin': 'https://www.linkedin.com/in/jasonmerefield',
                'github': 'https://github.com/jasebris03'
            }
        }
        
        # Save to JSON file
        with open('portfolio_data.json', 'w', encoding='utf-8') as f:
            json.dump(portfolio_data, f, indent=2, ensure_ascii=False)
        
        print("\n" + "="*50)
        print("EXTRACTION SUMMARY:")
        print("="*50)
        print(f"Name: {cv_info.get('name', 'Not found')}")
        print(f"Title: {cv_info.get('title', 'Not found')}")
        print(f"Summary length: {len(cv_info.get('summary', ''))} characters")
        print(f"Skills found: {len(cv_info.get('skills', []))}")
        print(f"Experience entries: {len(cv_info.get('experience', []))}")
        print(f"Education entries: {len(cv_info.get('education', []))}")
        print(f"Certifications: {len(cv_info.get('certifications', []))}")
        print(f"Contact info: {cv_info.get('contact', {})}")
        
        print("\nPortfolio data saved to portfolio_data.json")
        
    except Exception as e:
        print(f"Error extracting CV info: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main() 