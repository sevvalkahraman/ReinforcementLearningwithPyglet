import pyglet
from pyglet.window import key
from pyglet.window import FPSDisplay
from Config import EnvironmentConfig
from Config import RLConfig


class Window :
    def __init__(self):
        self.window = pyglet.window.Window(width=700, height=500, caption="Learning Mario", resizable=False)
        self.window.set_location(500, 100)
        self.fpsDisplay = FPSDisplay(self.window)
        self.fpsDisplay.label.font_size = 50
        self.mainBatch = pyglet.graphics.Batch()
        self.bacgroundList = []
        self.obstacleList =[]
        self.setIcons()
        self.setBackground()
        self.readEnvironment() #TODO:
        self.setEpisodeText()
        self.setEpisodeTextVar()
        self.setStepText()
        self.setStepTextVar()
        self.setRLVar()


    def setIcons(self):
        self.gridBackground = pyglet.image.load(EnvironmentConfig.BACKGROUND_IMAGE)
        self.playerImage = pyglet.image.load(EnvironmentConfig.PLAYER_IMAGE) 
        self.finishImage = pyglet.image.load(EnvironmentConfig.FINISH_IMAGE) 
        self.wallImage = pyglet.image.load(EnvironmentConfig.WALL_IMAGE)
        self.fireImage = pyglet.image.load(EnvironmentConfig.FIRE_IMAGE)

    def setBackground(self):
        for i in range(2):
            self.bacgroundList.append(pyglet.sprite.Sprite(self.gridBackground, x=0, y=i*500))

    def setPlayer(self, x, y):
        self.player = pyglet.sprite.Sprite(self.playerImage, x=x, y=y, batch=self.mainBatch)

    def setfinishImage(self, x, y):
        self.finish = pyglet.sprite.Sprite(self.finishImage, x=x, y=y, batch=self.mainBatch)

    def setWallImage(self,x,y):
        self.setObstacle(self.wallImage, x,y)

    def setFireImage(self,x,y):
        self.setObstacle(self.fireImage, x,y)

    def setObstacle(self, image, x, y):
        obstacleObject = pyglet.sprite.Sprite(image, x=x, y=y, batch=self.mainBatch)
        self.obstacleList.append(obstacleObject)

    def setEpisodeText(self):
        self.episodeText =  pyglet.text.Label("Episode :", x=560 , y=450, batch=self.mainBatch) 
        self.episodeText.anchor_x = "center"
        self.episodeText.anchor_y = "center"
        self.episodeText.italic = True
        self.episodeText.bold = True
        self.episodeText.font_size = 10
        self.episodeText.color = (120, 200, 150, 255)

    def setEpisodeTextVar(self):
        self.episodeTextVar =  pyglet.text.Label(str(0), x=600 , y=450, batch=self.mainBatch) 
        self.episodeTextVar.anchor_x = "center"
        self.episodeTextVar.anchor_y = "center"
        self.episodeTextVar.italic = True
        self.episodeTextVar.bold = True
        self.episodeTextVar.font_size = 10
        self.episodeTextVar.color = (120, 200, 150, 255)

    def setStepText(self):
        stepText =  pyglet.text.Label("Steps :", x=550 , y=430, batch=self.mainBatch) 
        stepText.anchor_x = "center"
        stepText.anchor_y = "center"
        stepText.italic = True
        stepText.bold = True
        stepText.font_size = 10
        stepText.color = (120, 200, 150, 255)

    def setStepTextVar(self):
        self.stepTextVar =  pyglet.text.Label(str(0), x=590 , y=430, batch=self.mainBatch) 
        self.stepTextVar.anchor_x = "center"
        self.stepTextVar.anchor_y = "center"
        self.stepTextVar.italic = True
        self.stepTextVar.bold = True
        self.stepTextVar.font_size = 10
        self.stepTextVar.color = (120, 200, 150, 255)

    def setRLVar(self):
        learning_rate_text =  pyglet.text.Label("Learning rate :", x=575 , y=410, batch=self.mainBatch) 
        learning_rate_text.anchor_x = "center"
        learning_rate_text.anchor_y = "center"
        learning_rate_text.italic = True
        learning_rate_text.bold = True
        learning_rate_text.font_size = 10
        learning_rate_text.color = (120, 200, 150, 255)

        learning_rate_text_var =  pyglet.text.Label(str(RLConfig.ALPHA), x=640 , y=410, batch=self.mainBatch) 
        learning_rate_text_var.anchor_x = "center"
        learning_rate_text_var.anchor_y = "center"
        learning_rate_text_var.italic = True
        learning_rate_text_var.bold = True
        learning_rate_text_var.font_size = 10
        learning_rate_text_var.color = (120, 200, 150, 255)

        discountfactor_text =  pyglet.text.Label("Discount factor:", x=580 , y=390, batch=self.mainBatch) 
        discountfactor_text.anchor_x = "center"
        discountfactor_text.anchor_y = "center"
        discountfactor_text.italic = True
        discountfactor_text.bold = True
        discountfactor_text.font_size = 10
        discountfactor_text.color = (120, 200, 150, 255)

        discountfactor_text_var =  pyglet.text.Label(str(RLConfig.DISCOUNTFACTOR), x=655 , y=390, batch=self.mainBatch) 
        discountfactor_text_var.anchor_x = "center"
        discountfactor_text_var.anchor_y = "center"
        discountfactor_text_var.italic = True
        discountfactor_text_var.bold = True
        discountfactor_text_var.font_size = 10
        discountfactor_text_var.color = (120, 200, 150, 255)

        epsilon_text =  pyglet.text.Label("Epsilon:", x=552 , y=370, batch=self.mainBatch) 
        epsilon_text.anchor_x = "center"
        epsilon_text.anchor_y = "center"
        epsilon_text.italic = True
        epsilon_text.bold = True
        epsilon_text.font_size = 10
        epsilon_text.color = (120, 200, 150, 255)

        epsilon_text_var =  pyglet.text.Label(str(RLConfig.EPSILON), x=600 , y=370, batch=self.mainBatch) 
        epsilon_text_var.anchor_x = "center"
        epsilon_text_var.anchor_y = "center"
        epsilon_text_var.italic = True
        epsilon_text_var.bold = True
        epsilon_text_var.font_size = 10
        epsilon_text_var.color = (120, 200, 150, 255)


    def readEnvironment(self):
        filename = EnvironmentConfig.FILENAME
        with open(filename) as f:
            content = f.read().splitlines()

        content.reverse()
        print(content)
        for i in range(EnvironmentConfig.SIZE_X):
            for j in range(EnvironmentConfig.SIZE_Y):
                if(content[i][j] == EnvironmentConfig.PLAYER_CHAR) :
                    self.setPlayer(EnvironmentConfig.BOX_SIZE*j, EnvironmentConfig.BOX_SIZE*i)
                elif(content[i][j] == EnvironmentConfig.FINISH_CHAR) :
                    self.setfinishImage(EnvironmentConfig.BOX_SIZE*j, EnvironmentConfig.BOX_SIZE*i)
                elif(content[i][j] == EnvironmentConfig.WALL_CHAR) :
                    self.setWallImage(EnvironmentConfig.BOX_SIZE*j, EnvironmentConfig.BOX_SIZE*i)
                elif(content[i][j] == EnvironmentConfig.FIRE_CHAR) :
                    self.setFireImage(EnvironmentConfig.BOX_SIZE*j, EnvironmentConfig.BOX_SIZE*i)

                


            
