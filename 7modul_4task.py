# Форматирование строк
team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = score_1 + score_2
time_avg = round(((team1_time + team2_time) / tasks_total), 1)
if team1_time / score_1 > team2_time / score_2:
    challenge_result = 'победа команды Волшебники данных'
elif team1_time / score_1 < team2_time / score_2:
    challenge_result = 'победа команды Мастера кода'
else:
    challenge_result = 'ничья'


# Использование %
print('В команде Мастера кода участников: %s !' % team1_num)
print('В команде Волшебники данных участников: %s !' % team2_num)
print('Итого сегодня в командах участников: %s%s%s !' % (team1_num, ' и ', team2_num))

# Использование format()
print('Команда Мастера кода решила задач: {} !'.format(score_1))
print('Команда Волшебники данных решила задач: {} !'.format(score_2))
print('Мастера кода решили задачи за {} с !'.format(team1_time))
print('Волшебники данных решили задачи за {} с !'.format(team2_time))

# Использование f-строк:
print(f'Команды решили {score_1} и {score_2} задач.')
print(f'Результат битвы: {challenge_result}!')
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.')