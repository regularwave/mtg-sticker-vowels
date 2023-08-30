import random
iterations, j = 1234567, 0
for draws in range(iterations):
    stickerVowels = [6, 5, 5, 4, 4, 4, 4, 4, 4, 3]
    random.shuffle(stickerVowels)
    if 3 in stickerVowels[-3::]:
        j += 1
print(j/iterations)
