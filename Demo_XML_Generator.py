from bs4 import BeautifulSoup as bs

class DictMaker(dict):
	def add(self, key, value):
		self[key] = value


def parseFileToDict(fileName, targetString):
	handler = open(fileName, 'r').read()
	content = bs(handler, 'lxml-xml')

	dict_object = DictMaker()
	i = 0

	for tag in content.findAll(targetString):
		dict_object.add(i, {'Platform' : tag.Platform.text,
		                    'TItle' : tag.Title.text,
		                    'Developer' : tag.Developer.text,
		                    'Publisher' : tag.Publisher.text,
		                    'Director' : tag.Director.text,
		                    'Producer' : tag.Producer.text,
		                    'Genre' : tag.Genre.text,
		                    'ESRB' : tag.ESRB.text,
		                    'Release' : tag.Release.text
		                    })
		i += 1
	return dict_object



if __name__ == "__main__":
	fileName ='Game_catalog.xml'
	targetString = 'GameCollection'

	dictData = parseFileToDict(fileName, targetString)
	for k,v in dictData.items():
		if 'PS4' in v.get('Platform'):
			print( v.get('Platform'), v.get('TItle'), v.get('ESRB'))
