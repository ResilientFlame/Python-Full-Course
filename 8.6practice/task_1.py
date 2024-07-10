count = 0
for i in range(10):
    scream_ = input('Крикните какую-то фразу чтобы попасть на борт ')
    if scream_ == 'Карамба' or scream_ == 'карамба':
        count += 1

print(count)