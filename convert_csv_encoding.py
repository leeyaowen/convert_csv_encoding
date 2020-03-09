import glob

while True:
    # noinspection PyBroadException
    try:
        input_encode = input('input_encode=? ')
        output_encode = input('output_encode=? ')
        for filename in glob.glob('*.csv'):
            with open(filename, mode='r', encoding=str(input_encode)) as input_file:
                content = input_file.read()
            with open(filename, mode='w', encoding=str(output_encode)) as output_file:
                output_file.write(content)
        print('Successfully convert!')
    except Exception:
        print('There are some errors!!')

    # noinspection PyBroadException
    try:
        ans = input('\nWant to close? ')
        if str(ans) == 'yes':
            break
        else:
            continue
    except Exception:
        continue
