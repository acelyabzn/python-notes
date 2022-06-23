ad = "Açelya"
soyad = "Bazan"
yas = "17"

msg = "Adım:" + ad + "  " + "Soyadım:" + soyad + "  " + "Yaşım:" + yas
karakterSayisi = len(msg)

# print(msg)

print(karakterSayisi)
print(msg)

print(msg[0]) # B
print(msg[1]) # e
print(msg[-2]) # 1

# iki işlemin sonucu aynıdır.
print(msg[-1]) # 7
print(msg[karakterSayisi -1]) # 7

# print(msg[karakterSayisi]) hata alırız..

# saymaya başlarken 0'dan başlanır.

# 0 dahil 5 dahil değil ilerleme: Adım:
print(msg[0:5])

# 6 dahil 16 dahil değil ilerleme: çelya  Soy
print(msg[6:16])

# 0'dan başlar 10 dahil olmadan ilerler: Adım:Açely
print(msg[:10])

# 10'dan başlar -1'e kadar ilerler: a  Soyadım:Bazan  Yaşım:17
print(msg[10:])

# -10'dan başlar -1 dahil olmadan ilerler:  Yaşım:17
print(msg[-10:-1])

# 0'dan başlar 20 dahil olmadan 2'şer ilerler: Aı:çla oaı
print(msg[0:20:2])

# baştan sona doğru 3'er ilerler: Amçy yıBa ş:
print(msg[::3])

# sağdan sola doğru ters çevirir: 71:mışaY  nazaB:mıdayoS  ayleçA:mıdA
print(msg[::-1])