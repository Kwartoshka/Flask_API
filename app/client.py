import requests

#
resp = requests.get('http://127.0.0.1:5001/health/')
print(resp)
# #
#
# resp = requests.get('http://127.0.0.1:5000/users/1').json()
# print(resp)

#
# resp = requests.post('http://127.0.0.1:5000/users/',
#                      json={
#                          'password': 'sgdsppo34FET32325',
#                          'email': 'tedsadsawwdewrsadsadsast@assa.test'
#                      })
# # print(resp)
#
# resp = requests.put('http://127.0.0.1:5000/advertisements/5',
#                      json={
#                          'title': 'mom',
#                          'owner_id': 1
#                      }).json()
# print(resp)
#
# # resp = requests.get('http://127.0.0.1:5000/advertisements/1',
# #                      ).json()
# # print(resp)

