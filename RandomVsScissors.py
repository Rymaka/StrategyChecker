import random

# задаем количество повторений эксперимента
numOfExperiments = 10

# задаем сколько поинтов будет получать и снимать игрокам за победу/поражение (без минуса)
ifAWin = 0
ifALose = 0
ifBWin = 0
ifBLose = 0

draw = 0

# словарь для подсчета побед каждого участника по всем экспериментам
totalMatchScores = {'a': 0, 'b': 0}

# словарь для подсчета побед каждого участника по эксперименту
winsInExperiments = {'a': 0, 'b': 0}
with open("input.txt", "w") as f, open('median.txt', "w") as m:   
# цикл для повторения эксперимента
  for j in range(numOfExperiments):

    # создаем словарь с именами участников и их текущими счетами
    scores = {'a': 0, 'b': 0}
    
    # задаем количество матчей в серии. По дефолту Bo7 
    numMatches = 7

    # цикл для проведения матчей
    for i in range(numMatches):
     
        # выбираем случайного победителя из списка
        winner = random.choice(list(scores.keys()))
        num = random.choice([1.5, 1])
        if num == 1.5:
          f.write(str("\nA is Scissors\n"))
          ifAWin = 1
          ifALose = num
          ifBWin = 1
          ifBLose = 1.5
        else:
          f.write(str('\nA is Rock\n'))
          ifAWin = num
          ifALose = num
          ifBWin = 1
          ifBLose = 1.5
          
        # добавляем 1 очко победителю и снимаем 1 очко с проигравшего
        if winner == "a":
          scores['a'] += ifAWin 
          totalMatchScores['a'] += ifAWin          
          
          scores['b'] -= ifBLose
          totalMatchScores['b'] -= ifBLose
        else:
          scores['a'] -= ifALose 
          totalMatchScores['a'] -= ifALose
          
          scores['b'] += ifBWin
          totalMatchScores['b'] += ifBWin
        # выводим результаты текущего матча
        f.write(f"Эксперимент {j+1}: Матч {i+1}: Победитель - {winner}\n")

        # проверяем, достигнута ли победа в серии
        if scores['a'] > numMatches/2+1:
           break
        if scores['b'] > numMatches/2+1:
           break

    
    
    if scores['a'] > scores['b']:
      winsInExperiments['a'] += 1  
    if scores['b'] > scores['a']:
      winsInExperiments['b'] += 1  
    # выводим итоговый счет на экран
    ifAWin = 0
    ifALose = 0
    ifBWin = 0
    ifBLose = 0  
    f.write(f"\nЭксперимент {j+1} завершен!\n")
    f.write("\nСчет:")
    m.write(str(scores['a'])+str(";")+str(scores['b']) + str(';'))  
    for participant in scores:
        f.write(participant + str(scores[participant]) + str(":"))
    if scores['a'] == scores['b']:
      draw += 1
    f.write("\n")
# выводим итоговый счет по всем матчам      
  f.write("\nИтоговый счет по всем матчам:")
  f.write(" A: "+ str(totalMatchScores['a']) + str(" B: ") + str(totalMatchScores['b']))

  # выводим итоговый счет по всем экспериментам     
  f.write("\nИтоговый счет по всем экспериментам: ")
  f.write(str(" A: ")+ str(winsInExperiments['a']) + str(" B: ") + str(winsInExperiments['b'])+ str(" Ничьих ") + str(draw))
  # выводим победителя
  if winsInExperiments['a'] > winsInExperiments['b']:
    f.write("\nПобедитель: A ")
  
  elif winsInExperiments['b'] > winsInExperiments['a']:
     f.write("\nПобедитель: B ")
    
  else:
      f.write("\nНичья")
  f.close 
  m.close
