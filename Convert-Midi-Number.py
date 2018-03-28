#CUI ツール

print("【MIDIナンバーから音名と周波数の判定ツール】\n MIDIナンバーを入力してください")

#midinumber = 60
midinumber = input(">>")
midinumber = int(midinumber)

note_name = ("C","C#","D","D#","E","F","F#","G","G#","A","A#","B") #タプル
note = midinumber % 12 #ノート判定
frequency = 440 *(pow (2 , (midinumber - 69) / 12))#周波数 f= 440×2(d-69)/12

print("MIDI Number:" + str(midinumber))
print("Note Name:" + str(note_name[note])) #求めた余りをもとにタプルから音名を取り出す
print("Frequency:" +str('{:.2f}'.format(frequency)) +" Hz") #小数点以下２位まで表示
