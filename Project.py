import pandas as pd
import numpy as np

cases = pd.read_excel('./2014_19년 서울_경기 개별 교통사고 정보.xlsx')

seoul = cases[cases.발생지_시도 == '서울']
kyungi = cases[cases.발생지_시도 == '경기']

seoul_2014 = seoul[(seoul.발생일 >= 20140101) & (seoul.발생일 <= 20141231)]
seoul_2015 = seoul[(seoul.발생일 >= 20150101) & (seoul.발생일 <= 20151231)]
seoul_2016 = seoul[(seoul.발생일 >= 20160101) & (seoul.발생일 <= 20161231)]
seoul_2017 = seoul[(seoul.발생일 >= 20170101) & (seoul.발생일 <= 20171231)]
seoul_2018 = seoul[(seoul.발생일 >= 20180101) & (seoul.발생일 <= 20181231)]
seoul_2019 = seoul[(seoul.발생일 >= 20190101) & (seoul.발생일 <= 20191231)]

kyungi_2014 = kyungi[(kyungi.발생일 >= 20140101) & (kyungi.발생일 <= 20141231)]
kyungi_2015 = kyungi[(kyungi.발생일 >= 20150101) & (kyungi.발생일 <= 20151231)]
kyungi_2016 = kyungi[(kyungi.발생일 >= 20160101) & (kyungi.발생일 <= 20161231)]
kyungi_2017 = kyungi[(kyungi.발생일 >= 20170101) & (kyungi.발생일 <= 20171231)]
kyungi_2018 = kyungi[(kyungi.발생일 >= 20180101) & (kyungi.발생일 <= 20181231)]
kyungi_2019 = kyungi[(kyungi.발생일 >= 20190101) & (kyungi.발생일 <= 20191231)]
