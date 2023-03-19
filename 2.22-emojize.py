emojis = { ":1st_place_medal:": "🥇",
          ":money_bag:": "💰",
          ":smile_cat": "😸"}

text = input("Write some text: ")
emoji = text.find(":")

for i in emojis:
    if i in text:
        val = str(i)

new_text = text.replace(val, emojis[str(val)])
print(new_text)