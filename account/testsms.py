#!/usr/bin/env python
#!/usr/bin/env python
from kavenegar import *
try:
    api = KavenegarAPI('78557A5558494338684C476C4A704B6F36794E756D51535A72484937674C4B684A4F4144733751635470453D', timeout=2)
    params = {
        'receptor': '09921221107',
        'template': 'login',
        'token': '1234',
        'type': 'sms',#sms vs call
    }   
    response = api.verify_lookup(params)
    print(response)
except APIException as e: 
  print(e)
except HTTPException as e: 
  print(e)