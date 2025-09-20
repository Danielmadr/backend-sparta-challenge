import requests

ENDPOINT = "http://localhost:8000"


def test_get_endpoint():
    response = requests.get(ENDPOINT)
    print(response)
    assert response.status_code == 200
    assert response.json() == {"System": "Backend Sparta Challenge", "Version": "1.0.0"}


def test_post_endpoint():
    payload = {
        "taxa": 0.02,
        "cotas": [
            {"valor": 100.0, "quantidades": [10, 50, 25]},
            {"valor": 102.5, "quantidades": [10, 40, 30]},
            {"valor": 101.0, "quantidades": [0, 40, 30]},
        ],
    }
    EXPECTED_OUTPUT = {0.1607142857142857, 1.0428571428571427, 0.682936507936508}

    response = requests.post(f"{ENDPOINT}/calcular-taxa-administrativa-por-cotista", json=payload)
    print(response)
    assert response.status_code == 200
    assert set(response.json()) == EXPECTED_OUTPUT, f"Expected {EXPECTED_OUTPUT}, but got {response.json()}"

def test_post_endpoint_large_data():
    with open('data/large_test_data.json', 'r') as f:
        large_payload = f.read()

    response = requests.post(f"{ENDPOINT}/calcular-taxa-administrativa-por-cotista", data=large_payload, headers={"Content-Type": "application/json"})
    print(response)
    assert response.status_code == 200
    assert len(response.json()) == 10  # Deve retornar exatamente 10 valores, um para cada cotista
