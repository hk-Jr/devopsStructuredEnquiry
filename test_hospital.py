from hospital import get_patient_summary

def test_existing_patient():
    result = get_patient_summary("P1")
    assert "Amit Sharma" in result
    assert "Flu" in result

def test_non_existing_patient():
    result = get_patient_summary("P99")
    assert result == "Patient not found"
