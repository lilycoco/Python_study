# 演習問題

# 2
letter = "じこーだずまあさかんでのみしーゅっみてはたなのんしだいろな"
print(letter[::2])
print(letter[1::2])

# 3
def introduction(x, y=20):
  return "私の名前は" + x + "で" + str(y) + "歳です"
print(introduction(x="Ryoko"))

# 4
galaxy = "「ではみなさんは、そういうふうに川だと云いわれたり、乳の流れたあとだと云われたりしていたこのぼんやりと白いものがほんとうは何かご承知ですか。」先生は、黒板に吊つるした大きな黒い星座の図の、上から下へ白くけぶった銀河帯のようなところを指さしながら、みんなに問といをかけました。"
print(len(set(galaxy)))

# 5
number = []
for i in range(101):
  number.append(str(i) + "円")
print(number)
