#!/usr/bin/env python3
import cgi
import html
import sys
import pandas as pd
import numpy as np
import codecs

sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()
name = form.getfirst("TEXT_1", "не задано")
password = form.getfirst("TEXT_2", "не задано")
name = html.escape(name)
password = html.escape(password)

InfoTable = pd.read_csv(r"G:\Users\Boris\Documents\MEGAsync\PythonServer\cgi-bin\InfoTable.csv", index_col=[0], sep=";", encoding='cp1251')
print("""<!DOCTYPE HTML>
			<html>
			<head>
				<meta charset="utf-8">
				<title>Обработка данных форм</title>
			</head>
			<body>""")
if password != str(InfoTable.loc[name, "Password"]):
	print("Content-type: text/html\n")
	print("<h1>Обработка данных форм!</h1>")
	print("<p>Wrong Pasword</p>")
else:
	santa = InfoTable.loc[name, "Santa"]
	wish = InfoTable.loc[name, "Wish"]
	print("Content-type: text/html\n")
	print("""<!DOCTYPE HTML>
			<html>
			<head>
				<meta charset="utf-8">
				<title>Обработка данных форм</title>
			</head>
			<body>""")

	print("<h1>Обработка данных форм!</h1>")
	print("<p>Ты тайный санта для {}.</p>".format(santa))
	if not pd.isnull(wish):
		print("<p>Здесь перечислены указаные интересы: {}.</p>".format(wish))
	else:
		print("<p>Пока что твой тайный друг не высказал никаких пожеланий по поводу подарка, но это может измениться в скором времени.</p>")
		print("<p>Советую проверить эту страницу еще раз позже.</p>")
print("""</body>
		</html>""")