from bs4 import BeautifulSoup as bs

class DictMaker(dict):
	def add(self, key, value):
		self[key] = value


def parseFileToDict(input1, input2):
	"""
	:param input1: The string which is to be reversed.
	:param input2: The string which is to be reversed.
	:return: The string which gets reversed.
	"""
	handler = open(input1, 'r').read()
	content = bs(handler, 'lxml-xml')  # if not working, try pip python install lxml

	dict_object = DictMaker()
	i = 0

	for tag in content.findAll(input2):
		dict_object.add(i, {
			'Platform': tag.Platform.text, 'Title': tag.Title.text, 'Developer': tag.Developer.text,
			'Publisher': tag.Publisher.text, 'Director': tag.Director.text,
			'Producer': tag.Producer.text, 'Genre': tag.Genre.text, 'ESRB': tag.ESRB.text, 'Release': tag.Release.text})
		i += 1
	return dict_object


if __name__ == "__main__":
	fileName = 'Game_catalog.xml'
	targetString = 'GameCollection'

	dictData = parseFileToDict(fileName, targetString)
	for k, v in dictData.items():
		if 'PS4' in v.get('Platform'):
			print(
				('{}' + '\t\tRate : {}' + '\t\t[ Title ] {}').format(v.get('Platform'), v.get('ESRB'), v.get('Title')))
