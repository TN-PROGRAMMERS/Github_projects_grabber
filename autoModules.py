import os 
import sys
import re


def auto_modules(module_name):
	""" this function will automatically :
		-try to import the module
		-if the module doesn't exist it'll:
			-find the pip path for any os 
			-run pip to download the module
		-if the module exist it'll break."""

	python_version = str(int(sys.version_info[0])*10+int(sys.version_info[1]))

	pip_path = str(os.path.dirname(sys.executable))

	try : 
		import module_name
	except :
		print(f"################# Downloading {module_name} ####################")
		try :
			if os.name == 'nt' :
				os.system(pip_path.replace('\\','\\\\')+'\\\\Scripts\\\\pip'+str(int(python_version)/10)+'.exe install '+module_name) # creating the pip path
			else :
				os.system('pip'+str(sys.version_info[0])+' install '+module_name)

			print('you are good to go!')

		except :
			print(f'Download module : {module_name} please !')

