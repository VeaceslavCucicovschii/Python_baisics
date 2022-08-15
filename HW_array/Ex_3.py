guests_1 = [ "Bethaney Bain", "Kacey Johns", "Manpreet Saunders" ]
guests_2 = [ "Elwood Curtis", "Diya Griffin", "Kacey Johns" ]
guests_3 = [ "Tobey Weiss", "Kadie Barnes", "Diya Griffin" ]

combined_list = guests_1 + guests_2 + guests_3

for i in range(len(combined_list)):
  if combined_list[0] != combined_list[i]:
    final_list = [combined_list[0], combined_list[i]]

for i in range(len(combined_list)):
  k = True
  for j in range(len(final_list)):
    if combined_list[i] == final_list[j]:
      k = False
  if k:  
    final_list.append(combined_list[i])

for line in final_list:
  print(line)