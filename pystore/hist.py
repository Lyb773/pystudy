def histogram(seq):
    d = dict()
    for e in seq:
        if e not in d:
            d[e] = 1
        else:
            d[e] += 1
    return d

def print_hist(hist):
    for key, value in hist.items():
        print(key, value)

def main():
  h = histogram('brontosaurus')
  print_hist(h)

if __name__ == "__main__":
    main()
