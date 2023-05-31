import pytest
from api import CreateToken
from pydantic import ValidationError
from serializers import AuthRequest


ct = CreateToken()

@pytest.mark.auth
@pytest.mark.parametrize('username, password, headers', [
    ('admin', 'password123', {'Content-Type': 'application/json'}),
    ('admin', 'password123', {'Content-Type': ''}),
    ('admin', 'password123', {}),
    ('', '', {'Content-Type: application/json'}),
])

def test_create_token(username, password, headers):

    try:
        data = AuthRequest(username=username, password=password)
    except ValidationError as e:
        if username == '' and password == '':
            assert str(e) == "1 Validation error for AuthRequestModel\nusername\n " \
                             "field required (type=value_error.missing)\npassword\n " \
                             "field required (type=value_error.missing"
    else:
        pytest.fail(f"Failed to validate request data: {e}")

    response = ct.create_auth_token()
    assert response.status_code == 200

    assert status == 200

    if "reason" in response.json() and response.json()['reason'] == "Bad credentials":
        assert 'token' not in response.json()
    else:
        assert 'token' in response.json()


