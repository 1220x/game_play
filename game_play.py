import random
import time

while True:
    player_value = 0
    enemy_value = 0
    for i in range(3):
        player_life = random.randint(100,150)
        player_attack = random.randint(30,50)
        enemy_life = random.randint(100,150)
        enemy_attack = random.randint(30,50)
        print('-----现在是第 {} 局比拼-----'.format(i+1))
        time.sleep(1.5)
        print('【玩家】血量：{}'.format(player_life))
        print('【玩家】攻击值：{}'.format(player_attack))
        print('--------------------------')
        time.sleep(1.5)
        print('【敌人】血量：{}'.format(enemy_life))
        print('【敌人】攻击值：{}'.format(enemy_attack))
        print('--------------------------')
        time.sleep(1.5)

        while ( player_life > 0 and enemy_life > 0 ) :
            player_life -= enemy_attack
            enemy_life -= player_attack
            print('【敌人】发起了攻击，【玩家】剩余血量 {}'.format(player_life))
            print('【玩家】发起了攻击，【敌人】剩余血量 {}'.format(enemy_life))
            print('--------------------------')
            time.sleep(1.5)

        if player_life < 0 and enemy_life < 0:
            print('你和敌人同归于尽了！')
        elif player_life > 0 and enemy_life < 0:
            print('恭喜，你打败了敌人！')
            player_value += 1
        else:
            print('糟糕，你被敌人消灭了！')
            enemy_value += 1
        print('--------------------------')
        time.sleep(1.5)
    if player_value > enemy_value:
        print('恭喜你在本轮比拼中胜利！')
    elif player_value < enemy_value:
        print('很遗憾你在本轮比拼中失败！')
    else:
        print('你在本轮比拼中平局！')

    option = input('您还想再来一次吗？继续请输入yes,退出请输入其他：')
    if option != 'yes':
        break
