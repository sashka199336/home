import time


class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, login: str, password: str) -> None:
        for user in self.users:
            if login == user.nickname and password == user.password:
                self.current_user = user

    def register(self, nickname: str, password: str, age: int) -> None:
        for user in self.users:
            if nickname in user.nickname:
                print(f"Пользователь {nickname} уже есть")
                break
        else:
            user = User(nickname, password, age)
            self.users.append(user)
            self.log_out()
            self.log_in(user.nickname, user.password)

    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for movie in args:
            self.videos.append(movie)

    def get_videos(self, text: str) -> list:
        list_movie = []
        for video in self.videos:
            if text.upper() in video.title.upper():
                list_movie.append(video.title)
        return list_movie

    def watch_video(self, movie: str) -> None:
        if self.current_user and self.current_user.age < 18:
            print('Тебе нет 18, вали отсюда')
        elif self.current_user:
            for video in self.videos:
                if movie in video.title:
                    for i in range(1, 11):
                        print(i, end=' ')
                        time.sleep(1)
                    print('Конец')
        else:
            print('Войди в аккаунт')

    def __str__(self):
        return f"{self.videos}"


class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f"{self.title}"


class User:
    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = password
        self.age = age

    def __str__(self):
        return f'{self.nickname}'

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __hash__(self):
        return hash(self.password)


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Как не платить налоги', 154)
    v2 = Video('Как правельно входить в хату', 62, adult_mode=True)


    ur.add(v1, v2)


    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))


    ur.watch_video('Как найти себе бабу?')
    ur.register('debil', 'umnyi', 12)
    ur.watch_video('Как найти себе бабу?')
    ur.register('tu[i', 'butro', 25)
    ur.watch_video('Как найти себе бабу?')


    ur.register('debil', 'umnyi', 55)
    print(ur.current_user)


    ur.watch_video('хАЧУ МНОГА ДЕНЕХ')
