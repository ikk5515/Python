def print_models(unprinted_design, completed_models):    # 지역변수
    if isinstance(unprinted_design, list) and isinstance(completed_models, list):
        while unprinted_design:
            curren_design = unprinted_design.pop()
            print(f"printing.......: {curren_design}")
            completed_models.append(curren_design)
    else:
        print("매개변수는 list만 넣어주세요")


def show_completed_models(completed_models):
    print("The following models have been printed: ")
    for cm in completed_models:
        print(cm)


unprinted_design = ['phone case', 'robot pendant']    # 전역변수
completed_moedels = []

print_models(unprinted_design, completed_moedels)
show_completed_models(completed_moedels)

print_models("테스트", "[테스트1, 테스트2]")
