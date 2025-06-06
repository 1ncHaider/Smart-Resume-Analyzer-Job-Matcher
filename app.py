from flask import Flask, request, jsonify, render_template
from resume_parser import parse_resume
from job_parser import parse_job_description
from matcher import match_resumes_to_jobs

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload_resume', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({'error': 'No resume file uploaded'}), 400
    
    resume_file = request.files['resume']
    resume_data = parse_resume(resume_file)
    
    return jsonify({'resume_data': resume_data})

@app.route('/upload_job', methods=['POST'])
def upload_job():
    if 'job' not in request.files:
        return jsonify({'error': 'No job description file uploaded'}), 400
    
    job_file = request.files['job']
    job_data = parse_job_description(job_file)
    
    return jsonify({'job_data': job_data})

@app.route('/match', methods=['POST'])
def match():
    resume_data = request.json.get('resume_data')
    job_data = request.json.get('job_data')
    
    if not resume_data or not job_data:
        return jsonify({'error': 'Resume data or job data missing'}), 400
    
    matches = match_resumes_to_jobs([resume_data], [job_data])
    
    return jsonify({'matches': matches})

if __name__ == '__main__':
    app.run(debug=True)
