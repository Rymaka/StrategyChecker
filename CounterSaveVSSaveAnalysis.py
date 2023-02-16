import random

# задаем количество повторений эксперимента
numOfExperiments = 100000

# задаем сколько поинтов будет получать и снимать игрокам за победу/поражение (без минуса)
ifAWin = 0
ifALose = 0
ifBWin = 0
ifBLose = 0
scissors = False
confidence = True
scissorsB = False


# словарь для подсчета побед каждого участника по всем экспериментам
totalMatchScores = {'a': 0, 'b': 0}

# словарь для подсчета побед каждого участника по эксперименту
winsInExperiments = {'a': 0, 'b': 0}
draw = 0

with open("input.txt", "w") as f:    
# цикл для повторения эксперимента
  for j in range(numOfExperiments):

    # создаем словарь с именами участников и их текущими счетами
    scores = {'a': 0, 'b': 0}

    # задаем количество матчей в серии. По дефолту Bo7 
    numMatches = 7

    # цикл для проведения матчей
    for i in range(numMatches):


      # игрок a специально проигрывает
        if i+1 < 2:
          winner = 'b'
        else:                
          winner = random.choice(list(scores.keys()))
        
        # добавляем очки победителю и снимаем очки с проигравшего
        if winner == "a":
          if i+1 == 2:
            f.write(str("\nScissors A \n"))
            scissorsA = True
            ifAWin = 1
            if scissorsB:
              ifBLose = 2
            else:
              ifBLose = 1
          else: 
            f.write(str(scissorsB))
            scissorsA = False
            if scissorsB:
              ifAWin = 1
              ifBlose = 2
            else:
              ifAWin = 0
              ifBLose = 0
          if i+1 >= 3:
            f.write(str("\nlost Confidence \n"))
            confidence = False    
            scissorsB = False
          if scissorsB:
            f.write(str("\nlost Confidence \n"))
            confidence = False    
            scissorsB = False
            
          scores['a'] += ifAWin 
          totalMatchScores['a'] += ifAWin          
          
          scores['b'] -= ifBLose
          totalMatchScores['b'] -= ifBLose

        else:
          f.write(str(scissorsB))
          if (i + 1 != 2):
            scissorsA = False
            if scissorsB:
              ifALose = 1
              ifBWin = 1
            else:
              ifALose = 0
              ifBWin = 0
          else:
            scissorsA = True
            ifALose = 2
          scores['a'] -= ifALose 
          totalMatchScores['a'] -= ifALose

          
          scores['b'] += ifBWin
          totalMatchScores['b'] += ifBWin
        if i+1 < 3 and confidence:
            f.write(str("\nScissors B \n"))
            scissorsB = True
            ifBWin = 1

   
        # выводим результаты текущего матча
        f.write(f"\nЭксперимент {j+1}: Матч {i+1}: Победитель - {winner}\n" + str("Счет: ") +str(scores["a"]) + str(scores["b"]) + str("\n"))
        if (scores["b"] == scores["a"]):
          f.write(str("\nНИЧЬЯ\n"))

        # проверяем, достигнута ли победа в серии
        if scores['a'] > numMatches/2+1:
           break
        if scores['b'] > numMatches/2+1:
           break



  
    scissorsA = False
    scissorsB = False
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
    if scores['a'] == scores['b']:
      draw += 1
    confidence = True
    scissors = False
# выводим итоговый счет по всем матчам      
  f.write("\nИтоговый счет по всем матчам:")
  f.write(" A: "+ str(totalMatchScores['a']) + str(" B: ") + str(totalMatchScores['b']) + str("\nНичьих ") + str(draw))

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
