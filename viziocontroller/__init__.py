#!/usr/bin/env python3

# Based on https://github.com/vkorn/pyvizio

import discover
import api

class VizioController:

	def __init__( self , options={} ):
		self.options = options
		if "mac_address" not in options:
			print("you have to send the mac adress of the tv")
			sys.exit( 1 )
		if "ip" not in options:
			self.discover = discover.Discover( options )
			self.ip = self.discover.find_tv()
			options["ip"] = self.ip
		else:
			self.ip = options["ip"]
		if "request_token" in options:
			if "code_displayed_on_tv" in options:
				self.api = api.API(options)
				options["access_token"] = self.api.pairing_stage_2( self.ip , options["request_token"] , options["code_displayed_on_tv"] )
		if "access_token" not in options:
			self.api = api.API(options)
			request_token = self.api.pairing_stage_1( self.ip )
			print( f"Ok , now rerun with this and set options['request_token']: {request_token}" )
			print( f"and options['code_displayed_on_tv']: code on tv" )
			sys.exit( 1 )
		else:
			self.access_token = options["access_token"]
		self.api = api.API(options)

if __name__ == "__main__":
	vizio = VizioController({
			"name": "Loft TV" ,
			"mac_address": "2c:64:1f:25:6b:3c" ,
			"ip": "192.168.1.102" ,
			"access_token": "Zhehzvszfq"
		})
	print( vizio.ip )
	vizio.api.get_volume()