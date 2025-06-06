"""
CLI Module
This module contains the command-line interface for the Smart Resume Analyzer & Job Matcher.
"""

import argparse
from resume_parser import parse_resume
from job_parser import parse_job_description
from matcher import match_resumes_to_jobs

def main():
    """
    Main function to run the CLI.
    """
    parser = argparse.ArgumentParser(description='Smart Resume Analyzer & Job Matcher')
    parser.add_argument('--resume', type=str, required=True, help='Path to the resume file')
    parser.add_argument('--job', type=str, required=True, help='Path to the job description file')
    
    args = parser.parse_args()
    
    resume_data = parse_resume(args.resume)
    job_data = parse_job_description(args.job)
    
    matches = match_resumes_to_jobs([resume_data], [job_data])
    
    print(matches)

if __name__ == '__main__':
    main()
