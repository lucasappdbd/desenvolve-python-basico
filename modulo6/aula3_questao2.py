URLs = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]

dominios = list()

for i in range(len(URLs)):
    dominios.append((URLs[i])[4:-4])

print(f"URLs: {URLs}")
print(f"Domínios: {dominios}")