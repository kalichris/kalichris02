#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  chatgpt3.5.py
#  
#  Copyright 2023 root <root@localhost>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup

import time
class main():
	def __init__(self):
		with sync_playwright() as PW:
			date={
				"url":"https://gptonline.ai/chatgpt-online/",
				"text":"What is the Python "
			}
			brawser=  PW.chromium.launch()
			pg_site= brawser.new_page()
			pg_site.goto(date["url"],timeout=0)
			print("opened %s"%(pg_site.title()))
			
			pg_site.screenshot(path="screenshot1.png")
			
			for x in range(3):
				pg_site.fill("input.msger-input",date["text"])
				pg_site.screenshot(path="screensho2.png")
				pg_site.click("button[type=submit]")
				time.sleep(15)
			source_pg=pg_site.content()
			#print(source_pg)
			soup = BeautifulSoup(source_pg, 'html.parser')
			div_find=soup.find_all('div',class_='msg-text')
			pg_site.screenshot(path="screenshot3.png")
			pg_fi=str(div_find)
			soup2 = BeautifulSoup(pg_fi, 'html.parser')
			div_find2=soup2.select('div.msg-text p')
			for attr in div_find2:
				sn=attr.text
				print(sn)
			pg_site.screenshot(path="screenshot3.png")
			pg_url=pg_site.url
			print("opened %s"%(pg_site.title()))
			print("opened %s"%(pg_url))
			
			

if __name__ == '__main__':
	main()
  
  
