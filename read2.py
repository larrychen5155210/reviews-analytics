import time
import progressbar

data = []
start_time = time.time()
word_count = {}
bar = progressbar.ProgressBar(max_value=1000000)
with open('reviews.txt', 'r') as f:
	count = 0
	for line in f:
		data.append(line)
		count += 1
		bar.update(count)
print('長度 = ', len(data))
count = 0
for d in data:
	words = d.split()
	for word in words:
		if word not in word_count:
			word_count[word] = 1 # 新增新的key進word_count字典
		else:
			word_count[word] += 1
	count += 1
	bar.update(count)
end_time = time.time()
print('總共花了', end_time - start_time, '秒')
for wc in word_count:
	if word_count[wc] > 1000000:
		print(wc, ':', word_count[wc])
print('總共出現', len(word_count), '種單字')

while True:
	word = input('請輸入要查找的單字: ')
	if word == 'q':
		break
	if word in word_count:
		print(word, '總共出現在留言裡', word_count[word], '次')
	else:
		print(word, '沒有出現在留言裡')

print('感謝使用此查詢功能')