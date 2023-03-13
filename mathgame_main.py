import mathgame_base as MB
import datetime as dt
import sys
#----------------------------------------------------
#Gamemodes
#----------------------------------------------------
def end_game(prefix='',end_mensage = f' Your score is'):
  MB.front_end.print(prefix + end_mensage + f' [yellow]{MB.score}[/yellow]!')
  MB.front_end.print('''do you want to play again?\n
  1 - [green]Yes[/green]
  2 - [red]No''')
  play_again = input()
  if play_again == '1':
    MB.gamemode = None
    MB.skip_line(50)
  else:
    sys.exit()

def set_difficult():
  MB.front_end.print('Which difficult do you want?')
  MB.front_end.print('''
  1 - [green]easy[/green]
  2 - [yellow]medium[/yellow]
  3 - [bright_red]Hard[/bright_red]
  4 - [bright_red]Hardcore[/bright_red]
  ''')
  
  difficult = input()
  match difficult:
    case "1":
      pass
    case '2':
      MB.number_difficult += 10
    case '3':
      MB.number_difficult +=25
    case '4':
      MB.number_difficult += 50

#----------------------------------------------------
#Gamemodes
#----------------------------------------------------

#Classic
def classic():
  MB.chance = 3
  while MB.chance > 0:
    MB.random_basic_operation()

  end_game('you loose,')

#Convertion


#----------------------------------------------------
#Gamemodes
#----------------------------------------------------

modes = {
  '1':classic,
  }

#----------------------------------------------------
#Set Game mod
#----------------------------------------------------

def set_game_mode():
  MB.front_end.print('[green]INSERT GAME MODE',style='i u')
  for mode in modes:
    MB.front_end.print(f'[yellow]{mode}[/yellow] - {modes[mode].__name__}')

  try:
    chosed_mode = input('insert game mode number: ')
    set_difficult()
    MB.skip_line()
    modes[chosed_mode]()
  except ValueError:
    print('cannot recognize command')
  except KeyError:
    print('cannot recognize command')


while MB.gamemode == None:
  set_game_mode()