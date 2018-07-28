









def run():

	with open('./data/aleph.txt', encoding='utf-8') as f:
		for line in f:
			print(line.count('Beatriz'))
		






if __name__ == '__main__':
	run()