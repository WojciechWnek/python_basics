birthdate = input("Pass birthdate DD-MM-YYYY: ")

months = ("jan", "feb", "mar", "apr", "may", "jun", "jul","aug","sep","oct","nov","dec")

month = int(birthdate[3:5])
print(month)
print("You were born in ", months[month -1] )