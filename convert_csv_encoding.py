import glob

for filename in glob.glob('*.csv'):
    s = open(filename, mode='r', encoding='utf8').read()
    open(filename, mode='w', encoding='ANSI').write(s)
