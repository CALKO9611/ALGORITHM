Hlo, Hhi = map(int, input().split())
Slo, Shi = map(int, input().split())
Vlo, Vhi = map(int, input().split())
R, G, B = map(int, input().split())

# V
V, m = max(R, G, B), min(R, G, B)

# S
S = 255 * (V - m) / V

# H
if V == R:
    H = 60 * (G - B) / (V - m)
elif V == G:
    H = 120 + 60 * (B - R) / (V - m)
elif V == B:
    H = 240 + 60 * (R - G) / (V - m)

if H < 0:
    H += 360

# 진정한™ 보라색 찾기
if Hlo <= H <= Hhi and Slo <= S <= Shi and Vlo <= V <= Vhi:
    print("Lumi will like it.")
else:
    print("Lumi will not like it.")
