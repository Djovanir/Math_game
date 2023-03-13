import random as rd
import datetime as dt
from rich .console import Console

#----------------------------------------------------
#Setting Interface
#----------------------------------------------------
front_end = Console(color_system='standard',highlight=False)

#----------------------------------------------------
#Utils 
#----------------------------------------------------
def skip_line(lines_number=100):
  for i in range(lines_number):
    front_end.print('\n')

#----------------------------------------------------
#Defining chance and score 
#----------------------------------------------------
chance = 0
score = 0
number_difficult = 0 
gamemode = None

#----------------------------------------------------
#wrong_answer, correct answer and correction
#----------------------------------------------------
def correct_answer():
  global score
  front_end.print('[green]Correct Answer\n\n')
  score += 1

def wrong_answer():
  global chance
  front_end.print('[red]Wrong Answer\n\n')
  chance -= 1
  

def correction(number):
  answer = int(input())
  if number  == answer:
    correct_answer()
  else:
    wrong_answer()


def correction_timed(number,time):
  start = dt.datetime.now()
  answer = int(input())
  end = dt.datetime.now()
  conclusion_time = end - start
  if conclusion_time.seconds < time:
    if number  == answer:
      correct_answer()
    else:
      wrong_answer()
  else: 
    print('demorou demais para responder')
    print(conclusion_time)

#----------------------------------------------------
# Count Setup | Operation setup
#----------------------------------------------------
def print_account(x, y, signal):
  front_end.print(f'how much is ([bright_cyan]{x}[/bright_cyan]) [red]{signal}[/red] ([bright_cyan]{y}[/bright_cyan])')

def get_answer(number1,number2,operator):
  match operator:
    case '+': 
      answer = number1 + number2
      x,y = number1,number2

    case '-':
       answer = number1 - number2
       x,y = number1,number2

    case '*': 
      answer = number1 * number2
      x,y = number1,number2

    case '/':
      if number2 ==0:
        number2 += 1
      answer = number1*number2/number2
      x,y = number1*number2, number2

  return answer,x,y
    

#----------------------------------------------------
#Basic operations 
#----------------------------------------------------

def operation(operator='+',difficult_improve=1):
  global number_difficult
  number1 = rd.randint(-number_difficult,number_difficult)
  number2 = rd.randint(-number_difficult,number_difficult)
  answer,x,y = get_answer(number1,number2,operator)
  print_account(x,y,operator)
  correction(answer)
  number_difficult += difficult_improve


def random_basic_operation(improve=1):
  operators = ['+','-','*','/']
  operator = rd.choice(operators)
  operation(operator,improve)

#----------------------------------------------------
#Timed operation
#----------------------------------------------------
def timed_operation(operator='+',difficult_improve=1, time=10):
  global number_difficult
  number1 = rd.randint(-number_difficult,number_difficult)
  number2 = rd.randint(-number_difficult,number_difficult)
  answer,x,y = get_answer(number1,number2,operator)
  print_account(x,y,operator)
  correction_timed(answer,time)
  number_difficult += difficult_improve
