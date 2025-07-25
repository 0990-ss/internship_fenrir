def isValid(s:str) -> bool:

  list_1 = [] #開きかっこを保存するリスト
  list_2 = [] #かっこのパターンを確認するための一時保存リスト

  for char in s:
    #閉じかっこが入力された場合
    if char in [")","}","]"]:
      if len(list_1) == 0:
        return False

      #list_1から、最後に入力された開きかっこを取り出す(ない場合はFalse↑)
      list_2.append(list_1.pop())
      list_2.append(char)

      #かっこが対応していればlist_2を初期化(非対応であればFalse)
      if "".join(list_2) == "()" or "".join(list_2) == "{}" or "".join(list_2) == "[]":
        list_2 = []
      else:
        return False

    #開きかっこ(または何らかの文字)が入力された場合
    else:
      list_1.append(char)

  #最終的にlist_1が空であればTrue(でなければFalse)
  if len(list_1) == 0:
    return True
  else:
    return False

#テスト
s="()"
print(isValid(s))
s="([]){}"
print(isValid(s))
s="({)}"
print(isValid(s))
s=")}"
print(isValid(s))
s="ABC123"
print(isValid(s))
