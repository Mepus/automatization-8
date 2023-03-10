import requests

class CompanyApi:

    def __init__(self, url):
        self.url = url

    
    def get_company_list(self, params_to_add = None):
        resp = requests.get(self.url+'/company', params=params_to_add)
        return resp.json()

    def get_token(self, user = 'michaelangelo', password = 'party-dude'):
        creds = {
            'username' : user, 
            'password' : password
        }

        resp = requests.post(self.url +'/auth/login', json=creds)
        return resp.json()["userToken"]
    

    def get_company(self, id):
        resp = requests.get(self.url+'/company'+ str(id))
        return resp.json

    def create_company(self, name, description=''):
        company = {
            "name": name,
            "description": description
        }

        my_headers = {}
        my_headers["x-clien-token"] = self.get_token()
        resp = requests.post(self.url +'/company', json=company, headers=my_headers)
        return resp.json

    def edit_company(self, new_id, new_name, new_descr):
        my_headers = {}
        my_headers["x-clien-token"] = self.get_token()

        company = {
            "name": new_name,
            "description": new_descr
        }
        resp = requests.patch(self.url+'/company'+ str(new_id), headers=my_headers, json=company)
        return resp.json()
    

    def delete_company(self, id):
        my_headers = {}
        my_headers["x-clien-token"] = self.get_token()
        resp = requests.get(self.url+'/company/delete/'+ str(id), headers=my_headers, headers = my_headers)
        return resp.json()
    
    def set_active_state(self, id, isActive):
       
        my_headers = {}
        my_headers["x-clien-token"] = self.get_token()
        resp = requests.get(self.url+'/company/delete/'+ str(id), headers=my_headers, json={'isActive'})
        
        return resp.json()