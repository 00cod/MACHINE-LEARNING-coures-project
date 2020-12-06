#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-11-23 20:04:49
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$

import os
import numpy as np
import pandas as pd
from pandas import DataFrame
from numpy import nan as NaN
def test_capital_loss(train_data):
	count = 0
	for row in train_data.itertuples(index=True, name='Pandas'):
		captial_gain = getattr(row, '_10')
		if captial_gain == 99999:
			count += 1
	print(count)


def test_education(train_data):
	education_dict = {}
	different_list = []
	for row in train_data.itertuples():
		education = getattr(row, 'education')
		education_num = getattr(row, 'education-num')
		if education not in education_dict:
			education_dict[education] = education_num
		else:
			if education_dict[education] != education_num:
				different_list.append([education, education_num])
	print(different_list)
def data_drop(train_data):
	train_data = train_data.drop(['education'],axis = 1)
	return train_data

def print_feature(train_data):
	for i in train_data:
		print(i)
		print(train_data[i].unique())
def find_feature_from_train_data(train_data):
	train_data_clomn = {}
	for i in train_data:
		if train_data[i].dtypes == 'object':
			train_data_clomn[i] = {}
			n = 0
			for y in train_data[i].unique():
				train_data_clomn[i][y] = n
				n = n+1
	return train_data_clomn

def transform_train_data(train_data,train_data_clomn):
	for i in train_data:
		if train_data[i].dtypes == 'object':
			for y in train_data_clomn[i]:
				train_data[i].replace(y,train_data_clomn[i][y],inplace=True)
	return train_data

def transform_test_data(train_data,train_data_clomn):
	for i in train_data:
		if train_data[i].dtypes == 'object':
			for y in train_data_clomn[i]:
				train_data[i].replace(y,train_data_clomn[i][y],inplace=True)
	return train_data


train_data = pd.read_csv('train.csv')
test_data = pd.read_csv('test.csv')
train_data = pd.DataFrame(train_data)
test_data = pd.DataFrame(test_data)


train_feature_dict = find_feature_from_train_data(train_data)
train_feature_dict['native-country'][' Holand-Netherlands'] = train_feature_dict['native-country'][' ?']
#print(train_feature_dict)
processed_train_data = transform_train_data(train_data,train_feature_dict)
#test_education(train_data)
#print_feature(processed_train_data)
test_capital_loss(train_data)
processed_test_data = transform_train_data(test_data,train_feature_dict)
processed_test_data = data_drop(test_data)
processed_train_data_x = train_data.iloc[:,:-1]
processed_train_data_x = data_drop(processed_train_data_x)
processed_train_data_y = train_data.iloc[:,-1:]
#print_feature(processed_train_data_x)
processed_test_data.to_csv('processed_test_data.csv',index=False)
processed_train_data_x.to_csv('processed_train_data_x.csv',index=False)
processed_train_data_y.to_csv('processed_train_data_y.csv',index=False)




