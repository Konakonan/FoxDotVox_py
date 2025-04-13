# まずテンポを下げてHIPHOPっぽく
Clock.bpm = 80

# キックとスネアの基本パターン
d1 >> play("X   X   X   X ", sample=2, dur=1)

# スネアは2拍目と4拍目に
d2 >> play("  o   o   ", sample=1, dur=1)

# ハイハットはトリッキーに（16分音符でランダム揺らし）
d3 >> play("-[--]-", dur=0.25, amp=PRand([0.3, 0.5, 0.7]))

# 808系ベース（重低音）
p1 >> dbass([0, -1, -3, -5], dur=1, amp=0.8, cutoff=linvar([200, 1200], 16), drive=0.4)

# 背景の雰囲気音（トラップ系コード）
p2 >> pads([0, 3, 5], dur=8, chop=8, amp=0.2, room=1, mix=0.6)
