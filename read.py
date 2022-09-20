#讀取檔案

data = []
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 1000 == 0: # count / 1000 的餘數 = 0
			print(len(data))
sum_len = 0			
for d in data:
	sum_len += len(d) # sum_len = sum_len + len(d)
avg_len = sum_len / len(data)
print('檔案已讀取完畢,總共有', len(data), '筆留言')
print('留言的平均長度為 ', avg_len)

# 篩選留言

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
print('總共有', len(new), '筆留言長度小於100')

good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('總共有', len(good), '筆留言提到good')