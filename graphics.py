def draw_card(value, suit):
    image = (
        ".------.",
       f"|{value}    {suit}|",
        "|      |",
        "|      |",
       f"|{suit}    {value}|",
        "`------'",
    )

    for line in image:
        print(line)

#♠♣♥♦
draw_card('A', '♦')