max_life_expectancy = 0
min_life_expectancy = 10000

max_life_expectancy_msg = ""
min_life_expectancy_msg = ""

life_expectancy_list = []

max_life_expectancy_overall = 0
min_life_expectancy_overall = 10000

max_life_expectancy_overall_msg = ""
min_life_expectancy_overall_msg = ""

year_of_interest = input('Enter the year of interest: ')

with open('/Users/smelcerc/Code/GitHub/smelcerc.github.io/CS-101/W11/life-expectancy.csv', 'r') as life_data:
    row_count = 0
    for row in life_data:
        if row_count > 0:
            clean_line = row.strip()
            parts = clean_line.split(",")
            entity = parts[0]
            code = parts[1]
            year = parts[2]
            life_expectancy = float(parts[3])

            if year == year_of_interest:
                life_expectancy_list.append(life_expectancy)

                if life_expectancy > max_life_expectancy:
                    max_life_expectancy = life_expectancy
                    max_life_expectancy_msg = f"The max life expectancy was in {entity} with {life_expectancy}"
                
                if life_expectancy < min_life_expectancy:
                    min_life_expectancy = life_expectancy
                    min_life_expectancy_msg = f"The min life expectancy was in {entity} with {life_expectancy}"

            if life_expectancy > max_life_expectancy_overall:
                max_life_expectancy_overall = life_expectancy
                max_life_expectancy_overall_msg = f"The overall max life expectancy is: {life_expectancy} from {entity} in {year}"

            if life_expectancy < min_life_expectancy_overall:
                min_life_expectancy_overall = life_expectancy
                min_life_expectancy_overall_msg = f"The overall min life expectancy is: {life_expectancy} from {entity} in {year}"

        row_count += 1

print(f"\n{max_life_expectancy_overall_msg}")
print(min_life_expectancy_overall_msg)

print(f"\nFor the year {year_of_interest}:")

average_for_year = sum(life_expectancy_list)/len(life_expectancy_list)
print(f"The average life expectancy across all countries was {average_for_year}")
print(max_life_expectancy_msg)
print(min_life_expectancy_msg)