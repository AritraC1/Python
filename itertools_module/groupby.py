# groupby
# Groups consecutive items based on a key. Input MUST be sorted by the key for correct grouping.

from itertools import groupby

data = [("fruit", "apple"), ("fruit", "banana"), ("veg", "carrot"), ("veg", "spinach")]

# Group by the first item in each tuple
for key, group in groupby(data, key=lambda x: x[0]):
    print(key, ":", [item[1] for item in group])