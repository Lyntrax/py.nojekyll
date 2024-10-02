Purihin = ['Pogi', 'Panget', 'Si', 'John', 'Carlo', 'Caspe']
def basher(words):
    iterator = iter(words)
    while True:
        try:
            word = next(iterator)
            if word == 'Panget':
                continue
            print(word)
        except StopIteration:
            break
basher(Purihin)





 