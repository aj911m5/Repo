import json
import requests
import datetime

accessKey='XXX'
templateName='tt.doc'

if accessKey=='XXX':
  print("Please set your access key")
  exit()

files = {'templateFile': open(templateName, 'rb')}
fields = {"accessKey":accessKey, "templateName":templateName }

req = requests.post('https://dws2.docmosis.com/services/rs/uploadTemplate', data=fields, stream=True, files=files)
print (req.text)
