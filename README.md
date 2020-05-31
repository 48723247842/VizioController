# Python Vizio Controller

## Based on https://github.com/vkorn/pyvizio

```
import viziocontroller
if __name__ == "__main__":
	tv = viziocontroller.VizioController({
			"name": "Loft TV" ,
			"mac_address": "2c:64:1f:25:6b:3c" ,
			"ip": "192.168.1.100" ,
			#"access_token": ""
		})
```