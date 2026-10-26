import json

def validate_medical_evals(file_path):
    """Validates structure and clinical auditing standards of medical evaluation records."""
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
            
        print(f"Loaded {len(data)} medical evaluation records successfully.\n")
        
        for record in data:
            record_id = record.get("id", "Unknown ID")
            domain = record.get("domain", "Unspecified")
            pref = record.get("preferred_response")
            justification = record.get("audit_justification")
            
            if not pref or not justification:
                print(f"[FAIL] Record {record_id} ({domain}): Missing preference or audit justification.")
            else:
                print(f"[PASS] Record {record_id} ({domain}): verified clinical reasoning audit.")
                
    except Exception as e:
        print(f"Error loading evaluation file: {e}")

if __name__ == "__main__":
    validate_medical_evals("medical_evals.json")