from .base import MentorBase
from .gentani import Gentani
from .yuki import Yuki
from .akari import Akari
from .teru import Teru

MENTORS = {
    0: MentorBase,
    1: Gentani,
    2: Yuki,
    3: Akari,
    4: Teru
}
