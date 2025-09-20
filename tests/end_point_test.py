import requests

ENDPOINT = "http://localhost:8000"

def test_get_endpoint():    
    response = requests.get(ENDPOINT)
    print(response)
    assert response.status_code == 200
    assert response.json() == {"System":"Backend Sparta Challenge","Version":"1.0.0"}
