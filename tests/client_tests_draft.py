import requests


def test_post(my_shipment_id, my_compendium_id, my_recipient, my_cookie):
    # curl -i -d '{'_id': null, 'compendium_id': $ID, 'recipient': 'eudat, 'action': 'c', 'cookie': $COOKIE'} -x POST http://localhost:8087/api/v1/shipment
    new_data = {'_id': my_shipment_id, 'compendium_id': str(my_compendium_id), 'recipient': str(my_recipient), 'action': 'c', 'cookie': str(my_cookie)}
    r = requests.post(''.join((host, 'shipment')), data=new_data)
    print(r.status_code)
    print(r.text)


def test_post_update(my_depot, my_compendium_id, my_recipient, my_cookie):
    # test md for zenodo only
    test_md = {'metadata': {
        "creators": [{
            "name": "Tester, Ted",
            "affiliation": "Univ"
        }],
        "publication_date": "2017-02-05",
        "description": "Some words about it.",
        "title": "Just a test title",
        "upload_type": "publication",
        "publication_type": "other",
        "access_right": "open",
        "license": "cc-by"}}
    new_data = {'deposition_id': my_depot, 'compendium_id': str(my_compendium_id), 'recipient': str(my_recipient), 'action': 'u', 'md': str(test_md), 'cookie': str(my_cookie)}
    r = requests.post(''.join((host, 'shipment')), data=new_data)
    print(r.status_code)
    print(r.text)


def test_return_filelist(my_depot, my_shipment_id, my_compendium_id, my_recipient, my_cookie):
    new_data = {'deposition_id': my_depot, '_id': my_shipment_id, 'compendium_id': str(my_compendium_id), 'action': 'r', 'recipient': str(my_recipient), 'cookie': str(my_cookie)}
    r = requests.post(''.join((host, 'shipment')), data=new_data)
    print(r.status_code)
    print(r.text)

def test_del(my_depot, my_shipment_id, my_compendium_id, my_recipient, my_cookie):
    new_data = {'deposition_id': my_depot, '_id': my_shipment_id, 'compendium_id': str(my_compendium_id), 'action': 'd', 'recipient': str(my_recipient), 'file_id': 'c9d47625-2f4a-45b9-93c3-832a1dc54f3f', 'cookie': str(my_cookie)}
    r = requests.post(''.join((host, 'shipment')), data=new_data)
    print(r.status_code)
    print(r.text)


def test_del_whole_depot(my_depot, my_shipment_id, my_recipient, my_cookie):
    new_data = {'deposition_id': my_depot, '_id': my_shipment_id, 'action': 'delete', 'recipient': str(my_recipient), 'cookie': str(my_cookie)}
    r = requests.post(''.join((host, 'shipment')), data=new_data)
    print(r.status_code)
    print(r.text)


def test_get(my_id):
    if not my_id:
        # list all
        r = requests.get(''.join((host, 'shipment')))
    else:
        # output specific
        r = requests.get(''.join((host, 'shipment/', my_id)))
    print(r.status_code)
    print(r.text)


# main:
print('client test for o2r shipper service')

host = 'http://localhost:8087/api/v1/'
userlevel = 200  # set user level >= 200 here
the_cookie = ''  # enter your cookie here

try:
    # Shipment create new
    test_post(None, '4XgD9', 'eudat', the_cookie)

    # Shipment update metadata only
    #test_post_update('12345', '4XgD9', 'zenodo', the_cookie)

    # Shipment list all files from specific depot
    #test_return_filelist('12345', None, '4XgD9', 'zenodo', the_cookie)

    #  Shipment delete whole depot
    #test_del_whole_depot('12345', None, 'zenodo', the_cookie)

    #  Shipment delete file from specific depot
    #test_del('12345', None, '4XgD9', 'zenodo', the_cookie)

    # Shipment list them all
    #test_get(None)

    # Shipment info retrieval based on id
    #test_get('49b878c6-301f-4b98-9f47-e9bef1b8f3b7')
except:
    raise
