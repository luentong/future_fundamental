# -*- coding: utf-8 -*-
import pdfplumber
import re, time, os
from datetime import date

ScanNumber = 20
def parsepdf_old(path_or_url, proxies=None):
	from pdfminer.pdfparser import PDFParser
	from pdfminer.pdfdocument import PDFDocument
	from pdfminer.pdfpage import PDFPage
	from pdfminer.pdfpage import PDFTextExtractionNotAllowed
	from pdfminer.pdfinterp import PDFResourceManager
	from pdfminer.pdfinterp import PDFPageInterpreter
	from pdfminer.pdfdevice import PDFDevice


	return ""
def parsepdf(path_or_url, mode=1, url_params=None, proxies=None, save_as=None):
	url_mode = False
	if re.search(r'''(?x)\A([a-z][a-z0-9+\-.]*)://([a-z0-9\-._~%]+|\[[a-z0-9\-._~%!$&'()*+,;=:]+\])''',path_or_url):
		url_mode = True
	else:
		pdf_path = path_or_url

	if url_mode:
		import requests
		pdf_url = path_or_url
		headers_d = None
		headers_d = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; rv:11.0) like Gecko)'}
		if not proxies:
			proxy_host = {}
		if not_url_params:
			url_params = {}
			url_params['headers'] = headers_d
			url_params['data'] = None
			url_params['params'] = None
			url_params['proxies'] = proxies
		if not url_params['headers']: url_params['headers'] = headers_d
		if not url_params['data'] or url_params['params']:
			response = requests.post(pdf_url, **url_params)
		else:
			response = requests.get(pdf_url, **url_params)

		pdf_path = save_as if save_as else f'-temp{time.time()}~.pdf'
		#pdf_path = "./所长早读20230731.pdf"
		with open(pdf_path, 'wb') as f:
			for chunk in response.iter_content(chunk_size=1024):
				if chunk:
					f.write(chunk)
					f.flush()
	# print("path before:", pdf_path)
	# #pdf_path = os.path.abspath(pdf_path)
	# print("path inside:", pdf_path)
	pdf_text = ''
	pdf_tables = []
	with pdfplumber.open(pdf_path) as pdf:
		for page in pdf.pages:
			if str(mode).lower() in ['1', 'text','0','3']:
				pdf_text += page.extract_text()
			if str(mode).lower() in ['2', 'table','0','3']:
				pdf_tables += page.extract_tables()

	if url_mode and not save_as:
		try:
			os.remove(pdf_path)
		except Exception as e:
			pass

	if str(mode).lower() in ['1', 'text']:
		return pdf_text
	elif str(mode).lower() in ['2','table']:
		return pdf_tables
	elif str(mode).lower() in ['3','text_and_table']:
		return pdf_text, pdf_tables

def GetPdfData(path):
	print("path???????",path)
	lines = parsepdf(path, mode=1)
	lines = lines.replace('\xa0','')
	i = 0
	res = dict()
	for sub_line in lines.split('\n'):
		index = i//ScanNumber
		if index in res:
			res[index].append(sub_line)
		else:
			res[index] = list()
			res[index].append(sub_line)
		i = i + 1
	return res

def pdf_to_string(path):
	res = GetPdfData(path)
	return res

if __name__=='__main__':
	path = './所长早读20230731.pdf'
	path = './所长早读_' + str(date.today()) + '.pdf'
	res = GetPdfData(path)
	#print(res)
	print(len(res))
	for i in res:
		print(res[i])

