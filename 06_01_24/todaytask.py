# x = float(input("Enter the initial revenue (in crores): "))
# after_years = x * 1.089 * 1.089 * 1.089 
# print(after_years)


x = int(input("Enter the initial revenue (in crores) : "))
growth_rate = float(input("Enter Growth rate in percentage : "))
years = int(input("Enter the number of years : "))
after_years = x * ((1 + (growth_rate/100)) ** years)
print("Revenue after given years", after_years)