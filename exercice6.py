days  = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

fiveDays1 = days[0:5]
endDays1 = days[5:7]

fiveDays2 = days[:5]
endDays2 = days[-2:]

endDay1 = days[len(days) - 1]
endDay2 = days[-1]

inverse = days[::-1]

print("Les cinq premiers jours de la semaine :", fiveDays1)
print("Les jours du week-end :", endDays1)
print("\nAutre méthode :")
print("Les cinq premiers jours de la semaine :", fiveDays2)
print("Les jours du week-end :", endDays2)
print("\nLe dernier jour de la semaine (méthode 1) :", endDay1)
print("Le dernier jour de la semaine (méthode 2) :", endDay2)
print("\nJours de la semaine inversés :", inverse)