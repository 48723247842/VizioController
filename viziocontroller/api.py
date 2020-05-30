import requests
import json
import warnings
from pprint import pprint

warnings.simplefilter( "ignore" )

class API:

	def __init__( self , options={} ):
		self.options = options

	def pairing_stage_1( self , ip_address ):
		headers = {
			"Content-Type": "application/json" ,
		}
		data = {
			"_url": "/pairing/start" ,
			"DEVICE_ID": "pyvizio" ,
			"DEVICE_NAME": "Python Vizio" ,
		}
		url = f"https://{ip_address}:7345/pairing/start"
		response = requests.put( url , headers=headers , data=json.dumps( data ) , verify=False )
		response.raise_for_status()

		# Should Return
		# {
		# 	'ITEM': {'CHALLENGE_TYPE': 1, 'PAIRING_REQ_TOKEN': 802927 } ,
		# 	'STATUS': {'DETAIL': 'Success', 'RESULT': 'SUCCESS'}
		# }
		result = json.loads( response.text )
		pprint( result )
		return result["ITEM"]["PAIRING_REQ_TOKEN"]

	def pairing_stage_2( self , ip_address , pairing_request_token , code_displayed_on_tv ):
		headers = {
			"Content-Type": "application/json" ,
		}
		data = {
			"_url": "/pairing/pair" ,
			"DEVICE_ID": "pyvizio" ,
			"DEVICE_NAME": "Python Vizio" ,
			"CHALLENGE_TYPE": 1 ,
			"PAIRING_REQ_TOKEN": pairing_request_token ,
			"RESPONSE_VALUE": str( code_displayed_on_tv )
		}
		print( data )
		url = f"https://{ip_address}:7345/pairing/pair"
		response = requests.put( url , headers=headers , data=json.dumps( data ) , verify=False )
		response.raise_for_status()

		# Should Return
		# {
		# 	'ITEM': {'AUTH_TOKEN': 'Zhehzvszfq' } ,
		# 	'STATUS': {'DETAIL': 'Success', 'RESULT': 'SUCCESS'}
		# }
		result = json.loads( response.text )
		pprint( result )
		return result["ITEM"]["AUTH_TOKEN"]

	def get_volume( self ):
		headers = {
			'AUTH': self.options["access_token"]
		}
		url = f"https://{self.options['ip']}:7345/menu_native/dynamic/tv_settings/audio/volume"
		response = requests.get( url , headers=headers , verify=False )
		response.raise_for_status()

		# Should Return
		# {'HASHLIST': [2308455925, 729988045],
		#  'ITEMS': [{'CNAME': 'volume',
		#             'ENABLED': 'FALSE',
		#             'HASHVAL': 1731828541,
		#             'NAME': 'Volume',
		#             'TYPE': 'T_VALUE_V1',
		#             'VALUE': 10}],
		#  'PARAMETERS': {'FLAT': 'TRUE', 'HASHONLY': 'FALSE', 'HELPTEXT': 'FALSE'},
		#  'STATUS': {'DETAIL': 'Success', 'RESULT': 'SUCCESS'},
		#  'URI': '/menu_native/dynamic/tv_settings/audio/volume'}

		result = json.loads( response.text )
		pprint( result )
		return result


if __name__ == "__main__":

	api = API()
