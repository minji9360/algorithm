while True:
    try:
        print(input())
    except EOFError:
        break

# for문으로 100문장 받을 수 있도록 돌리면 런타임 에러가 발생한다.
# 예전에도 했었는데 혹시나 싶어 도전했다가 틀렸다.
# 그리고 파이참에서 테스트한 코드 긁어다가 썼는데, 이전 문제 코드여서 계속 틀렸다.
# 어쩐지 코드에 문제가 없어 보였는데 이상하다 했더니.. 문제를 잘 읽자