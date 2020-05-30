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
		#pprint( result )
		return result["ITEMS"][0]["VALUE"]

	def volume_down( self ):
		headers = {
			"Content-Type": "application/json" ,
			"AUTH": self.options["access_token"]
		}
		data = {
			"_url": "/key_command/" ,
			"KEYLIST": [{
				"CODESET": 5 ,
				"CODE": 0 ,
				"ACTION": "KEYPRESS"
			}]
		}
		url = f"https://{self.options['ip']}:7345/key_command/"
		response = requests.put( url , headers=headers , data=json.dumps( data ) , verify=False )
		response.raise_for_status()

		# Should Return
		# {"STATUS": {"RESULT": "SUCCESS", "DETAIL": "Success"}, "URI": "/key_command/"}
		result = json.loads( response.text )
		pprint( result )
		return result

	def volume_up( self ):
		headers = {
			"Content-Type": "application/json" ,
			"AUTH": self.options["access_token"]
		}
		data = {
			"_url": "/key_command/" ,
			"KEYLIST": [{
				"CODESET": 5 ,
				"CODE": 1 ,
				"ACTION": "KEYPRESS"
			}]
		}
		url = f"https://{self.options['ip']}:7345/key_command/"
		response = requests.put( url , headers=headers , data=json.dumps( data ) , verify=False )
		response.raise_for_status()

		# Should Return
		# {"STATUS": {"RESULT": "SUCCESS", "DETAIL": "Success"}, "URI": "/key_command/"}
		result = json.loads( response.text )
		pprint( result )
		return result

	def mute_off( self ):
		headers = {
			"Content-Type": "application/json" ,
			"AUTH": self.options["access_token"]
		}
		data = {
			"_url": "/key_command/" ,
			"KEYLIST": [{
				"CODESET": 5 ,
				"CODE": 2 ,
				"ACTION": "KEYPRESS"
			}]
		}
		url = f"https://{self.options['ip']}:7345/key_command/"
		response = requests.put( url , headers=headers , data=json.dumps( data ) , verify=False )
		response.raise_for_status()

		# Should Return
		# {"STATUS": {"RESULT": "SUCCESS", "DETAIL": "Success"}, "URI": "/key_command/"}
		result = json.loads( response.text )
		pprint( result )
		return result

	def mute_on( self ):
		headers = {
			"Content-Type": "application/json" ,
			"AUTH": self.options["access_token"]
		}
		data = {
			"_url": "/key_command/" ,
			"KEYLIST": [{
				"CODESET": 5 ,
				"CODE": 3 ,
				"ACTION": "KEYPRESS"
			}]
		}
		url = f"https://{self.options['ip']}:7345/key_command/"
		response = requests.put( url , headers=headers , data=json.dumps( data ) , verify=False )
		response.raise_for_status()

		# Should Return
		# {"STATUS": {"RESULT": "SUCCESS", "DETAIL": "Success"}, "URI": "/key_command/"}
		result = json.loads( response.text )
		pprint( result )
		return result

	def mute_toggle( self ):
		headers = {
			"Content-Type": "application/json" ,
			"AUTH": self.options["access_token"]
		}
		data = {
			"_url": "/key_command/" ,
			"KEYLIST": [{
				"CODESET": 5 ,
				"CODE": 4 ,
				"ACTION": "KEYPRESS"
			}]
		}
		url = f"https://{self.options['ip']}:7345/key_command/"
		response = requests.put( url , headers=headers , data=json.dumps( data ) , verify=False )
		response.raise_for_status()

		# Should Return
		# {"STATUS": {"RESULT": "SUCCESS", "DETAIL": "Success"}, "URI": "/key_command/"}
		result = json.loads( response.text )
		pprint( result )
		return result

	def get_current_input( self ):
		headers = {
			'AUTH': self.options["access_token"]
		}
		url = f"https://{self.options['ip']}:7345/menu_native/dynamic/tv_settings/devices/current_input"
		response = requests.get( url , headers=headers , verify=False )
		response.raise_for_status()

		# Should Return
		# {'HASHLIST': [1209501159, 1519436522],
		#  'ITEMS': [{'CNAME': 'current_input',
		#             'ENABLED': 'FALSE',
		#             'HASHVAL': 2690294191,
		#             'HIDDEN': 'TRUE',
		#             'NAME': 'Current Input',
		#             'TYPE': 'T_STRING_V1',
		#             'VALUE': 'hdmi2'}],
		#  'PARAMETERS': {'FLAT': 'TRUE', 'HASHONLY': 'FALSE', 'HELPTEXT': 'FALSE'},
		#  'STATUS': {'DETAIL': 'Success', 'RESULT': 'SUCCESS'},
		#  'URI': '/menu_native/dynamic/tv_settings/devices/current_input'}
		result = json.loads( response.text )
		#pprint( result )
		return { "name": result["ITEMS"][0]["VALUE"] , "hash_value": result["ITEMS"][0]["HASHVAL"] }

	def get_available_inputs( self ):
		headers = {
			'AUTH': self.options["access_token"]
		}
		url = f"https://{self.options['ip']}:7345/menu_native/dynamic/tv_settings/devices/name_input"
		response = requests.get( url , headers=headers , verify=False )
		response.raise_for_status()
		result = json.loads( response.text )
		# pprint( result )
		inputs = [ { "name": x["NAME"] , "hashval": x["HASHVAL"] } for x in result["ITEMS"] ]
		return inputs

	def set_input( self , input_name ):

		# For this one, you first need the hash value of the current input id
		current_input = self.get_current_input()

		headers = {
			"Content-Type": "application/json" ,
			"AUTH": self.options["access_token"]
		}
		data = {
			"_url": "/menu_native/dynamic/tv_settings/devices/current_input" ,
			"item_name": "CURRENT_INPUT" ,
			"VALUE": input_name ,
			"HASHVAL": current_input["hash_value"] ,
			"REQUEST": "MODIFY"
		}
		url = f"https://{self.options['ip']}:7345/menu_native/dynamic/tv_settings/devices/current_input"
		response = requests.put( url , headers=headers , data=json.dumps( data ) , verify=False )
		response.raise_for_status()

		# Should Return

		result = json.loads( response.text )
		pprint( result )
		return result

	def cycle_input( self ):
		headers = {
			"Content-Type": "application/json" ,
			"AUTH": self.options["access_token"]
		}
		data = {
			"_url": "/key_command/" ,
			"KEYLIST": [{
				"CODESET": 7 ,
				"CODE": 1 ,
				"ACTION": "KEYPRESS"
			}]
		}
		url = f"https://{self.options['ip']}:7345/key_command/"
		response = requests.put( url , headers=headers , data=json.dumps( data ) , verify=False )
		response.raise_for_status()

		# Should Return
		# {"STATUS": {"RESULT": "SUCCESS", "DETAIL": "Success"}, "URI": "/key_command/"}
		result = json.loads( response.text )
		#pprint( result )
		return result

	def get_audio_settings( self ):
		headers = {
			'AUTH': self.options["access_token"]
		}
		url = f"https://{self.options['ip']}:7345/menu_native/dynamic/tv_settings/audio"
		response = requests.get( url , headers=headers , verify=False )
		response.raise_for_status()
		result = json.loads( response.text )
		#pprint( result )
		return result