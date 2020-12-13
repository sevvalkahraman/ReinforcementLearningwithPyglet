import pyglet
from pyglet.window import key
from pyglet.window import FPSDisplay

import random
from random import randint, choice

from Agent import Agent
from Config import EnvironmentConfig
from Config import RLConfig
from Window import Window
window = Window()


game = False
episode = False
hitObstacle =False
actionList = [0,1,2,3]
episodes = 0
steps = 0
step_list = []
qtable = []
rewardList = []
environmentObjects = []
flashTime = 1

agent = Agent()

def initialoints():
    global gtable
    for i in range (10):
       qtable.append([])
       for j in range(10):
           qtable[i].append([])
           for k in range(4):
               qtable[i][j].append(0)

def print_qtable():
   global gtable               
   print(qtable)

def setRewards():
    global rewardList
    for i in range (10):
       rewardList.append([])
       for j in range(10):
           rewardList[i].append(0)

    for i in range (10):
       for j in range(10):
           if i == 6 and j == 9 :
            rewardList[i][j] = 100
           elif i == 4 or i == 5 and j == 9:
            rewardList[i][j] = -50
           elif i == 5 and j == 8:
            rewardList[i][j] = -50
           elif i == 5 and j == 7:
            rewardList[i][j] = -50
           elif i == 2 and j == 7:
            rewardList[i][j] = -50
           elif i == 2 and j == 2 :
            rewardList[i][j] = -50
           elif i == 0 and j == 9 :
            rewardList[i][j] = -50
           elif i == 1 and j == 9 :
            rewardList[i][j]= -50

def find_actions ():
    list = []
    if agent.x == 0 :
        if agent.y == 0 :
            list = [1,2]
        elif agent.y == 9 :
            list = [1,3]
        else :
            list = [1,2,3]
    elif agent.y == 9 :
        if agent.x == 0 :
            list = [1,2]
        elif agent.x == 9 :
            list = [0,3]
        else :
            list = [0,1,3]
    else:
        list = [0,1,2,3]
    return list


def preload():
    global preloaded, game, episode
    game = True
    episode = True
    initialoints()
    setRewards()
    preloaded = True

@window.window.event
def on_draw():
    window.window.clear()
    if not preloaded:
        preload()
    for bg in window.bacgroundList:
        bg.draw()
    if game:
        window.mainBatch.draw()
    else :
        screen_shake()
        intro_text.draw() 

def agent_move(action, dt):
    global game, steps, episode, hitObstacle, agent
    if action == 0 and window.player.x - 50 >= 0 :
        window.player.x = window.player.x - 50
        agent.x = agent.x - 1
    elif action == 1 and window.player.x + 50 <= 450 :
        window.player.x = window.player.x + 50
        agent.x = agent.x + 1
    elif action == 2 and window.player.y + 50 <= 450 :
        window.player.y = window.player.y + 50
        agent.y = agent.y + 1
    elif action == 3 and window.player.y - 50 >= 0 :
        window.player.y = window.player.y - 50
        agent.y = agent.y - 1

    steps = steps + 1

    for obstacle in window.obstacleList:
        if window.player.x == obstacle.x and  window.player.y  == obstacle.y :
            hitObstacle = True

    if window.player.x == window.finish.x and  window.player.y  == window.finish.y :
        episode = False #episode is finished          

shakeTime = 0
def screen_shake():
    global shakeTime
    shakeTime -= 0.1
    x = randint(-5, 5)
    if shakeTime <= 0:
        intro_text.x = intro_text.x  + x
        shakeTime += 0.11
    elif shakeTime >= 0:
        intro_text.x = 250

def update_flash():
    global flashTime, hitObstacle
    flashTime -= 0.4
    window.player.color = (255, 0, 0)
    if flashTime <= 0:
        window.player.color = (255, 255, 255)
        flashTime = 1
        hitObstacle = False

def get_max_action_point():
    global qtable
    list = []
    listmax = []
    for i in range(4):
        list.append(qtable[agent.x][agent.y][i])
    for i in range(4):
        if list[i] == max(list) :
            listmax.append(i)
    return random.choice(listmax)

new_action = True
def update(dt):
    global episode, steps, episodes, qtable, new_action
    if episode == False :
        step_list.append(steps)
        steps = 0
        episodes = episodes + 1
        print(episodes)
        window.episodeTextVar.text = str(episodes)
        window.player.x = 0
        window.player.y = 0
        agent.x = 0
        agent.y = 0
        print_qtable()
        episode = True
    if hitObstacle :
        update_flash()
    if game and new_action:
        new_action = False
        if(qtable[agent.x][agent.y][0] == 0) and (qtable[agent.x][agent.y][1] == 0) and (qtable[agent.x][agent.y][2] == 0) and (qtable[agent.x][agent.y][3] == 0):
            print(find_actions())
            action = random.choice(find_actions())
        else: 
            random_number = random.uniform(0, 1)
            if random_number < RLConfig.EPSILON:
                print(find_actions())
                action = random.choice(find_actions())
            else:
                action = get_max_action_point()
        prevX = agent.x
        prevY = agent.y
        agent_move(action, dt)
        qtable[prevX][prevY][action] = qtable[prevX][prevY][action] + RLConfig.ALPHA * (rewardList[agent.x][agent.x] + (RLConfig.DISCOUNTFACTOR * qtable[agent.x][agent.y][get_max_action_point()]) - qtable[prevX][prevY][action])
        window.stepTextVar.text = str(steps) 
        new_action = True

if __name__ == "__main__":
    preload()
    pyglet.clock.schedule_interval(update, 5/60)
    pyglet.app.run()