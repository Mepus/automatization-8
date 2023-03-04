import requests
from CompanyApi import CompanyApi


api = CompanyApi("https://x-clients-be.onrender.com")

def test_get_companies():
    body = api.get_company_list()
    assert len(body) > 1 

def test_get_active_companies():
    # 1. Получить список всех компаний
    full_list = api.get_company_list()

    # 2. Получить список активных компаний
    filtered_list = api.get_company_list(params_to_add={'active' : 'true'})


    # 3. Проверить, что список 1 > списка 2
    assert len(full_list) > len(filtered_list)



def test_add_new_company():

    body = api.get_company_list()
    len_before = len(body)

    name = "Autotest"
    descr = "Descr"
    result = api.create_company(name = name, description=descr)
    new_id = result["id"]
    body = api.get_company_list()
    len_after = len(body)

    assert len_after - len_before == 1
    assert body[-1]["name" == name]
    assert body[-1]["description" == descr]
    assert body[-1]["id"] == new_id
   
def test_get_one_company():
    name = 'VS Code'
    descr = 'IDE'
    result = api.create_company(name, descr)
    new_id = result["id"]

    new_company = api.get_company(new_id)

    assert new_company["id"] == new_id
    assert new_company["name"] == name
    assert new_company["description"] == descr
    assert new_company["isActive"] == True

def test_edit_company():
    name = 'Company to be edited'
    descr = 'Edit me'
    result = api.create_company(name, descr)
    new_id = result["id"]

    new_name = "UPDATED"
    new_descr = "__upd__"
    edited = api.edit(new_id, new_name, new_descr)
    assert edited ["id"] == new_id
    assert edited ["name"] == new_name
    assert edited ["description"] == new_descr
    assert edited ["isActive"] == True

def test_delete_company():
    name = 'Company to be deleted'
    descr = 'Edit me'
    result = api.create_company(name, descr)
    new_id = result["id"]

    edited = api.delete(new_id)
    assert edited ["id"] == new_id
    assert edited ["name"] == name
    assert edited ["description"] == ''
    assert edited ["isActive"] == True

    body = api.get_company_list()
    assert body [-1]["id"] != new_id


def test_deactivate_company():

    name = "Company to be deactivated"
    result = api.create_company(name = name, description=descr)
    new_id = result["id"]
    
    body = api.deactivate(new_id, False)
    assert body["isActive"] == False

def test_deactivate_and_activate_back():

    name = "Company to be deactivated"
    result = api.create_company(name = name, description=descr)
    new_id = result["id"]
    
    api.set_active_state(new_id, False)
    body = api.deactivate(new_id, True)
    assert body["isActive"] == True
