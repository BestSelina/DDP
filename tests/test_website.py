import json

class TestAccess:
    def test_login1(self, client): # login case 1: expected to login successfully
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'loginEmail': 'admin@123.com',
            'loginPassword': 'admin'
        }
        response = client.post("/login", headers=headers, data=json.dumps(data))
        # print(response) # output is <WrapperTestResponse streamed [200 OK]>
        # response_text = response.text # type is str
        # print(response.data) # type is json
        # print(json.loads(response.data)) # type is dict
        # assert response.status_code == 200, 'HTTP状态码异常'
        assert response.status_code == 200, 'HTTP status code for Exceptions'
        print(json.loads(response.data).get("info"))
        assert json.loads(response.data).get("status") == 'success', 'failed to login!'
    
    def test_login2(self, client):  # login case 2: expected to fail and print "password is wrong!"
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'loginEmail': 'admin@123.com',
            'loginPassword': 'ad'
        }
        response = client.post("/login", headers=headers, data=json.dumps(data))
        assert response.status_code == 200, 'HTTP status code for Exceptions'
        print(json.loads(response.data).get("info"))
        assert json.loads(response.data).get("status") == 'success', 'failed to login!'
    
    def test_login3(self, client):  # login case 3: expected to fail and print "email address doesn't exist!"
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'loginEmail': 'test_login@123.com',
            'loginPassword': 'test'
        }
        response = client.post("/login", headers=headers, data=json.dumps(data))
        assert response.status_code == 200, 'HTTP status code for Exceptions'
        print(json.loads(response.data).get("info"))
        assert json.loads(response.data).get("status") == 'success', 'failed to login!'
    
    def test_signup1(self, client): # signup case 1: expected to signup successfully"
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'regEmail': 'test_case@123.com',
            'regPassword': 'test'
        }
        response = client.post("/signup", headers=headers, data=json.dumps(data))
        assert response.status_code == 200, 'HTTP status code for Exceptions'
        print(json.loads(response.data).get("info"))
        assert json.loads(response.data).get("status") == 'success', 'failed to signup!'
    
    def test_signup2(self, client): # signup case 2: expected to fail and print "email address already exists!"
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'regEmail': 'admin@123.com',
            'regPassword': 'admin'
        }
        response = client.post("/signup", headers=headers, data=json.dumps(data))
        assert response.status_code == 200, 'HTTP status code for Exceptions'
        print(json.loads(response.data).get("info"))
        assert json.loads(response.data).get("status") == 'success', 'failed to signup!'
        
    def test_order1(self, client): # order case 1: expected to order successfully
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'quantity': '50',
        }
        response = client.post("/order", headers=headers, data=json.dumps(data))
        assert response.status_code == 200, 'HTTP status code for Exceptions'
        print(json.loads(response.data).get("info"))
        print(json.loads(response.data).get("order_id"))
        assert json.loads(response.data).get("status") == 'success', 'failed to order!'
        
    def test_order2(self, client): # order case 2: expected to fail and print "the quantity is over stock!"
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'quantity': '500',
        }
        response = client.post("/order", headers=headers, data=json.dumps(data))
        assert response.status_code == 200, 'HTTP status code for Exceptions'
        print(json.loads(response.data).get("info"))
        print(json.loads(response.data).get("order_id"))
        assert json.loads(response.data).get("status") == 'success', 'failed to order!'
    
    def test_search1(self, client): # search case: expected to search successfully
        headers = {
            'Content-Type': 'application/json'
        }
        data = {
            'searchInput': 'and',
        }
        response = client.post("/goose", headers=headers, data=json.dumps(data))
        assert response.status_code == 200, 'HTTP status code for Exceptions'
        print(json.loads(response.data))
    
    