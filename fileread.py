import main

with open('sample.txt', 'r') as f:
    kw_list = f.read().split("\n")
    print(kw_list)

# 1 in {1, 2, 3} # True
# 5 in {1, 2, 3} # False

for i in kw_list:

    #if i in {'http://www.omiscale.co.jp/', }:
        #print(i + 'continue')
        #continue

    try:
        main.makedict(i)
    except:
        pass