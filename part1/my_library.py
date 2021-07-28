def build_user_profile(first_name, last_name, **user_info):
    user_info["f_name"] = first_name
    user_info["l_name"] = last_name
    return user_info

def baloons_order(*colors):
    print("You want baloon of each of these colors: ")
    for color in colors:
        print(color)

def complete_tasks(all_tasks, all_finished_tasks):
    while all_tasks:
        finished_task = all_tasks.pop()
        all_finished_tasks.append(finished_task)