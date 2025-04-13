#テンポ設定
Clock.bpm=0 #130～150くらい(?)

#ドラム x:キック、o:スネア、-:ハイハット、[]:複数音、{}:ランダムで音を選む
d1 >>play("X ",dur=0.25,amp=1.2)#X:ドラム、dur:1拍が0.25秒、amp:音量

d2>>play("--[--]--",dur=0.25,amp=0.6)#-:ハイハット、[]:音を詰める

#シンセ
p1 >> sawbass(var([0, 2, 4, 3], 8) + PWhite(-1, 1), dur=0.25, 
              amp=0.8, cutoff=linvar([300, 1800], 16), 
              drive=0.4, formant=1)
#sawbass>シンセ設定、sawbassはウネっている低音系のシンセ
#var([],数値)>数値拍ごとにベースの音階が変わる
#+PWhite(-1,1):-1~1のランダムで微妙に音をブレさせる
#cutoff=linvar([300,1800],16)
#drive=0.4:歪ませる




p2 >> pads([0, 4, 5], dur=8, amp=0.3, chop=8, room=1, mix=0.7)
#pads:空間系のシンセ
#chop=8:音を8分割して小刻みにカット
#room=1,mix=0.7:リバーブ効果


p3 >> pluck(PWalk() + var([7, 9], 16), dur=0.25, amp=0.4, 
            echo=0.25, echotime=4, shape=0.2)
#shape=0.2:波形を変形 → シャープで独特な音




print(SynthDefs)  # 使用可能なシンセ名
print(SynthDefs["pluck"].info())  # そのシンセのパラメータ一覧


# パラメータ	内容	例
# dur	ノートの長さ（拍数）	dur=0.25（16分音符）
# oct	オクターブ	oct=5（5オクターブ目）
# amp	音量（0〜1）	amp=0.7
# sus	サスティン（音の保持時間）	sus=0.2
# pan	左右定位（-1〜1）	pan=(-1,1)
# rate	再生スピード	rate=1.5（1.5倍速）
# slide	ピッチを滑らかに変化	slide=0.5
# formant	フォルマント（声っぽさ）	formant=2
# vib	ビブラートの速さ	vib=4
# vibdepth	ビブラートの深さ	vibdepth=0.1
# shape	波形の歪みや変形度	shape=0.3
# chop	サンプルを刻む	chop=4（4分割）
# room	リバーブ空間の広さ	room=0.8
# mix	リバーブの量	mix=0.5
# echo	エコーの長さ	echo=0.25
# decay	音の減衰時間	decay=1.5
# bend	ピッチベンド	bend=1
# blur	ノートを重ねる	blur=2（和音っぽくなる）


Scale.default = Scale.minor
# 数字	実際の音（Cメジャー(スケールがメジャであった場合）
# 0	C（ド）
# 1	D（レ）
# 2	E（ミ）
# 3	F（ファ）
# 4	G（ソ）
# 5	A（ラ）
# 6	B（シ）
# 7	C（1オクターブ上）


# コード	音の鳴り方	説明
# [0, 2, 4]	♪ ド → ミ → ソ	それぞれ別々のタイミングで鳴る（メロディ）
# [[0, 2, 4]]	♫ ドミソ（同時に鳴る）	同時に鳴る音（和音）
# [ [0, 2, 4], [5, 7, 9] ]	♫ ドミソ → ♫ ファソラ	和音を交互に鳴らす

