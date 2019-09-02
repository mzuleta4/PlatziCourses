def run():
    count = 0
    with open('aleph.txt','r') as f:
        for line in f:
            count += line.count('Beatriz')

    print('Beatriz se encuentra {} veces en el texto'.format(count))

if __name__ == "__main__":
    run()