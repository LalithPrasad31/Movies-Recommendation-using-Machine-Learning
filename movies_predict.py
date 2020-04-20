
from flask import Flask, redirect, url_for, request 
import numpy as np
import csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
	
app = Flask(__name__) 
 
@app.route('/movies', methods=["GET", "POST"]) 
def movies():
	lang = request.form['lang']
	genre = int(request.form['genre'])
	rating = int(request.form['rate'])
	year = int(request.form['year'])
	pop = int(request.form['pop'])
	runtime = int(request.form['run'])
	rating = rating*2
	fil = 'E:\python project\Dataset\\'
	fil = fil+lang+'.csv'
	names = ['1','2','3','4','5','6']
	dataset = pd.read_csv(fil, names=names)
	x = dataset.iloc[:, :-1].values
	y = dataset.iloc[:, 5].values
	scaler = StandardScaler()
	scaler.fit(x)
	
	x = scaler.transform(x)
	
	classifier = KNeighborsClassifier(n_neighbors=1)
	classifier.fit(x, y)
	
	x_t = [[pop,runtime,genre,rating,year]]
	
	x_t = scaler.transform(x_t)
	
	y_pred = classifier.predict(x_t)
	
	with open(fil, 'r') as inp, open('E:\python project\Dataset\\edit1.csv', 'w') as out:
		writer = csv.writer(out)
		for row in csv.reader(inp):
				if row[5] != str(y_pred[0]):
					writer.writerow(row)
	fil = 'E:\python project\Dataset\\edit1.csv'
	names = ['1','2','3','4','5','6']
	dataset = pd.read_csv(fil, names=names)
	x = dataset.iloc[:, :-1].values
	y = dataset.iloc[:, 5].values
	scaler = StandardScaler()
	scaler.fit(x)
	
	x = scaler.transform(x)
	
	classifier = KNeighborsClassifier(n_neighbors=1)
	classifier.fit(x, y)
	x_t = [[pop,runtime,genre,rating,year]]
	x_t = scaler.transform(x_t)
	
	y_pred1 = classifier.predict(x_t)
	print(y_pred1)
	print(y_pred)
	'''
	with open('E:\python project\Dataset\\edit1.csv', 'r') as inp, open('E:\python project\Dataset\\edit2.csv', 'w') as out:
		writer = csv.writer(out)
		for row in csv.reader(inp):
				if row[5] != str(y_pred1[0]):
					writer.writerow(row)
    
	fil = 'E:\python project\Dataset\\edit2.csv'
	names = ['1','2','3','4','5','6']
	dataset = pd.read_csv(fil, names=names)
	x = dataset.iloc[:, :-1].values
	y = dataset.iloc[:, 5].values
	scaler = StandardScaler()
	scaler.fit(x)
	
	x = scaler.transform(x)
	
	classifier = KNeighborsClassifier(n_neighbors=1)
	classifier.fit(x, y)
	
	x_t = [[pop,runtime,genre,rating,year]]
	x_t = scaler.transform(x_t)

	y_pred2 = classifier.predict(x_t)
	
	
	with open('E:\python project\Dataset\\edit2.csv', 'r') as inp, open('E:\python project\Dataset\\edit3.csv', 'w') as out:
		writer = csv.writer(out)
		for row in csv.reader(inp):
			if row[5] != str(y_pred2[0]):
				writer.writerow(row)
    
	fil = 'E:\python project\Dataset\\edit3.csv'
	names = ['1','2','3','4','5','6']
	dataset = pd.read_csv(fil, names=names)
	x = dataset.iloc[:, :-1].values
	y = dataset.iloc[:, 5].values
	scaler = StandardScaler()
	scaler.fit(x)
	
	x = scaler.transform(x)
	
	classifier = KNeighborsClassifier(n_neighbors=1)
	classifier.fit(x, y)
	
	x_t = [[pop,runtime,genre,rating,year]]
	x_t = scaler.transform(x_t)
	
	y_pred3 = classifier.predict(x_t)
	'''
	sel = "<font color=""red""><h1><u>TOP SELECTIONS FOR YOU</u></h1></font><h3>"

	bre="<br><br>"
	cent = "<center>"
	
	return  '{} {} {} {} {}'.format(cent,sel,y_pred,bre,y_pred1)
  
if __name__ == '__main__': 
   app.run(debug = True) 