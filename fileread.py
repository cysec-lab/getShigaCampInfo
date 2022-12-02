import main

with open('sample.txt', 'r') as f:
    kw_list = f.read().split("\n")
    print(kw_list)

for i in kw_list:
    print(i)
    main.makedict(i)