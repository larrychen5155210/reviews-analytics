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
print('檔案已讀取完畢,總共有', len(data), '筆資料')
print('平均長度為 ', avg_len)