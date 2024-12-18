#abstract factory
class MazeFactory:
    def create_room(self):
        pass
    def create_wall(self):
        pass
    def create_enemy(self):
        pass

class Room:
    def describe(self):
        pass
class Wall:
    def describe(self):
        pass
class Enemy:
    def describe(self):
        pass

#factories
class WinterMazeFactory(MazeFactory):
    def create_room(self):
        return WinterRoom()
    def create_wall(self):
        return WinterWall()
    def create_enemy(self):
        return WinterEnemy()

class DesertMazeFactory(MazeFactory):
    def create_room(self):
        return DesertRoom()
    def create_wall(self):
        return DesertWall()
    def create_enemy(self):
        return DesertEnemy()

class JungleMazeFactory(MazeFactory):
    def create_room(self):
        return JungleRoom()
    def create_wall(self):
        return JungleWall()
    def create_enemy(self):
        return JungleEnemy()


class WinterRoom(Room):
    def describe(self):
        return "Its cold here"
class WinterWall(Wall):
    def describe(self):
        return "Ice walls"
class WinterEnemy(Enemy):
    def describe(self):
        return "Frozen zombie"

class DesertRoom(Room):
    def describe(self):
        return "Its warm here"
class DesertWall(Wall):
    def describe(self):
        return "Sand walls"
class DesertEnemy(Enemy):
    def describe(self):
        return "Roasted zombie"


class JungleRoom(Room):
    def describe(self):
        return "Its wet here"
class JungleWall(Wall):
    def describe(self):
        return "Stone walls with lianas"
class JungleEnemy(Enemy):
    def describe(self):
        return "Wild zombie"
    

class MazeGame:
    def __init__(self, factory):
        self.room = factory.create_room()
        self.wall = factory.create_wall()
        self.enemy = factory.create_enemy()

    def play(self):
        print(self.room.describe())
        print(self.wall.describe())
        print(self.enemy.describe())


def main():
    theme = input("SELECT MAZE ROOM (winter/desert/jungle): ")

    if theme == "winter":
        factory = WinterMazeFactory()
    elif theme == "desert":
        factory = DesertMazeFactory()
    elif theme == "jungle":
        factory = JungleMazeFactory()
    else:
        print("Cant find this room")
        return

    game = MazeGame(factory)
    game.play()

if __name__ == "__main__":
    main()