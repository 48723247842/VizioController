import viziocontroller

if __name__ == "__main__":

	tv = viziocontroller.VizioController({
			"name": "Loft TV" ,
			"mac_address": "2c:64:1f:25:6b:3c" ,
			"ip": "192.168.1.100" ,
			"access_token": "Zhehzvszfq"
		})
	print( tv.ip )

	current_volume = tv.api.get_volume()
	tv.api.volume_up()
	tv.api.volume_down()

	audio_settings = tv.api.get_audio_settings()
	tv_speakers = tv.api.get_audio_setting( "tv_speakers" )
	all_audio_settings_options = tv.api.get_all_audio_settings_options()
	tv_speakers = tv.api.get_audio_settings_options( "tv_speakers" )
	tv.api.set_audio_setting( "mute" , "Off" )

	current_input = tv.api.get_current_input()
	available_inputs = tv.api.get_available_inputs()
	tv.api.set_input( "HDMI-1" )
	tv.api.set_input( "HDMI-2" )

	tv.api.cycle_input()
	tv.api.cycle_input()

	settings_types = tv.api.get_settings_types()
	audio_settings = tv.api.get_all_settings_for_type( "audio" )
	backlight = tv.api.get_setting( "picture" , "backlight" )
	picture_settings = tv.api.get_all_settings_options_for_type( "picture" )
	backlight_setting = tv.api.get_settings_option( "picture" , "backlight" )
	tv.api.set_settings_option( "picture" , "backlight" , 100 )

	tv.api.launch_app_config( "1" , 3 )
	current_app = tv.api.get_current_app()