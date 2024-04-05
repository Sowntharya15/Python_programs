from prettytable import  PrettyTable 
table = PrettyTable()
table.add_column("NO.",["1","2","3","4","5"])
table.add_column("Name",["Bernard Arnault","Elon Musk","Jeff Bezos","Mark Zuckerberg","Larry Ellison"])
table.add_column("Net Worth(in $Billions)",["$233","$194","$195","$177","$141"])
table.add_column("Source of wealth",["LVMH","Tesla,SpaceX","Amazon","Facebook","Oracle"])
table.add_column("Country",["France","United States","United States","United States","United States"])
table.align = 'l'
print(table)


