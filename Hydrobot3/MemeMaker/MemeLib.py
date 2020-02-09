from enum import Enum
from PIL import ImageFont
from MemeMaker.MemeModel import MemeImage, TextZone

class MemeImages(Enum):
    def __str__(self):
        return str(self.value)

    MeAlsoMe = MemeImage(
        "mealsome.png",
        [TextZone(
            pos=(60, 0),
            dimensions=(400, 300),
            font=ImageFont.truetype("arial.ttf", 24),
        ),
            TextZone(
            pos=(120, 100),
            dimensions=(350, 300),
            font=ImageFont.truetype("arial.ttf", 24),
        )]
    ),
    ItsRetarded = MemeImage(
        "itsretarded.png",
        [TextZone(
            pos=(253, 3),
            dimensions=(220, 100),
            font=ImageFont.truetype("arial.ttf", 20),
            centering=(False, True)
        )]
    ),
    Headache = MemeImage(
        "headache.png",
        [TextZone(
            pos=(250, 490),
            dimensions=(400, 50),
            font=ImageFont.truetype("impact.ttf", 54),
            centering=(True, False)
        )]
    ),
    ItsTime = MemeImage(
        "itstime.png",
        [TextZone(
            pos=(60, 50),
            dimensions=(200, 150),
            font=ImageFont.truetype("arial.ttf", 36),
            centering=(True, True)
        ),
        TextZone(
            pos=(95, 380),
            dimensions=(110, 75),
            font=ImageFont.truetype("arial.ttf", 24),
            centering=(True, True)
        )]
    ),
    ClassNote = MemeImage(
        "classnote.png",
        [TextZone(
            pos=(585, 545),
            dimensions=(175, 140),
            angle=30,
            font=ImageFont.truetype("arial.ttf", 24),
            centering=(True, True)
        )]
    ),
    FirstWord = MemeImage(
        "firstword.png",
        [TextZone(
            pos=(100, 30),
            dimensions=(500, 50),
            font=ImageFont.truetype("comic.ttf", 60),
        ),
        TextZone(
            pos=(100, 485),
            dimensions=(500, 200),
            font=ImageFont.truetype("comic.ttf", 60),
            centering=(False, True)
        )],
    ),
    NutButton = MemeImage(
        "nutbutton.jpg",
        [TextZone(
            pos=(133, 300),
            dimensions=(175, 100),
            angle=10,
            font=ImageFont.truetype("arial.ttf", 56),
            centering=(False, True)
        )]
    ),
    SwuUok = MemeImage(
        "swu_uok.png",
        [TextZone(
            pos=(20,22),
            dimensions=(220, 220),
            font=ImageFont.truetype("arial.ttf", 36),
            centering=(False, True)
        ),
        TextZone(
            pos=(20, 300),
            dimensions=(220, 220),
            font=ImageFont.truetype("arial.ttf", 36),
            centering=(False, True)
        )]
    )