with open("exam.txt", encoding="utf-8") as src:
    text = open("exam.txt", encoding="utf-8")
    print(text.read())
    line = 0
    word = input("Введіть слово: ")
    file = src.read().split('\n')
    for x in file:
        for y in x.split():
            if y.lower() == word.lower():
                print("Слово знайдено у абзаці: " + x)
                line += 1
    if line == 0:
        print("Слово не знайдено.")
