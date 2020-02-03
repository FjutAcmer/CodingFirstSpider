# Automatically created by: scrapyd-deploy

from setuptools import setup, find_packages

setup(
    name='CodingFirstSpider',
    version='1.0',
    packages=find_packages(),
    entry_points={'scrapy': ['settings = CodingFirstSpider.settings']}, install_requires=['scrapy', 'pymysql',
                                                                                          'twisted']
)
