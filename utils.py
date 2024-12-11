from dataclasses import dataclass
from datetime import datetime


@dataclass
class Run:
    pilot1: str
    pilot2: str
    to_go: bool
    winner_run: int
    winner_placement: int
    loser_run: int
    loser_placement: int


@dataclass
class Championship:
    name: str
    pilots: list[str]
    log: list[int]
    setka: dict
    date: datetime = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    filename: str = datetime.now().strftime("%Y-%m-%d %H-%M-%S") + ".txt"


def handle_emptys(setka: dict):
    ordered_keys = sorted(list(setka.keys()))
    for i in ordered_keys:
        run = setka[i]
        condition1 = run[1] == "empty" or run[2] == "empty"
        condition2 = run[1] != "" and run[2] != ""
        condition3 = run["to_go"] == 0
        if condition1 and condition2 and condition3:
            not_empty_pos = 2 if run[1] == "empty" else 1
            setka = reg_result(i, not_empty_pos, setka)
    return setka


def setka_creator_8(pilots: list[str]) -> dict:
    setka = {
        1: {
            1: "",
            2: "",
            "winner_run": 7,
            "winner_placement": 1,
            "loser_run": 5,
            "loser_placement": 1,
            "to_go": 0,
            "who_won": 0,
            "coord1": (115, 270),
            "coord2": (115, 310),
        },
        2: {
            1: "",
            2: "",
            "winner_run": 7,
            "winner_placement": 2,
            "loser_run": 5,
            "loser_placement": 2,
            "to_go": 0,
            "who_won": 0,
            "coord1": (115, 370),
            "coord2": (115, 410),
        },
        3: {
            1: "",
            2: "",
            "winner_run": 8,
            "winner_placement": 1,
            "loser_run": 6,
            "loser_placement": 1,
            "to_go": 0,
            "who_won": 0,
            "coord1": (115, 470),
            "coord2": (115, 510),
        },
        4: {
            1: "",
            2: "",
            "winner_run": 8,
            "winner_placement": 2,
            "loser_run": 6,
            "loser_placement": 2,
            "to_go": 0,
            "who_won": 0,
            "coord1": (115, 570),
            "coord2": (115, 610),
        },
        5: {
            1: "",
            2: "",
            "winner_run": 10,
            "winner_placement": 1,
            "loser_run": 0,
            "loser_placement": 0,
            "to_go": 0,
            "who_won": 0,
            "coord1": (115, 815),
            "coord2": (115, 855),
        },
        6: {
            1: "",
            2: "",
            "winner_run": 9,
            "winner_placement": 1,
            "loser_run": 0,
            "loser_placement": 0,
            "to_go": 0,
            "who_won": 0,
            "coord1": (115, 915),
            "coord2": (115, 955),
        },
        7: {
            1: "",
            2: "",
            "winner_run": 12,
            "winner_placement": 1,
            "loser_run": 10,
            "loser_placement": 2,
            "to_go": 0,
            "who_won": 0,
            "coord1": (550, 315),
            "coord2": (550, 355),
        },
        8: {
            1: "",
            2: "",
            "winner_run": 12,
            "winner_placement": 2,
            "loser_run": 9,
            "loser_placement": 2,
            "to_go": 0,
            "who_won": 0,
            "coord1": (550, 510),
            "coord2": (550, 550),
        },
        9: {
            1: "",
            2: "",
            "winner_run": 11,
            "winner_placement": 1,
            "loser_run": 0,
            "loser_placement": 0,
            "to_go": 0,
            "who_won": 0,
            "coord1": (425, 875),
            "coord2": (425, 915),
        },
        10: {
            1: "",
            2: "",
            "winner_run": 11,
            "winner_placement": 2,
            "loser_run": 0,
            "loser_placement": 0,
            "to_go": 0,
            "who_won": 0,
            "coord1": (425, 775),
            "coord2": (425, 815),
        },
        11: {
            1: "",
            2: "",
            "winner_run": 13,
            "winner_placement": 1,
            "loser_run": 0,
            "loser_placement": 0,
            "to_go": 0,
            "who_won": 0,
            "coord1": (815, 830),
            "coord2": (815, 870),
        },
        12: {
            1: "",
            2: "",
            "winner_run": 14,
            "winner_placement": 1,
            "loser_run": 13,
            "loser_placement": 2,
            "to_go": 0,
            "who_won": 0,
            "coord1": (1075, 445),
            "coord2": (1075, 485),
        },
        13: {
            1: "",
            2: "",
            "winner_run": 14,
            "winner_placement": 2,
            "loser_run": 0,
            "loser_placement": 0,
            "to_go": 0,
            "who_won": 0,
            "coord1": (1075, 830),
            "coord2": (1075, 870),
        },
        14: {
            1: "",
            2: "",
            "winner_run": 15,
            "winner_placement": 1,
            "loser_run": 15,
            "loser_placement": 2,
            "to_go": 0,
            "who_won": 0,
            "coord1": (1400, 635),
            "coord2": (1400, 675),
        },
        15: {1: "", 2: "", "to_go": 1, "coord1": (1395, 290), "coord2": (1395, 330)},
    }
    diff = 8 - len(pilots)
    ext = ["empty"] * diff
    pilots = pilots.copy()
    pilots.extend(ext)
    setka[1][1] = pilots[0]
    setka[1][2] = pilots[7]
    setka[2][1] = pilots[3]
    setka[2][2] = pilots[4]
    setka[3][1] = pilots[1]
    setka[3][2] = pilots[6]
    setka[4][1] = pilots[2]
    setka[4][2] = pilots[5]
    setka = handle_emptys(setka)
    return setka


def get_runs(setka: dict) -> list:
    result = []
    ordered_keys = sorted(list(setka.keys()))
    for i in ordered_keys:
        run = setka[i]
        if run[1] == "empty" or run[2] == "empty":
            continue
        if run[1] == "" or run[2] == "":
            continue
        if run["to_go"] == 1:
            continue
        result.append(
            [
                i,
                run[1],
                run[2],
                run["winner_run"],
                run["winner_placement"],
                run["loser_run"],
                run["loser_placement"],
            ]
        )
    return result


def reg_result(run_number: int, winner: int, setka: dict) -> dict:
    run = setka[run_number]
    setka[run_number]["to_go"] = 1
    setka[run_number]["who_won"] = winner
    loser = 1 if winner == 2 else 2
    setka[run["winner_run"]][run["winner_placement"]] = run[winner]
    if run["loser_run"] != 0:
        setka[run["loser_run"]][run["loser_placement"]] = run[loser]
    # setka = handle_emptys(setka)
    return setka


def championship_save(chapmpionship: Championship, filename: str):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(chapmpionship.name + "\n")
        f.write("pilots" + "\n")
        f.write(",".join(chapmpionship.pilots) + "\n")
        f.write(f"log" + "\n")
        f.write(",".join(chapmpionship.log))
        f.write(f"setka, {len(chapmpionship.setka)}" + "\n")
        for run_number, run in chapmpionship.setka.items():
            # print(run_number, run)
            line = [f"{run_number}"]
            for k, v in run.items():
                line += [f"{k}:{v}"]
            f.write(",".join(line) + "\n")


def champ_read(file_name: str) -> Championship:
    with open(file_name, encoding="utf-8") as file:
        lines = file.readlines()
    champ_name = lines[0][:-1]
    pilots = lines[2][:-1].split(",")
    log = list(map(int, lines[4][:-1].split(",")))
    setka = {}
    setka_len = int(lines[5].split(",")[1])
    for i in range(6, 6 + setka_len):
        run_number, *run = lines[i][:-1].split(",")
        run_number = int(run_number)
        run_dict = {}
        for i in run:
            l, r = i.split(":")
            if l in ["1", "2"]:
                run_dict[int(l)] = r
            else:
                run_dict[l] = int(r)
        setka[run_number] = run_dict
    return Championship(name=champ_name, pilots=pilots, log=log, setka=setka)


def setka_jpg(setka):

    import cv2

    img = cv2.imread("rei.png")
    font = cv2.FONT_HERSHEY_COMPLEX
    name_offset = 10
    box_width = 240
    box_height = 30
    text_color = (0, 0, 0)
    grid_box_color = (0, 0, 255)

    for run in setka.values():
        x1 = run["coord1"][0]
        y1 = run["coord1"][1]
        x2 = run["coord2"][0]
        y2 = run["coord2"][1]

        cv2.putText(img, run[1], run["coord1"], font, 1, color=text_color, thickness=1)
        cv2.rectangle(
            img,
            (x1, y1 + name_offset),
            (x1 + box_width, y1 - box_height),
            color=grid_box_color,
            thickness=2,
        )

        cv2.putText(img, run[2], run["coord2"], font, 1, color=text_color, thickness=1)
        cv2.rectangle(
            img,
            (x2, y2 + name_offset),
            (x2 + box_width, y2 - box_height),
            color=grid_box_color,
            thickness=2,
        )

    lines = [
        [(355, 280), (450, 280)],
        [(355, 375), (450, 375)],
        [(355, 475), (450, 475)],
        [(355, 575), (450, 575)],
        [(450, 280), (450, 375)],
        [(450, 475), (450, 575)],
        [(450, 325), (555, 325)],
        [(450, 520), (555, 520)],
        [(790, 525), (895, 525)],
        [(790, 320), (895, 320)],
        [(895, 320), (895, 525)],
        [(900, 420), (1045, 420)],
        [(1045, 420), (1045, 455)],
        [(1045, 455), (1080, 455)],
        [(1315, 455), (1380, 455)],
        [(1380, 455), (1380, 840)],
        [(1315, 840), (1380, 840)],
        [(1080, 840), (1045, 840)],
        [(665, 785), (730, 785)],
        [(865, 840), (730, 840)],
        [(730, 885), (730, 785)],
        [(665, 885), (730, 885)],
        [(405, 785), (425, 785)],
        [(570, 785), (535, 785)],
        [(405, 785), (405, 820)],
        [(355, 820), (405, 820)],
        [(425, 885), (405, 885)],
        [(405, 885), (405, 920)],
        [(405, 920), (355, 920)],
        [(1380, 645), (1410, 645)],
        [(1640, 645), (1675, 645)],
        [(1675, 645), (1675, 300)],
        [(1675, 300), (1635, 300)]
    ]
    for coord1, coord2 in lines:
        cv2.line(img, coord1, coord2, grid_box_color, thickness=2)

    cv2.imwrite("result.jpg", img)
    # res = cv2.resize(img, dsize=(1600, 900), interpolation=cv2.INTER_CUBIC)
    # cv2.namedWindow("Resized", cv2.WINDOW_NORMAL)

    # cv2.imshow("Resized", res)

    # cv2.waitKey()
