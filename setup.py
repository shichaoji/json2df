from setuptools import setup, find_packages

setup(
    name = "json2df",
    version = "0.1.3",
    description = "convert json data to Pandas DataFrame",
    author = "Shichao(Richard) Ji",
    author_email = "jshichao@vt.edu",
    url = "https://github.com/shichaoji/json2df",
    download_url = "https://github.com/shichaoji/json2df/archive/0.1.1.tar.gz",
    license = 'MIT',
    keywords = ['data','json','dataframe','python'],
    classifiers = [
	'License :: OSI Approved :: MIT License',
	'Programming Language :: Python :: 2', 
	'Programming Language :: Python :: 3',
	],
    packages = find_packages(),
    install_requires=[
          'pandas',
      ]
)

