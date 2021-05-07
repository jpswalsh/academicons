#!/usr/bin/env python3
""" Simple python script to save a screenshoft of table.html
"""

from selenium import webdriver
from pathlib import Path
import argparse
import sys

browser_map = {
	'firefox': webdriver.Firefox,
	'chrome': webdriver.Chrome,
	'ie': webdriver.Ie,
	'opera': webdriver.Opera,
	'safari': webdriver.Safari,
	'phantomjs': webdriver.PhantomJS,
}


def capture(output, driver_name):
	""" Main function: starts the selenium driver, gets the element, and saves the screenshot.
	"""
	url = 'file://' + str(Path(__file__).with_name('table.html').absolute())
	driver = browser_map[driver_name]()

	driver.get(url)

	elem = driver.find_element_by_css_selector('table.ai')
	elem.screenshot(output)

	driver.quit()


if __name__ == '__main__':
	parser = argparse.ArgumentParser(description=__doc__)

	parser.add_argument('output', metavar='glyph-table.png', nargs='?',
			help='file output', default='glyph-table.png')

	parser.add_argument('-d', '--driver', dest='driver', action='store', default='chrome',
			help='Selenium browser to use, from: ' + ', '.join(browser_map.keys()))

	args = parser.parse_args()

	if args.driver not in browser_map:
		print('Invalid driver specified:', args.driver, file=sys.stderr)
		parser.print_help()
		sys.exit(1)

	capture(args.output, args.driver)
