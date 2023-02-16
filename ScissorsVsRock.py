import random

# задаем количество повторений эксперимента
numOfExperiments = 100000

# задаем сколько поинтов будет получать и снимать игрокам за победу/поражение (без минуса)
ifAWin = 1
ifALose = 2
ifBWin = 1
ifBLose = 1
##loseAPointByMatch = 0 
##loseBPointByMatch = 0 

# словарь для подсчета побед каждого участника по всем экспериментам
totalMatchScores = {'a': 0, 'b': 0}

# словарь для подсчета побед каждого участника по эксперименту
winsInExperiments = {'a': 0, 'b': 0}

with open("input.txt", "w") as f:    
# цикл для повторения эксперимента
  for j in range(numOfExperiments):

    # создаем словарь с именами участников и их текущими счетами
    scores = {'a': 0, 'b': 0}

    # задаем количество матчей в серии. По дефолту Bo7 
    numMatches = 7

    # цикл для проведения матчей
    for i in range(numMatches):

      #снимаем поинты за каждый ход, если необходимо
        ##scores["a"] -= loseAPointByMatch
        ##scores["b"] -= loseBPointByMatch
        ##totalMatchScores['a'] -= loseAPointByMatch
        ##totalMatchScores['b'] -= loseBPointByMatch
      
        # выбираем случайного победителя из списка
        winner = random.choice(list(scores.keys()))
        
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
    f.write(f"\nЭксперимент {j+1} завершен!\n")
    f.write("\nСчет:")

      
    for participant in scores:
        f.write(participant + str(scores[participant]) + str(":"))
    f.write("\n")
# выводим итоговый счет по всем матчам      
  f.write("\nИтоговый счет по всем матчам:")
  f.write(" A: "+ str(totalMatchScores['a']) + str(" B: ") + str(totalMatchScores['b']))

  # выводим итоговый счет по всем экспериментам     
  f.write("\nИтоговый счет по всем экспериментам: ")
  f.write(str(" A: ")+ str(winsInExperiments['a']) + str(" B: ") + str(winsInExperiments['b']))
  # выводим победителя
  if winsInExperiments['a'] > winsInExperiments['b']:
    f.write("\nПобедитель: A ")
  
  elif winsInExperiments['b'] > winsInExperiments['a']:
     f.write("\nПобедитель: B ")
    
  else:
      f.write("\nНичья")
  f.close 
