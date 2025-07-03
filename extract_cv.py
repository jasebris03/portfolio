#!/usr/bin/env python3
"""
Script to extract CV information and GitHub repositories for portfolio website.
"""

import json
import requests
from docx import Document
import re
from typing import Dict, List, Any

def extract_cv_info(cv_path: str) -> Dict[str, Any]:
    """Extract information from the CV document."""
    doc = Document(cv_path)
    
    # Extract all text from the document
    full_text = []
    for paragraph in doc.paragraphs:
        if paragraph.text.strip():
            full_text.append(paragraph.text.strip())
    
    # Join all text
    cv_text = '\n'.join(full_text)
    
    # Extract basic information using regex patterns
    info = {
        'name': '',
        'title': '',
        'summary': '',
        'experience': [],
        'skills': [],
        'education': [],
        'contact': {}
    }
    
    # Extract name (usually at the top)
    lines = cv_text.split('\n')
    if lines:
        info['name'] = lines[0].strip()
    
    # Extract title (usually second line or after name)
    if len(lines) > 1:
        info['title'] = lines[1].strip()
    
    # Extract summary (look for summary section)
    summary_match = re.search(r'summary[:\s]*(.*?)(?=\n\n|\n[A-Z]|$)', cv_text, re.IGNORECASE | re.DOTALL)
    if summary_match:
        info['summary'] = summary_match.group(1).strip()
    
    # Extract skills (look for skills section)
    skills_match = re.search(r'skills[:\s]*(.*?)(?=\n\n|\n[A-Z]|$)', cv_text, re.IGNORECASE | re.DOTALL)
    if skills_match:
        skills_text = skills_match.group(1)
        # Split by common delimiters
        skills = re.split(r'[,•·\n]+', skills_text)
        info['skills'] = [skill.strip() for skill in skills if skill.strip()]
    
    # Extract experience (look for experience section)
    experience_match = re.search(r'experience[:\s]*(.*?)(?=\n\n|\n[A-Z]|$)', cv_text, re.IGNORECASE | re.DOTALL)
    if experience_match:
        experience_text = experience_match.group(1)
        # Split into individual experiences
        experiences = re.split(r'\n(?=[A-Z][a-z]+\s+\d{4})', experience_text)
        for exp in experiences:
            if exp.strip():
                info['experience'].append(exp.strip())
    
    # Extract education (look for education section)
    education_match = re.search(r'education[:\s]*(.*?)(?=\n\n|\n[A-Z]|$)', cv_text, re.IGNORECASE | re.DOTALL)
    if education_match:
        education_text = education_match.group(1)
        # Split into individual education entries
        educations = re.split(r'\n(?=[A-Z][a-z]+\s+\d{4})', education_text)
        for edu in educations:
            if edu.strip():
                info['education'].append(edu.strip())
    
    return info

def fetch_github_repos(username: str) -> List[Dict[str, Any]]:
    """Fetch public repositories from GitHub API."""
    try:
        url = f"https://api.github.com/users/{username}/repos"
        response = requests.get(url)
        response.raise_for_status()
        
        repos = response.json()
        # Filter and format repository information
        formatted_repos = []
        for repo in repos:
            if not repo['fork']:  # Only include original repos, not forks
                formatted_repos.append({
                    'name': repo['name'],
                    'description': repo['description'] or 'No description available',
                    'url': repo['html_url'],
                    'language': repo['language'],
                    'stars': repo['stargazers_count'],
                    'forks': repo['forks_count'],
                    'updated_at': repo['updated_at']
                })
        
        # Sort by stars and then by update date
        formatted_repos.sort(key=lambda x: (x['stars'], x['updated_at']), reverse=True)
        return formatted_repos[:10]  # Return top 10 repos
        
    except requests.RequestException as e:
        print(f"Error fetching GitHub repos: {e}")
        return []

def main():
    """Main function to extract CV info and fetch GitHub repos."""
    # Extract CV information
    cv_path = "CVs/JM Platform Engineer Resume 20250618.docx"
    cv_info = extract_cv_info(cv_path)
    
    # Fetch GitHub repositories
    github_username = "jasebris03"
    repos = fetch_github_repos(github_username)
    
    # Combine all information
    portfolio_data = {
        'personal_info': cv_info,
        'github_repos': repos,
        'social_links': {
            'linkedin': 'https://www.linkedin.com/in/jasonmerefield',
            'github': f'https://github.com/{github_username}'
        }
    }
    
    # Save to JSON file
    with open('portfolio_data.json', 'w', encoding='utf-8') as f:
        json.dump(portfolio_data, f, indent=2, ensure_ascii=False)
    
    print("Portfolio data extracted successfully!")
    print(f"Name: {cv_info.get('name', 'Not found')}")
    print(f"Title: {cv_info.get('title', 'Not found')}")
    print(f"Skills found: {len(cv_info.get('skills', []))}")
    print(f"Experience entries: {len(cv_info.get('experience', []))}")
    print(f"GitHub repos found: {len(repos)}")

if __name__ == "__main__":
    main() 