from datetime import datetime

class Task:
    def __init__(self, task_id, start_dt, end_dt, title, text):
        self.task_id = task_id
        self.start_dt = start_dt
        self.end_dt = end_dt
        self.title = title
        self.text = text

class User:
    # class_id, seiseki は後回し
    def __init__(self, user_id, name, password, grade, gakka):
        self.user_id = user_id
        self.name = name
        self.password = password
        self.grade = grade
        self.gakka = gakka
        self.tasks = []
        
    def regist_task(self, task):
        self.tasks.append(task)
    
    def merge_user_class_tasks(self, classroom):
        for task in classroom.tasks:
            self.tasks.append(task)
            
    def get_tasks(self):
        return self.tasks

    def get_future_tasks(self, from_dt):
        relevant_tasks = []
        for task in self.tasks:
            if task.start_dt >= from_dt:
                relevant_tasks.append(task)
        return relevant_tasks

class ClassRoom:
    def __init__(self, class_id, grade, gakka):
        self.class_id = class_id
        self.grade = grade
        self.gakka = gakka
        self.tasks = []
        
    def regist_task(self, task):
        self.tasks.append(task)

def format_task(task):
    s = "{}月{}日 {:02}:{:02} {}".format(task.start_dt.month,
                                    task.start_dt.day,
                                    task.start_dt.hour,
                                    task.start_dt.minute,
                                    task.title)
    return s
    
def main():
    user_task1 = Task(task_id=1, start_dt=datetime(2023, 1, 1, 10, 0),
                                end_dt=datetime(2023, 1, 1, 12, 0),
                                title="初詣",
                                text="厳島神社へ集合")

    user_task2 = Task(task_id=2, start_dt=datetime(2023, 4, 1, 20, 0),
                                end_dt=datetime(2023, 4, 1, 23, 59),
                                title="エイプリルフール",
                                text="害のない嘘を呟く")

    class_task1 = Task(task_id=1, start_dt=datetime(2023, 6, 1, 8, 50),
                                end_dt=datetime(2023, 6, 1, 10, 20),
                                title="アルゴリズム",
                                text="")
    class_task2 = Task(task_id=2, start_dt=datetime(2023, 6, 1, 10, 30),
                                end_dt=datetime(2023, 6, 1, 12, 0),
                                title="設計技法",
                                text="")
    class_task3 = Task(task_id=3, start_dt=datetime(2023, 6, 8, 8, 50),
                                end_dt=datetime(2023, 6, 8, 10, 20),
                                title="アルゴリズム",
                                text="")
    class_task4 = Task(task_id=4, start_dt=datetime(2023, 6, 8, 10, 30),
                                end_dt=datetime(2023, 6, 8, 12, 0),
                                title="設計技法",
                                text="")

    # ユーザの生成 ＆ タスクの登録
    # (メモ) DB から引っ張ってくる時点でユーザID(user_id)を特定する
    user = User(user_id=1, name="MUTO", password="password", grade=3, gakka="S")
    user.regist_task(user_task1)
    user.regist_task(user_task2)

    # クラスルームの生成 ＆ タスクの登録
    # (メモ) DB から引っ張ってくる時点でクラス名(class_id)を特定する
    classroom = ClassRoom(class_id=1, grade=3, gakka="S")
    classroom.regist_task(class_task1)
    classroom.regist_task(class_task2)
    classroom.regist_task(class_task3)
    classroom.regist_task(class_task4)

    # ユーザのタスク／クラスルームのタスクの合体
    user.merge_user_class_tasks(classroom)
    
    # 過去も含めて，全てのタスクを列挙
    print("=== {}'s tasks ===".format(user.name))
    for task in user.get_tasks():
        print(format_task(task))

    # 指定した日時以降のタスクを列挙
    print("=== {}'s future tasks ===".format(user.name))
    for task in user.get_future_tasks(datetime(2023, 6, 1, 0, 0)):
        print(format_task(task))

if __name__ == '__main__':
    main()
