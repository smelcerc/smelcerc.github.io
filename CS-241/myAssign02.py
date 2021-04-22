def find_average(lst):
    return sum(lst) / len(lst)

def find_max(comp_lst, zip_lst, state_lst, rate_lst):
    max_value = max(rate_lst)
    max_index = rate_lst.index(max_value)

    company = comp_lst[max_index]
    zip_code = zip_lst[max_index]
    state = state_lst[max_index]

    return f'{company} ({zip_code}, {state}) - ${max_value}'

def find_min(comp_lst, zip_lst, state_lst, rate_lst):
    min_value = min(rate_lst)
    min_index = rate_lst.index(min_value)

    company = comp_lst[min_index]
    zip_code = zip_lst[min_index]
    state = state_lst[min_index]

    return f'{company} ({zip_code}, {state}) - ${min_value}'

def main():
    input_file = input('Please enter the data file: ')

    zip_list = []
    company_list = []
    state_list = []
    comm_rate_list = []

    with open(input_file, 'r') as data_file:
        row_count = 0
        for row in data_file:
            if row_count > 0:
                clean_line = row.strip()
                parts = clean_line.split(',')
                
                zip_list.append(parts[0])
                company_list.append(parts[2])
                state_list.append(parts[3])
                comm_rate_list.append(float(parts[6]))

            row_count += 1

    print(f'\nThe average commercial rate is: {find_average(comm_rate_list)}\n')
    print('The highest rate is:')
    print(find_max(company_list, zip_list, state_list, comm_rate_list))
    print('\nThe lowest rate is:')
    print(find_min(company_list, zip_list, state_list, comm_rate_list))

if __name__ == '__main__':
    main()