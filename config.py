import env


class Config:

    __slots__ = ['target_dir']

    def __init__(self):
        self.target_dir = env.target_dirs

