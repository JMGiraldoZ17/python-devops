from main import app

def test_health_endpoint():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json == {"status": "ok"}

def test_hello_endpoint():
    client = app.test_client()
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json == {"message": "Hello from DevOps API"}
