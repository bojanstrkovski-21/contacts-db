from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
import toml
import os
from datetime import datetime
import io

app = Flask(__name__, static_folder='static')
CORS(app)

# Data directory for TOML files
DATA_DIR = './data'
INDIVIDUALS_FILE = os.path.join(DATA_DIR, 'individuals.toml')
COMPANIES_FILE = os.path.join(DATA_DIR, 'companies.toml')

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

def load_toml(filepath):
    """Load data from TOML file"""
    if os.path.exists(filepath):
        try:
            return toml.load(filepath)
        except Exception as e:
            print(f"Error loading {filepath}: {e}")
            return {}
    return {}

def save_toml(filepath, data):
    """Save data to TOML file"""
    try:
        with open(filepath, 'w') as f:
            toml.dump(data, f)
        return True
    except Exception as e:
        print(f"Error saving {filepath}: {e}")
        return False

def get_next_id(data):
    """Get next available ID"""
    if not data:
        return 1
    return max([int(k.replace('contact_', '')) for k in data.keys()]) + 1

# Routes
@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/api/individuals', methods=['GET'])
def get_individuals():
    """Get all individuals"""
    data = load_toml(INDIVIDUALS_FILE)
    # Convert dict to list for frontend
    contacts = []
    for key, value in data.items():
        contact = value.copy()
        contact['id'] = key
        contacts.append(contact)
    return jsonify(contacts)

@app.route('/api/individuals', methods=['POST'])
def add_individual():
    """Add new individual"""
    data = load_toml(INDIVIDUALS_FILE)
    contact_data = request.json
    
    # Generate ID
    next_id = get_next_id(data)
    contact_key = f"contact_{next_id}"
    
    # Add timestamp
    contact_data['created_at'] = datetime.now().isoformat()
    contact_data['updated_at'] = datetime.now().isoformat()
    
    # Save
    data[contact_key] = contact_data
    if save_toml(INDIVIDUALS_FILE, data):
        contact_data['id'] = contact_key
        return jsonify(contact_data), 201
    return jsonify({'error': 'Failed to save'}), 500

@app.route('/api/individuals/<contact_id>', methods=['PUT'])
def update_individual(contact_id):
    """Update individual"""
    data = load_toml(INDIVIDUALS_FILE)
    
    if contact_id not in data:
        return jsonify({'error': 'Contact not found'}), 404
    
    contact_data = request.json
    contact_data['updated_at'] = datetime.now().isoformat()
    
    # Preserve created_at
    if 'created_at' in data[contact_id]:
        contact_data['created_at'] = data[contact_id]['created_at']
    
    data[contact_id] = contact_data
    if save_toml(INDIVIDUALS_FILE, data):
        contact_data['id'] = contact_id
        return jsonify(contact_data)
    return jsonify({'error': 'Failed to save'}), 500

@app.route('/api/individuals/<contact_id>', methods=['DELETE'])
def delete_individual(contact_id):
    """Delete individual"""
    data = load_toml(INDIVIDUALS_FILE)
    
    if contact_id not in data:
        return jsonify({'error': 'Contact not found'}), 404
    
    del data[contact_id]
    if save_toml(INDIVIDUALS_FILE, data):
        return jsonify({'message': 'Deleted successfully'})
    return jsonify({'error': 'Failed to delete'}), 500

@app.route('/api/companies', methods=['GET'])
def get_companies():
    """Get all companies"""
    data = load_toml(COMPANIES_FILE)
    contacts = []
    for key, value in data.items():
        contact = value.copy()
        contact['id'] = key
        contacts.append(contact)
    return jsonify(contacts)

@app.route('/api/companies', methods=['POST'])
def add_company():
    """Add new company"""
    data = load_toml(COMPANIES_FILE)
    contact_data = request.json
    
    next_id = get_next_id(data)
    contact_key = f"contact_{next_id}"
    
    contact_data['created_at'] = datetime.now().isoformat()
    contact_data['updated_at'] = datetime.now().isoformat()
    
    data[contact_key] = contact_data
    if save_toml(COMPANIES_FILE, data):
        contact_data['id'] = contact_key
        return jsonify(contact_data), 201
    return jsonify({'error': 'Failed to save'}), 500

@app.route('/api/companies/<contact_id>', methods=['PUT'])
def update_company(contact_id):
    """Update company"""
    data = load_toml(COMPANIES_FILE)
    
    if contact_id not in data:
        return jsonify({'error': 'Contact not found'}), 404
    
    contact_data = request.json
    contact_data['updated_at'] = datetime.now().isoformat()
    
    if 'created_at' in data[contact_id]:
        contact_data['created_at'] = data[contact_id]['created_at']
    
    data[contact_id] = contact_data
    if save_toml(COMPANIES_FILE, data):
        contact_data['id'] = contact_id
        return jsonify(contact_data)
    return jsonify({'error': 'Failed to save'}), 500

@app.route('/api/companies/<contact_id>', methods=['DELETE'])
def delete_company(contact_id):
    """Delete company"""
    data = load_toml(COMPANIES_FILE)
    
    if contact_id not in data:
        return jsonify({'error': 'Contact not found'}), 404
    
    del data[contact_id]
    if save_toml(COMPANIES_FILE, data):
        return jsonify({'message': 'Deleted successfully'})
    return jsonify({'error': 'Failed to delete'}), 500

@app.route('/api/export/individuals/toml', methods=['GET'])
def export_individuals_toml():
    """Export individuals as TOML"""
    data = load_toml(INDIVIDUALS_FILE)
    toml_str = toml.dumps(data)
    
    return app.response_class(
        response=toml_str,
        status=200,
        mimetype='text/plain',
        headers={'Content-Disposition': f'attachment; filename=individuals_{datetime.now().strftime("%Y%m%d")}.toml'}
    )

@app.route('/api/export/companies/toml', methods=['GET'])
def export_companies_toml():
    """Export companies as TOML"""
    data = load_toml(COMPANIES_FILE)
    toml_str = toml.dumps(data)
    
    return app.response_class(
        response=toml_str,
        status=200,
        mimetype='text/plain',
        headers={'Content-Disposition': f'attachment; filename=companies_{datetime.now().strftime("%Y%m%d")}.toml'}
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
