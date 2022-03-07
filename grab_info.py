import requests
from lxml import html
import datetime

class get_info(object):
	def __init__(self, url='', xpath='', nickname='', write_path=''):
		self.url = url
		self.xpath = xpath
		self.write_path = write_path
		self.nickname = nickname
		self.delimiter = '|'

	def set_new_target(self, url, xpath):
		self.url = url
		self.xpath = xpath
		return 0

	def set_write_path(self, write_path):
		self.write_path = write_path
		return 0

	def set_nickname(self, nickname):
		self.nickname = nickname
		return 0
	def record_datetime(self):
		dt = datetime.datetime.now()
		self.recorded_datetime = dt.strftime("%m/%d/%Y, %H:%M:%S")
		return 0

	def retrieve(self):
		assert self.url != '' and self.xpath != '', "Must first set URL and xpath!"
		page = requests.get(self.url)
		self.record_datetime()

		# temp page write
		with open('page_content.html', 'w') as f:
			f.write(str(page.content))
			f.close()

		tree = html.fromstring(page.content)  
		result_string = tree.xpath(self.xpath)
		return result_string


	def write_result(self, result, write_nickname=True, write_datetime=True):
		write_list = []
		
		if write_nickname==True:
			write_list.append(self.nickname)
		if write_datetime==True:
			write_list.append(self.recorded_datetime)
		
		write_list.append(result)
		write_text = self.delimiter.join(write_list)

		with open(self.write_path, 'a') as f:
			f.write(write_text + '\n')
			f.close()
		return 0