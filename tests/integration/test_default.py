def test_index_return_200(client):
    response = client.get('/')
    assert response.status_code == 200
    assert response.data == b'The server is runing!'


def test_inexistent_url_returning_404(client):
    response = client.get('/some-invalid-request')
    assert response.status_code == 404
    assert response.json['status'] == 'error'
    assert response.json['message'] == 'not Found'


def test_protected_url_returning_200_with_valid_jwt_token(client, auth):
    response = client.get('/account', headers=auth['access_token'])
    assert response.status_code == 200


def test_protected_url_returning_422_with_invalid_jwt_token(client):
    response = client.get('/account', headers={'Authorization': 'Bearer x123x'})
    assert response.status_code == 422
    assert response.json['msg'] == 'Not enough segments'


def test_protected_url_returning_401_if_no_jwt_token(client):
    response = client.get('/account')
    assert response.status_code == 401
    assert response.json['msg'] == 'Missing Authorization Header'
