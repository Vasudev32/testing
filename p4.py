document = "My name is vasu"
name = "vasu"
word_counts = {}
for i in document:
    print(i)
    if i in word_counts:

        word_counts[i] += 1
    # else:
    #     word_counts = 1
print(word_counts)
# name = "vasu"
# for i in name:
#     print(i)