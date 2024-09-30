# 2. You have a list of your favourite marvel super heros
# heros=['spider man','thor','hulk','iron man','captain america']
# Using this list

heros=['spider man','thor','hulk','iron man','captain america']    # 1. Length of the list
print(len(heros))

heros.append("black panther")     # 2. Add 'black panther' at the end of this list
print(heros)

heros.remove("black panther")
heros.insert(3,"black panther")              # 3. black panther after hulk
print(heros)
heros.remove("black panther")


#heros.remove("thor")
#heros.remove("hulk")                  # 4. Remove thor and hulk from list and replace them with doctor strange
heros[1:3]=["black panther"]
print(heros)


# 5. Sort the list in alphabetical order
heros.sort()
print(heros)