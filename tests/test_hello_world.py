
def test_get_hello_page(client):
    response = client.get("/")
    # check if a 200 status code is returned
    assert response.status_code == 200

