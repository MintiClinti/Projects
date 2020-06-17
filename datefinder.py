day_code = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday',
            0: 'Sunday'}
month_code = {'January': 6, 'February': 2, 'March': 2, 'April': 5, 'May': 0, 'June': 3, 'July': 5, 'August': 1,
              'September': 4, 'October': 6, 'November': 2, 'December': 4}
leap_code = {'January': 5, 'February': 1, 'March': 2, 'April': 5, 'May': 0, 'June': 3, 'July': 5, 'August': 1,
             'September': 4, 'October': 6, 'November': 2, 'December': 4}

month = input('Enter a month. ')
date = int(input('Enter a day. '))
year = input('Enter a year. ')

month_num = int(month_code[month])
leap_num = int(leap_code[month])
year_dig = int(year[2:])
year_mult = ((year_dig // 4) + year_dig) // 7
year_code = ((year_dig // 4) + year_dig) - year_mult * 7

if int(year) % 4 == 0:
    final_sum = leap_num + date + year_code
    answer_mult = int(final_sum) // 7
    answer = final_sum - answer_mult * 7
    print(day_code[answer])
else:
    final_sum = month_num + date + year_code
    answer_mult = int(final_sum) // 7
    answer = final_sum - answer_mult * 7
    print(day_code[answer])



