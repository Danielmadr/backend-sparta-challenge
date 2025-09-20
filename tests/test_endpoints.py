import requests
import time

ENDPOINT = "http://localhost:8000"


def test_get_endpoint():
    response = requests.get(ENDPOINT)
    assert response.status_code == 200
    assert response.json() == {"System": "Backend Sparta Challenge", "Version": "1.0.0"}

def test_post_endpoint_large_data():
    with open('data/large_test_data.json', 'r') as f:
        large_payload = f.read()

    inicio = time.time()
    response = requests.post(f"{ENDPOINT}/calcular-taxa-administrativa-por-cotista", data=large_payload, headers={"Content-Type": "application/json"})
    fim = time.time()
    print(f"Tempo de resposta: {fim - inicio} segundos")

    assert response.status_code == 200
    assert len(response.json()) == 40000  #should return exactly 40000 values, one for each shareholder

def test_post_endpoint_large_data_brute_force():
    with open('data/large_test_data.json', 'r') as f:
        large_payload = f.read()

    inicio = time.time()
    response = requests.post(f"{ENDPOINT}/calcular-taxa-administrativa-por-cotista-brute-force", data=large_payload, headers={"Content-Type": "application/json"})
    fim = time.time()
    print(f"Tempo de resposta força bruta: {fim - inicio} segundos")

    assert response.status_code == 200
    assert len(response.json()) == 40000  # should return exactly 40000 values, one for each shareholder