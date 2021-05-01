# -*- coding: utf-8 -*-
"""
Created on 2021

@author: pengz
"""

'''
KMP Search
'''

def get_next_arr(s):
	next_arr = [0 for i in range(len(s))]
	i = 1  # 从第二个开始找, 第一个永远是0
	now = next_arr[i-1]
	while i < len(s):
		if s[i] == s[now]:
			now += 1
			next_arr[i] = now
			i += 1
		else:
			if now == 0:
				i += 1
			else:
				now = next_arr[now-1]
	return next_arr


def kmp_search(s,p):
	s_id = 0
	p_id = 0
	res = []  # 用来存放匹配结果
	next_arr = get_next_arr(p)
	while s_id < len(s):
		if s[s_id] == p[p_id]:
			s_id += 1
			p_id += 1
		else:
			if p_id == 0:
				s_id += 1
			else:
				p_id = next_arr[p_id-1]
		if p_id = len(p):
			res.append(s_id - p_id)
			p_id = next_arr[p_id-1]
	return res


print search_kmp("ababaabaabac", "abaabac")