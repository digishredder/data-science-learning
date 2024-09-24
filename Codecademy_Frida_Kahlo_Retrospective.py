paintings = ['The Two Fridas', 'My Dress Hangs Here', 'Tree of Hope', 'Self Portrait With Monkeys']

dates = [1939, 1933, 1946, 1940]

# paintings = list(zip(paintings, dates))

# print(paintings)

paintings.append('The Broken Column')
dates.append(1944)
paintings.append('The Wounded Deer')
dates.append(1946)
paintings.append('Me and My Doll')
dates.append(1937)

paintings = list(zip(paintings, dates))

print(paintings)

paintings_length = len(paintings)

print("There are "+ str(paintings_length) + " paintings." + "\n")

audio_tour_number = list(range(1,8))

print(str(audio_tour_number) + "\n")

master_list = list(zip(audio_tour_number, paintings))

print("This is the full list:" + "\n" + str(master_list))
