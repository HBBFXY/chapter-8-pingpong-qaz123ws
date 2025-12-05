import random

def simulate_game(prob_a):
    """模拟单局比赛，返回A的得分、B的得分"""
    score_a = 0
    score_b = 0
    while True:
        # 按概率prob_a让A得分，否则B得分
        if random.random() < prob_a:
            score_a += 1
        else:
            score_b += 1
        
        # 判断局胜负
        if (score_a >= 11 or score_b >= 11) and abs(score_a - score_b) >= 2:
            return score_a, score_b

def simulate_match(prob_a, n_games=3):
    """模拟n局n胜制比赛，返回A获胜的局数"""
    win_a = 0
    for _ in range(n_games):
        a, b = simulate_game(prob_a)
        if a > b:
            win_a += 1
    return win_a

# 模拟多场比赛，分析规律
def analysis(prob_a, n_matches=10000):
    a_win_match = 0
    for _ in range(n_matches):
        if simulate_match(prob_a, 5) >= 3:  # 五局三胜
            a_win_match += 1
    return a_win_match / n_matches

# 测试：A选手每球胜率0.55，模拟1万场五局三胜
print(f"A选手获胜概率：{analysis(0.55)}")
