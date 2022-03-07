import grab_info
import configparser

write_path='./records.csv'

config = configparser.ConfigParser()
config.read('config.ini')


for section in config.sections():
	nickname = section
	url = config[section]['url']
	xpath = config[section]['xpath']
	try:
		always_increment = int(config[section]['always_increment'])
	except:
		always_increment = ''

	current = grab_info.get_info(url=url, xpath=xpath, nickname=nickname, write_path=write_path)
	result_string = current.retrieve()
	if always_increment != '':
		result_string = result_string[always_increment]

	# clean string
	result_string = result_string.replace('\t','').replace('\n','')

	write_status = current.write_result(result_string)

	if write_status == 0:
		print('Success!')