#version read
with open('database(version).csv', 'r') as f:
    csv_data = f.readlines().split(",")
    not_found = True

    while not_found:
        input_ver = input('知りたいversionを入力してください: ')

        for row in csv_data:
            if input_ver == row[0]:
                print(row)
                not_found = False

        if not_found:
            print("not  found")
        