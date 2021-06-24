
"""
    core/sounds/vox/vox.py
    module that contains half-life vox
    announcement system sounds as .wav files
    in folder original

    if this file is run for the first time
    on your computer, it will autogenerate
    all the sound files -15 db (because they are loud by original)
    and they are placed in a folder called 'sounds'
    in your home dir on your os

    author: @alexzander
"""


# python
import os
import threading
from time import sleep

# core package ( pip install python-core )
from core.json__ import *
from core.audio import *
from core.aesthetics import ConsoleColored

# core/sounds
from core.sounds.play import play_commands
from core.sounds.initialize import check_remote_database


# checking and reading remote database
remote_sounds_json_path = check_remote_database("vox")
remote_sounds_json = read_json_from_file(remote_sounds_json_path)


# =========== variety of vox announcement system sounds ===============

def access_denied():
    print(ConsoleColored("Access denied!", "red", bold=1))
    commands = ["access", "denied"]
    play_commands(remote_sounds_json, *commands)


def access_granted():
    print(ConsoleColored("Access granted!", "green", bold=1))
    commands = ["access", "granted"]
    play_commands(remote_sounds_json, *commands)


def you_are_authorized_to(action="proceed", __not=0):
    commands = ["you", "are", "authorized", "to", action]
    if __not:
        print(ConsoleColored("You are unauthorized to {}.".format(action), "red", bold=1))
        commands[2] = "unauthorized"
    else:
        print(ConsoleColored("You are authorized to {}.".format(action), "green", bold=1))

    play_commands(remote_sounds_json, *commands)


def system_is_down():
    print(ConsoleColored("System is down.", "red", bold=1))
    commands = ["system", "is", "down"]
    play_commands(remote_sounds_json, *commands)


def command_is_forbidden():
    print(ConsoleColored("Command is forbidden.", "yellow", bold=1))
    commands = ["command", "is", "forbidden"]
    play_commands(remote_sounds_json, *commands)


def command_is_invalid():
    print(ConsoleColored("Command is invalid.", "yellow", bold=1))
    play_commands("command", "is", "invalid")


def intruder_is_detected():
    print(ConsoleColored("Intruder is detected.", "yellow", bold=1))
    commands = ["Intruder", "is", "detected"]
    play_commands(remote_sounds_json, *commands)


digits = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen",
    20: "twenty"
}


def countdown(start=20, color="yellow", __pause=.4):
    if start > 20:
        raise ValueError("this cannot be > 10")

    for i in range(start, -1, -1):
        if i > 9:
            print("[  {}  ]".format(ConsoleColored(str(i), color, bold=1)))
        else:
            print("[   {}  ]".format(ConsoleColored(str(i), color, bold=1)))

        playaudio(remote_sounds_json[digits[i]])
        sleep(__pause)


def countdown_allarm(start=20, color="yellow", __pause=.4):
    if start > 20:
        raise ValueError("this cannot be > 10")

    allarm_thread = threading.Thread(target=play_commands, args=("death-star-allarm",))
    allarm_thread.start()

    countdown(start, color, __pause)

    # i dont know how to kill the allarm thread
    # cuz has 22 seconds and the countdown has max 10 seconds
    # solution:
    # crop the allarm from 22 to 10 seconds, easy

def detonation_activated():
    print(ConsoleColored("[[[ Detonation activated ]]].", "red", bold=1))
    play_commands("detonation", "activated", "ten", "seconds", "remaining")
    countdown_allarm(color="red")


def computer_is_loading():
    print(ConsoleColored("Computer is loading...", "green", bold=1))
    play_commands("computer", "is", "loading")


def computer_is_under_control():
    print(ConsoleColored("Computer is under control.", "green", bold=1))
    play_commands("computer", "is", "under", "control")


def malfunction_detected():
    print(ConsoleColored("Malfunction detected.", "yellow", bold=1))
    play_commands("malfunction", "detected")


def you_are_an_idiot():
    print(ConsoleColored("You are an idiot.", "blue", bold=1))
    play_commands("you", "are", "an", "idiot")


def decompression_activated():
    print(ConsoleColored("Decompression activated...", "yellow", bold=1))
    play_commands("decompression", "activated")


def level_unlocked():
    print(ConsoleColored("Level unlocked.", "green", bold=1))
    play_commands("level", "unlocked")


def twenty():
    play_commands(remote_sounds_json, "twenty")


def order():
    play_commands(remote_sounds_json, "order")


def a_sound():
    play_commands(remote_sounds_json, "a")


def accelerating_sound():
    play_commands(remote_sounds_json, "accelerating")


def accelerator_sound():
    play_commands(remote_sounds_json, "accelerator")


def accepted_sound():
    play_commands(remote_sounds_json, "accepted")


def access_sound():
    play_commands(remote_sounds_json, "access")


def acknowledge_sound():
    play_commands(remote_sounds_json, "acknowledge")


def acknowledged_sound():
    play_commands(remote_sounds_json, "acknowledged")


def acquired_sound():
    play_commands(remote_sounds_json, "acquired")


def acquisition_sound():
    play_commands(remote_sounds_json, "acquisition")


def across_sound():
    play_commands(remote_sounds_json, "across")


def activate_sound():
    play_commands(remote_sounds_json, "activate")


def activated_sound():
    play_commands(remote_sounds_json, "activated")


def activity_sound():
    play_commands(remote_sounds_json, "activity")


def adios_sound():
    play_commands(remote_sounds_json, "adios")


def administration_sound():
    play_commands(remote_sounds_json, "administration")


def advanced_sound():
    play_commands(remote_sounds_json, "advanced")


def after_sound():
    play_commands(remote_sounds_json, "after")


def agent_sound():
    play_commands(remote_sounds_json, "agent")


def alarm_sound():
    play_commands(remote_sounds_json, "alarm")


def alert_sound():
    play_commands(remote_sounds_json, "alert")


def alien_sound():
    play_commands(remote_sounds_json, "alien")


def aligned_sound():
    play_commands(remote_sounds_json, "aligned")


def all_sound():
    play_commands(remote_sounds_json, "all")


def alpha_sound():
    play_commands(remote_sounds_json, "alpha")


def am_sound():
    play_commands(remote_sounds_json, "am")


def amigo_sound():
    play_commands(remote_sounds_json, "amigo")


def ammunition_sound():
    play_commands(remote_sounds_json, "ammunition")


def an_sound():
    play_commands(remote_sounds_json, "an")


def and_sound():
    play_commands(remote_sounds_json, "and")


def announcement_sound():
    play_commands(remote_sounds_json, "announcement")


def anomalous_sound():
    play_commands(remote_sounds_json, "anomalous")


def antenna_sound():
    play_commands(remote_sounds_json, "antenna")


def any_sound():
    play_commands(remote_sounds_json, "any")


def apprehend_sound():
    play_commands(remote_sounds_json, "apprehend")


def approach_sound():
    play_commands(remote_sounds_json, "approach")


def are_sound():
    play_commands(remote_sounds_json, "are")


def area_sound():
    play_commands(remote_sounds_json, "area")


def arm_sound():
    play_commands(remote_sounds_json, "arm")


def armed_sound():
    play_commands(remote_sounds_json, "armed")


def armor_sound():
    play_commands(remote_sounds_json, "armor")


def armory_sound():
    play_commands(remote_sounds_json, "armory")


def arrest_sound():
    play_commands(remote_sounds_json, "arrest")


def ass_sound():
    play_commands(remote_sounds_json, "ass")


def at_sound():
    play_commands(remote_sounds_json, "at")


def atomic_sound():
    play_commands(remote_sounds_json, "atomic")


def attention_sound():
    play_commands(remote_sounds_json, "attention")


def authorize_sound():
    play_commands(remote_sounds_json, "authorize")


def authorized_sound():
    play_commands(remote_sounds_json, "authorized")


def automatic_sound():
    play_commands(remote_sounds_json, "automatic")


def away_sound():
    play_commands(remote_sounds_json, "away")


def b_sound():
    play_commands(remote_sounds_json, "b")


def back_sound():
    play_commands(remote_sounds_json, "back")


def backman_sound():
    play_commands(remote_sounds_json, "backman")


def bad_sound():
    play_commands(remote_sounds_json, "bad")


def bag_sound():
    play_commands(remote_sounds_json, "bag")


def bailey_sound():
    play_commands(remote_sounds_json, "bailey")


def barracks_sound():
    play_commands(remote_sounds_json, "barracks")


def base_sound():
    play_commands(remote_sounds_json, "base")


def bay_sound():
    play_commands(remote_sounds_json, "bay")


def be_sound():
    play_commands(remote_sounds_json, "be")


def been_sound():
    play_commands(remote_sounds_json, "been")


def before_sound():
    play_commands(remote_sounds_json, "before")


def beyond_sound():
    play_commands(remote_sounds_json, "beyond")


def biohazard_sound():
    play_commands(remote_sounds_json, "biohazard")


def biological_sound():
    play_commands(remote_sounds_json, "biological")


def birdwell_sound():
    play_commands(remote_sounds_json, "birdwell")


def bizwarn_sound():
    play_commands(remote_sounds_json, "bizwarn")


def black_sound():
    play_commands(remote_sounds_json, "black")


def blast_sound():
    play_commands(remote_sounds_json, "blast")


def blocked_sound():
    play_commands(remote_sounds_json, "blocked")


def bloop_sound():
    play_commands(remote_sounds_json, "bloop")


def blue_sound():
    play_commands(remote_sounds_json, "blue")


def bottom_sound():
    play_commands(remote_sounds_json, "bottom")


def bravo_sound():
    play_commands(remote_sounds_json, "bravo")


def breach_sound():
    play_commands(remote_sounds_json, "breach")


def breached_sound():
    play_commands(remote_sounds_json, "breached")


def break_sound():
    play_commands(remote_sounds_json, "break")


def bridge_sound():
    play_commands(remote_sounds_json, "bridge")


def bust_sound():
    play_commands(remote_sounds_json, "bust")


def but_sound():
    play_commands(remote_sounds_json, "but")


def button_sound():
    play_commands(remote_sounds_json, "button")


def buzwarn_sound():
    play_commands(remote_sounds_json, "buzwarn")


def bypass_sound():
    play_commands(remote_sounds_json, "bypass")


def c_sound():
    play_commands(remote_sounds_json, "c")


def cable_sound():
    play_commands(remote_sounds_json, "cable")


def call_sound():
    play_commands(remote_sounds_json, "call")


def called_sound():
    play_commands(remote_sounds_json, "called")


def canal_sound():
    play_commands(remote_sounds_json, "canal")


def cap_sound():
    play_commands(remote_sounds_json, "cap")


def captain_sound():
    play_commands(remote_sounds_json, "captain")


def capture_sound():
    play_commands(remote_sounds_json, "capture")


def ceiling_sound():
    play_commands(remote_sounds_json, "ceiling")


def celsius_sound():
    play_commands(remote_sounds_json, "celsius")


def center_sound():
    play_commands(remote_sounds_json, "center")


def centi_sound():
    play_commands(remote_sounds_json, "centi")


def central_sound():
    play_commands(remote_sounds_json, "central")


def chamber_sound():
    play_commands(remote_sounds_json, "chamber")


def charlie_sound():
    play_commands(remote_sounds_json, "charlie")


def check_sound():
    play_commands(remote_sounds_json, "check")


def checkpoint_sound():
    play_commands(remote_sounds_json, "checkpoint")


def chemical_sound():
    play_commands(remote_sounds_json, "chemical")


def cleanup_sound():
    play_commands(remote_sounds_json, "cleanup")


def clear_sound():
    play_commands(remote_sounds_json, "clear")


def clearance_sound():
    play_commands(remote_sounds_json, "clearance")


def close_sound():
    play_commands(remote_sounds_json, "close")


def code_sound():
    play_commands(remote_sounds_json, "code")


def coded_sound():
    play_commands(remote_sounds_json, "coded")


def collider_sound():
    play_commands(remote_sounds_json, "collider")


def comma_sound():
    play_commands(remote_sounds_json, "comma")


def command_sound():
    play_commands(remote_sounds_json, "command")


def communication_sound():
    play_commands(remote_sounds_json, "communication")


def complex_sound():
    play_commands(remote_sounds_json, "complex")


def computer_sound():
    play_commands(remote_sounds_json, "computer")


def condition_sound():
    play_commands(remote_sounds_json, "condition")


def containment_sound():
    play_commands(remote_sounds_json, "containment")


def contamination_sound():
    play_commands(remote_sounds_json, "contamination")


def control_sound():
    play_commands(remote_sounds_json, "control")


def coolant_sound():
    play_commands(remote_sounds_json, "coolant")


def coomer_sound():
    play_commands(remote_sounds_json, "coomer")


def core_sound():
    play_commands(remote_sounds_json, "core")


def correct_sound():
    play_commands(remote_sounds_json, "correct")


def corridor_sound():
    play_commands(remote_sounds_json, "corridor")


def crew_sound():
    play_commands(remote_sounds_json, "crew")


def cross_sound():
    play_commands(remote_sounds_json, "cross")


def cryogenic_sound():
    play_commands(remote_sounds_json, "cryogenic")


def d_sound():
    play_commands(remote_sounds_json, "d")


def dadeda_sound():
    play_commands(remote_sounds_json, "dadeda")


def damage_sound():
    play_commands(remote_sounds_json, "damage")


def damaged_sound():
    play_commands(remote_sounds_json, "damaged")


def danger_sound():
    play_commands(remote_sounds_json, "danger")


def day_sound():
    play_commands(remote_sounds_json, "day")


def deactivated_sound():
    play_commands(remote_sounds_json, "deactivated")


def decompression_sound():
    play_commands(remote_sounds_json, "decompression")


def decontamination_sound():
    play_commands(remote_sounds_json, "decontamination")


def deeoo_sound():
    play_commands(remote_sounds_json, "deeoo")


def defense_sound():
    play_commands(remote_sounds_json, "defense")


def degrees_sound():
    play_commands(remote_sounds_json, "degrees")


def delta_sound():
    play_commands(remote_sounds_json, "delta")


def denied_sound():
    play_commands(remote_sounds_json, "denied")


def deploy_sound():
    play_commands(remote_sounds_json, "deploy")


def deployed_sound():
    play_commands(remote_sounds_json, "deployed")


def destroy_sound():
    play_commands(remote_sounds_json, "destroy")


def destroyed_sound():
    play_commands(remote_sounds_json, "destroyed")


def detain_sound():
    play_commands(remote_sounds_json, "detain")


def detected_sound():
    play_commands(remote_sounds_json, "detected")


def detonation_sound():
    play_commands(remote_sounds_json, "detonation")


def device_sound():
    play_commands(remote_sounds_json, "device")


def did_sound():
    play_commands(remote_sounds_json, "did")


def die_sound():
    play_commands(remote_sounds_json, "die")


def dimensional_sound():
    play_commands(remote_sounds_json, "dimensional")


def dirt_sound():
    play_commands(remote_sounds_json, "dirt")


def disengaged_sound():
    play_commands(remote_sounds_json, "disengaged")


def dish_sound():
    play_commands(remote_sounds_json, "dish")


def disposal_sound():
    play_commands(remote_sounds_json, "disposal")


def distance_sound():
    play_commands(remote_sounds_json, "distance")


def distortion_sound():
    play_commands(remote_sounds_json, "distortion")


def do_sound():
    play_commands(remote_sounds_json, "do")


def doctor_sound():
    play_commands(remote_sounds_json, "doctor")


def doop_sound():
    play_commands(remote_sounds_json, "doop")


def door_sound():
    play_commands(remote_sounds_json, "door")


def down_sound():
    play_commands(remote_sounds_json, "down")


def dual_sound():
    play_commands(remote_sounds_json, "dual")


def duct_sound():
    play_commands(remote_sounds_json, "duct")


def e_sound():
    play_commands(remote_sounds_json, "e")


def east_sound():
    play_commands(remote_sounds_json, "east")


def echo_sound():
    play_commands(remote_sounds_json, "echo")


def ed_sound():
    play_commands(remote_sounds_json, "ed")


def effect_sound():
    play_commands(remote_sounds_json, "effect")


def egress_sound():
    play_commands(remote_sounds_json, "egress")


def eight_sound():
    play_commands(remote_sounds_json, "eight")


def eighteen_sound():
    play_commands(remote_sounds_json, "eighteen")


def eighty_sound():
    play_commands(remote_sounds_json, "eighty")


def electric_sound():
    play_commands(remote_sounds_json, "electric")


def electromagnetic_sound():
    play_commands(remote_sounds_json, "electromagnetic")


def elevator_sound():
    play_commands(remote_sounds_json, "elevator")


def eleven_sound():
    play_commands(remote_sounds_json, "eleven")


def eliminate_sound():
    play_commands(remote_sounds_json, "eliminate")


def emergency_sound():
    play_commands(remote_sounds_json, "emergency")


def energy_sound():
    play_commands(remote_sounds_json, "energy")


def engage_sound():
    play_commands(remote_sounds_json, "engage")


def engaged_sound():
    play_commands(remote_sounds_json, "engaged")


def engine_sound():
    play_commands(remote_sounds_json, "engine")


def enter_sound():
    play_commands(remote_sounds_json, "enter")


def entry_sound():
    play_commands(remote_sounds_json, "entry")


def environment_sound():
    play_commands(remote_sounds_json, "environment")


def error_sound():
    play_commands(remote_sounds_json, "error")


def escape_sound():
    play_commands(remote_sounds_json, "escape")


def evacuate_sound():
    play_commands(remote_sounds_json, "evacuate")


def exchange_sound():
    play_commands(remote_sounds_json, "exchange")


def exit_sound():
    play_commands(remote_sounds_json, "exit")


def expect_sound():
    play_commands(remote_sounds_json, "expect")


def experiment_sound():
    play_commands(remote_sounds_json, "experiment")


def experimental_sound():
    play_commands(remote_sounds_json, "experimental")


def explode_sound():
    play_commands(remote_sounds_json, "explode")


def explosion_sound():
    play_commands(remote_sounds_json, "explosion")


def exposure_sound():
    play_commands(remote_sounds_json, "exposure")


def exterminate_sound():
    play_commands(remote_sounds_json, "exterminate")


def extinguish_sound():
    play_commands(remote_sounds_json, "extinguish")


def extinguisher_sound():
    play_commands(remote_sounds_json, "extinguisher")


def extreme_sound():
    play_commands(remote_sounds_json, "extreme")


def f_sound():
    play_commands(remote_sounds_json, "f")


def facility_sound():
    play_commands(remote_sounds_json, "facility")


def fahrenheit_sound():
    play_commands(remote_sounds_json, "fahrenheit")


def failed_sound():
    play_commands(remote_sounds_json, "failed")


def failure_sound():
    play_commands(remote_sounds_json, "failure")


def farthest_sound():
    play_commands(remote_sounds_json, "farthest")


def fast_sound():
    play_commands(remote_sounds_json, "fast")


def feet_sound():
    play_commands(remote_sounds_json, "feet")


def field_sound():
    play_commands(remote_sounds_json, "field")


def fifteen_sound():
    play_commands(remote_sounds_json, "fifteen")


def fifth_sound():
    play_commands(remote_sounds_json, "fifth")


def fifty_sound():
    play_commands(remote_sounds_json, "fifty")


def final_sound():
    play_commands(remote_sounds_json, "final")


def fine_sound():
    play_commands(remote_sounds_json, "fine")


def fire_sound():
    play_commands(remote_sounds_json, "fire")


def first_sound():
    play_commands(remote_sounds_json, "first")


def five_sound():
    play_commands(remote_sounds_json, "five")


def flooding_sound():
    play_commands(remote_sounds_json, "flooding")


def floor_sound():
    play_commands(remote_sounds_json, "floor")


def fool_sound():
    play_commands(remote_sounds_json, "fool")


def for_sound():
    play_commands(remote_sounds_json, "for")


def forbidden_sound():
    play_commands(remote_sounds_json, "forbidden")


def force_sound():
    play_commands(remote_sounds_json, "force")


def forms_sound():
    play_commands(remote_sounds_json, "forms")


def found_sound():
    play_commands(remote_sounds_json, "found")


def four_sound():
    play_commands(remote_sounds_json, "four")


def fourteen_sound():
    play_commands(remote_sounds_json, "fourteen")


def fourth_sound():
    play_commands(remote_sounds_json, "fourth")


def fourty_sound():
    play_commands(remote_sounds_json, "fourty")


def foxtrot_sound():
    play_commands(remote_sounds_json, "foxtrot")


def freeman_sound():
    play_commands(remote_sounds_json, "freeman")


def freezer_sound():
    play_commands(remote_sounds_json, "freezer")


def from_sound():
    play_commands(remote_sounds_json, "from")


def front_sound():
    play_commands(remote_sounds_json, "front")


def fuel_sound():
    play_commands(remote_sounds_json, "fuel")


def g_sound():
    play_commands(remote_sounds_json, "g")


def get_sound():
    play_commands(remote_sounds_json, "get")


def go_sound():
    play_commands(remote_sounds_json, "go")


def going_sound():
    play_commands(remote_sounds_json, "going")


def good_sound():
    play_commands(remote_sounds_json, "good")


def goodbye_sound():
    play_commands(remote_sounds_json, "goodbye")


def gordon_sound():
    play_commands(remote_sounds_json, "gordon")


def got_sound():
    play_commands(remote_sounds_json, "got")


def government_sound():
    play_commands(remote_sounds_json, "government")


def granted_sound():
    play_commands(remote_sounds_json, "granted")


def great_sound():
    play_commands(remote_sounds_json, "great")


def green_sound():
    play_commands(remote_sounds_json, "green")


def grenade_sound():
    play_commands(remote_sounds_json, "grenade")


def guard_sound():
    play_commands(remote_sounds_json, "guard")


def gulf_sound():
    play_commands(remote_sounds_json, "gulf")


def gun_sound():
    play_commands(remote_sounds_json, "gun")


def guthrie_sound():
    play_commands(remote_sounds_json, "guthrie")


def handling_sound():
    play_commands(remote_sounds_json, "handling")


def hangar_sound():
    play_commands(remote_sounds_json, "hangar")


def has_sound():
    play_commands(remote_sounds_json, "has")


def have_sound():
    play_commands(remote_sounds_json, "have")


def hazard_sound():
    play_commands(remote_sounds_json, "hazard")


def head_sound():
    play_commands(remote_sounds_json, "head")


def health_sound():
    play_commands(remote_sounds_json, "health")


def heat_sound():
    play_commands(remote_sounds_json, "heat")


def helicopter_sound():
    play_commands(remote_sounds_json, "helicopter")


def helium_sound():
    play_commands(remote_sounds_json, "helium")


def hello_sound():
    play_commands(remote_sounds_json, "hello")


def help_sound():
    play_commands(remote_sounds_json, "help")


def here_sound():
    play_commands(remote_sounds_json, "here")


def hide_sound():
    play_commands(remote_sounds_json, "hide")


def high_sound():
    play_commands(remote_sounds_json, "high")


def highest_sound():
    play_commands(remote_sounds_json, "highest")


def hit_sound():
    play_commands(remote_sounds_json, "hit")


def hole_sound():
    play_commands(remote_sounds_json, "hole")


def hostile_sound():
    play_commands(remote_sounds_json, "hostile")


def hot_sound():
    play_commands(remote_sounds_json, "hot")


def hotel_sound():
    play_commands(remote_sounds_json, "hotel")


def hour_sound():
    play_commands(remote_sounds_json, "hour")


def hours_sound():
    play_commands(remote_sounds_json, "hours")


def hundred_sound():
    play_commands(remote_sounds_json, "hundred")


def hydro_sound():
    play_commands(remote_sounds_json, "hydro")


def i_sound():
    play_commands(remote_sounds_json, "i")


def idiot_sound():
    play_commands(remote_sounds_json, "idiot")


def illegal_sound():
    play_commands(remote_sounds_json, "illegal")


def immediate_sound():
    play_commands(remote_sounds_json, "immediate")


def immediately_sound():
    play_commands(remote_sounds_json, "immediately")


def in_sound():
    play_commands(remote_sounds_json, "in")


def inches_sound():
    play_commands(remote_sounds_json, "inches")


def india_sound():
    play_commands(remote_sounds_json, "india")


def ing_sound():
    play_commands(remote_sounds_json, "ing")


def inoperative_sound():
    play_commands(remote_sounds_json, "inoperative")


def inside_sound():
    play_commands(remote_sounds_json, "inside")


def inspection_sound():
    play_commands(remote_sounds_json, "inspection")


def inspector_sound():
    play_commands(remote_sounds_json, "inspector")


def interchange_sound():
    play_commands(remote_sounds_json, "interchange")


def intruder_sound():
    play_commands(remote_sounds_json, "intruder")


def invallid_sound():
    play_commands(remote_sounds_json, "invallid")


def invasion_sound():
    play_commands(remote_sounds_json, "invasion")


def is_sound():
    play_commands(remote_sounds_json, "is")


def it_sound():
    play_commands(remote_sounds_json, "it")


def johnson_sound():
    play_commands(remote_sounds_json, "johnson")


def juliet_sound():
    play_commands(remote_sounds_json, "juliet")


def key_sound():
    play_commands(remote_sounds_json, "key")


def kill_sound():
    play_commands(remote_sounds_json, "kill")


def kilo_sound():
    play_commands(remote_sounds_json, "kilo")


def kit_sound():
    play_commands(remote_sounds_json, "kit")


def lab_sound():
    play_commands(remote_sounds_json, "lab")


def lambda_sound():
    play_commands(remote_sounds_json, "lambda")


def laser_sound():
    play_commands(remote_sounds_json, "laser")


def last_sound():
    play_commands(remote_sounds_json, "last")


def launch_sound():
    play_commands(remote_sounds_json, "launch")


def leak_sound():
    play_commands(remote_sounds_json, "leak")


def leave_sound():
    play_commands(remote_sounds_json, "leave")


def left_sound():
    play_commands(remote_sounds_json, "left")


def legal_sound():
    play_commands(remote_sounds_json, "legal")


def level_sound():
    play_commands(remote_sounds_json, "level")


def lever_sound():
    play_commands(remote_sounds_json, "lever")


def lie_sound():
    play_commands(remote_sounds_json, "lie")


def lieutenant_sound():
    play_commands(remote_sounds_json, "lieutenant")


def life_sound():
    play_commands(remote_sounds_json, "life")


def light_sound():
    play_commands(remote_sounds_json, "light")


def lima_sound():
    play_commands(remote_sounds_json, "lima")


def liquid_sound():
    play_commands(remote_sounds_json, "liquid")


def loading_sound():
    play_commands(remote_sounds_json, "loading")


def locate_sound():
    play_commands(remote_sounds_json, "locate")


def located_sound():
    play_commands(remote_sounds_json, "located")


def location_sound():
    play_commands(remote_sounds_json, "location")


def lock_sound():
    play_commands(remote_sounds_json, "lock")


def locked_sound():
    play_commands(remote_sounds_json, "locked")


def locker_sound():
    play_commands(remote_sounds_json, "locker")


def lockout_sound():
    play_commands(remote_sounds_json, "lockout")


def lower_sound():
    play_commands(remote_sounds_json, "lower")


def lowest_sound():
    play_commands(remote_sounds_json, "lowest")


def magnetic_sound():
    play_commands(remote_sounds_json, "magnetic")


def main_sound():
    play_commands(remote_sounds_json, "main")


def maintenance_sound():
    play_commands(remote_sounds_json, "maintenance")


def malfunction_sound():
    play_commands(remote_sounds_json, "malfunction")


def man_sound():
    play_commands(remote_sounds_json, "man")


def mass_sound():
    play_commands(remote_sounds_json, "mass")


def materials_sound():
    play_commands(remote_sounds_json, "materials")


def maximum_sound():
    play_commands(remote_sounds_json, "maximum")


def may_sound():
    play_commands(remote_sounds_json, "may")


def medical_sound():
    play_commands(remote_sounds_json, "medical")


def men_sound():
    play_commands(remote_sounds_json, "men")


def mercy_sound():
    play_commands(remote_sounds_json, "mercy")


def mesa_sound():
    play_commands(remote_sounds_json, "mesa")


def message_sound():
    play_commands(remote_sounds_json, "message")


def meter_sound():
    play_commands(remote_sounds_json, "meter")


def micro_sound():
    play_commands(remote_sounds_json, "micro")


def middle_sound():
    play_commands(remote_sounds_json, "middle")


def mike_sound():
    play_commands(remote_sounds_json, "mike")


def miles_sound():
    play_commands(remote_sounds_json, "miles")


def military_sound():
    play_commands(remote_sounds_json, "military")


def milli_sound():
    play_commands(remote_sounds_json, "milli")


def million_sound():
    play_commands(remote_sounds_json, "million")


def minefield_sound():
    play_commands(remote_sounds_json, "minefield")


def minimum_sound():
    play_commands(remote_sounds_json, "minimum")


def minutes_sound():
    play_commands(remote_sounds_json, "minutes")


def mister_sound():
    play_commands(remote_sounds_json, "mister")


def mode_sound():
    play_commands(remote_sounds_json, "mode")


def motor_sound():
    play_commands(remote_sounds_json, "motor")


def motorpool_sound():
    play_commands(remote_sounds_json, "motorpool")


def move_sound():
    play_commands(remote_sounds_json, "move")


def must_sound():
    play_commands(remote_sounds_json, "must")


def nearest_sound():
    play_commands(remote_sounds_json, "nearest")


def nice_sound():
    play_commands(remote_sounds_json, "nice")


def nine_sound():
    play_commands(remote_sounds_json, "nine")


def nineteen_sound():
    play_commands(remote_sounds_json, "nineteen")


def ninety_sound():
    play_commands(remote_sounds_json, "ninety")


def no_sound():
    play_commands(remote_sounds_json, "no")


def nominal_sound():
    play_commands(remote_sounds_json, "nominal")


def north_sound():
    play_commands(remote_sounds_json, "north")


def not_sound():
    play_commands(remote_sounds_json, "not")


def november_sound():
    play_commands(remote_sounds_json, "november")


def now_sound():
    play_commands(remote_sounds_json, "now")


def number_sound():
    play_commands(remote_sounds_json, "number")


def objective_sound():
    play_commands(remote_sounds_json, "objective")


def observation_sound():
    play_commands(remote_sounds_json, "observation")


def of_sound():
    play_commands(remote_sounds_json, "of")


def officer_sound():
    play_commands(remote_sounds_json, "officer")


def ok_sound():
    play_commands(remote_sounds_json, "ok")


def on_sound():
    play_commands(remote_sounds_json, "on")


def one_sound():
    play_commands(remote_sounds_json, "one")


def open_sound():
    play_commands(remote_sounds_json, "open")


def operating_sound():
    play_commands(remote_sounds_json, "operating")


def operations_sound():
    play_commands(remote_sounds_json, "operations")


def operative_sound():
    play_commands(remote_sounds_json, "operative")


def option_sound():
    play_commands(remote_sounds_json, "option")


def order_sound():
    play_commands(remote_sounds_json, "order")


def organic_sound():
    play_commands(remote_sounds_json, "organic")


def oscar_sound():
    play_commands(remote_sounds_json, "oscar")


def out_sound():
    play_commands(remote_sounds_json, "out")


def outside_sound():
    play_commands(remote_sounds_json, "outside")


def over_sound():
    play_commands(remote_sounds_json, "over")


def overload_sound():
    play_commands(remote_sounds_json, "overload")


def override_sound():
    play_commands(remote_sounds_json, "override")


def pacify_sound():
    play_commands(remote_sounds_json, "pacify")


def pain_sound():
    play_commands(remote_sounds_json, "pain")


def pal_sound():
    play_commands(remote_sounds_json, "pal")


def panel_sound():
    play_commands(remote_sounds_json, "panel")


def percent_sound():
    play_commands(remote_sounds_json, "percent")


def perimeter_sound():
    play_commands(remote_sounds_json, "perimeter")


def period_sound():
    play_commands(remote_sounds_json, "period")


def permitted_sound():
    play_commands(remote_sounds_json, "permitted")


def personnel_sound():
    play_commands(remote_sounds_json, "personnel")


def pipe_sound():
    play_commands(remote_sounds_json, "pipe")


def plant_sound():
    play_commands(remote_sounds_json, "plant")


def platform_sound():
    play_commands(remote_sounds_json, "platform")


def please_sound():
    play_commands(remote_sounds_json, "please")


def point_sound():
    play_commands(remote_sounds_json, "point")


def portal_sound():
    play_commands(remote_sounds_json, "portal")


def power_sound():
    play_commands(remote_sounds_json, "power")


def presence_sound():
    play_commands(remote_sounds_json, "presence")


def press_sound():
    play_commands(remote_sounds_json, "press")


def primary_sound():
    play_commands(remote_sounds_json, "primary")


def proceed_sound():
    play_commands(remote_sounds_json, "proceed")


def processing_sound():
    play_commands(remote_sounds_json, "processing")


def progress_sound():
    play_commands(remote_sounds_json, "progress")


def proper_sound():
    play_commands(remote_sounds_json, "proper")


def propulsion_sound():
    play_commands(remote_sounds_json, "propulsion")


def prosecute_sound():
    play_commands(remote_sounds_json, "prosecute")


def protective_sound():
    play_commands(remote_sounds_json, "protective")


def push_sound():
    play_commands(remote_sounds_json, "push")


def quantum_sound():
    play_commands(remote_sounds_json, "quantum")


def quebec_sound():
    play_commands(remote_sounds_json, "quebec")


def question_sound():
    play_commands(remote_sounds_json, "question")


def questioning_sound():
    play_commands(remote_sounds_json, "questioning")


def quick_sound():
    play_commands(remote_sounds_json, "quick")


def quit_sound():
    play_commands(remote_sounds_json, "quit")


def radiation_sound():
    play_commands(remote_sounds_json, "radiation")


def radioactive_sound():
    play_commands(remote_sounds_json, "radioactive")


def rads_sound():
    play_commands(remote_sounds_json, "rads")


def rapid_sound():
    play_commands(remote_sounds_json, "rapid")


def reach_sound():
    play_commands(remote_sounds_json, "reach")


def reached_sound():
    play_commands(remote_sounds_json, "reached")


def reactor_sound():
    play_commands(remote_sounds_json, "reactor")


def red_sound():
    play_commands(remote_sounds_json, "red")


def relay_sound():
    play_commands(remote_sounds_json, "relay")


def released_sound():
    play_commands(remote_sounds_json, "released")


def remaining_sound():
    play_commands(remote_sounds_json, "remaining")


def renegade_sound():
    play_commands(remote_sounds_json, "renegade")


def repair_sound():
    play_commands(remote_sounds_json, "repair")


def report_sound():
    play_commands(remote_sounds_json, "report")


def reports_sound():
    play_commands(remote_sounds_json, "reports")


def required_sound():
    play_commands(remote_sounds_json, "required")


def research_sound():
    play_commands(remote_sounds_json, "research")


def resevoir_sound():
    play_commands(remote_sounds_json, "resevoir")


def resistance_sound():
    play_commands(remote_sounds_json, "resistance")


def right_sound():
    play_commands(remote_sounds_json, "right")


def rocket_sound():
    play_commands(remote_sounds_json, "rocket")


def roger_sound():
    play_commands(remote_sounds_json, "roger")


def romeo_sound():
    play_commands(remote_sounds_json, "romeo")


def room_sound():
    play_commands(remote_sounds_json, "room")


def round_sound():
    play_commands(remote_sounds_json, "round")


def run_sound():
    play_commands(remote_sounds_json, "run")


def safe_sound():
    play_commands(remote_sounds_json, "safe")


def safety_sound():
    play_commands(remote_sounds_json, "safety")


def sargeant_sound():
    play_commands(remote_sounds_json, "sargeant")


def satellite_sound():
    play_commands(remote_sounds_json, "satellite")


def save_sound():
    play_commands(remote_sounds_json, "save")


def science_sound():
    play_commands(remote_sounds_json, "science")


def scream_sound():
    play_commands(remote_sounds_json, "scream")


def screen_sound():
    play_commands(remote_sounds_json, "screen")


def search_sound():
    play_commands(remote_sounds_json, "search")


def second_sound():
    play_commands(remote_sounds_json, "second")


def secondary_sound():
    play_commands(remote_sounds_json, "secondary")


def seconds_sound():
    play_commands(remote_sounds_json, "seconds")


def sector_sound():
    play_commands(remote_sounds_json, "sector")


def secure_sound():
    play_commands(remote_sounds_json, "secure")


def secured_sound():
    play_commands(remote_sounds_json, "secured")


def security_sound():
    play_commands(remote_sounds_json, "security")


def select_sound():
    play_commands(remote_sounds_json, "select")


def selected_sound():
    play_commands(remote_sounds_json, "selected")


def service_sound():
    play_commands(remote_sounds_json, "service")


def seven_sound():
    play_commands(remote_sounds_json, "seven")


def seventeen_sound():
    play_commands(remote_sounds_json, "seventeen")


def seventy_sound():
    play_commands(remote_sounds_json, "seventy")


def severe_sound():
    play_commands(remote_sounds_json, "severe")


def sewage_sound():
    play_commands(remote_sounds_json, "sewage")


def sewer_sound():
    play_commands(remote_sounds_json, "sewer")


def shield_sound():
    play_commands(remote_sounds_json, "shield")


def shipment_sound():
    play_commands(remote_sounds_json, "shipment")


def shock_sound():
    play_commands(remote_sounds_json, "shock")


def shoot_sound():
    play_commands(remote_sounds_json, "shoot")


def shower_sound():
    play_commands(remote_sounds_json, "shower")


def shut_sound():
    play_commands(remote_sounds_json, "shut")


def side_sound():
    play_commands(remote_sounds_json, "side")


def sierra_sound():
    play_commands(remote_sounds_json, "sierra")


def sight_sound():
    play_commands(remote_sounds_json, "sight")


def silo_sound():
    play_commands(remote_sounds_json, "silo")


def six_sound():
    play_commands(remote_sounds_json, "six")


def sixteen_sound():
    play_commands(remote_sounds_json, "sixteen")


def sixty_sound():
    play_commands(remote_sounds_json, "sixty")


def slime_sound():
    play_commands(remote_sounds_json, "slime")


def slow_sound():
    play_commands(remote_sounds_json, "slow")


def soldier_sound():
    play_commands(remote_sounds_json, "soldier")


def some_sound():
    play_commands(remote_sounds_json, "some")


def someone_sound():
    play_commands(remote_sounds_json, "someone")


def something_sound():
    play_commands(remote_sounds_json, "something")


def son_sound():
    play_commands(remote_sounds_json, "son")


def sorry_sound():
    play_commands(remote_sounds_json, "sorry")


def south_sound():
    play_commands(remote_sounds_json, "south")


def squad_sound():
    play_commands(remote_sounds_json, "squad")


def square_sound():
    play_commands(remote_sounds_json, "square")


def stairway_sound():
    play_commands(remote_sounds_json, "stairway")


def status_sound():
    play_commands(remote_sounds_json, "status")


def sterile_sound():
    play_commands(remote_sounds_json, "sterile")


def sterilization_sound():
    play_commands(remote_sounds_json, "sterilization")


def storage_sound():
    play_commands(remote_sounds_json, "storage")


def sub_sound():
    play_commands(remote_sounds_json, "sub")


def subsurface_sound():
    play_commands(remote_sounds_json, "subsurface")


def sudden_sound():
    play_commands(remote_sounds_json, "sudden")


def suit_sound():
    play_commands(remote_sounds_json, "suit")


def superconducting_sound():
    play_commands(remote_sounds_json, "superconducting")


def supercooled_sound():
    play_commands(remote_sounds_json, "supercooled")


def supply_sound():
    play_commands(remote_sounds_json, "supply")


def surface_sound():
    play_commands(remote_sounds_json, "surface")


def surrender_sound():
    play_commands(remote_sounds_json, "surrender")


def surround_sound():
    play_commands(remote_sounds_json, "surround")


def surrounded_sound():
    play_commands(remote_sounds_json, "surrounded")


def switch_sound():
    play_commands(remote_sounds_json, "switch")


def system_sound():
    play_commands(remote_sounds_json, "system")


def systems_sound():
    play_commands(remote_sounds_json, "systems")


def tactical_sound():
    play_commands(remote_sounds_json, "tactical")


def take_sound():
    play_commands(remote_sounds_json, "take")


def talk_sound():
    play_commands(remote_sounds_json, "talk")


def tango_sound():
    play_commands(remote_sounds_json, "tango")


def tank_sound():
    play_commands(remote_sounds_json, "tank")


def target_sound():
    play_commands(remote_sounds_json, "target")


def team_sound():
    play_commands(remote_sounds_json, "team")


def temperature_sound():
    play_commands(remote_sounds_json, "temperature")


def temporal_sound():
    play_commands(remote_sounds_json, "temporal")


def ten_sound():
    play_commands(remote_sounds_json, "ten")


def terminal_sound():
    play_commands(remote_sounds_json, "terminal")


def terminated_sound():
    play_commands(remote_sounds_json, "terminated")


def termination_sound():
    play_commands(remote_sounds_json, "termination")


def test_sound():
    play_commands(remote_sounds_json, "test")


def that_sound():
    play_commands(remote_sounds_json, "that")


def the_sound():
    play_commands(remote_sounds_json, "the")


def then_sound():
    play_commands(remote_sounds_json, "then")


def there_sound():
    play_commands(remote_sounds_json, "there")


def third_sound():
    play_commands(remote_sounds_json, "third")


def thirteen_sound():
    play_commands(remote_sounds_json, "thirteen")


def thirty_sound():
    play_commands(remote_sounds_json, "thirty")


def this_sound():
    play_commands(remote_sounds_json, "this")


def those_sound():
    play_commands(remote_sounds_json, "those")


def thousand_sound():
    play_commands(remote_sounds_json, "thousand")


def threat_sound():
    play_commands(remote_sounds_json, "threat")


def three_sound():
    play_commands(remote_sounds_json, "three")


def through_sound():
    play_commands(remote_sounds_json, "through")


def time_sound():
    play_commands(remote_sounds_json, "time")


def to_sound():
    play_commands(remote_sounds_json, "to")


def top_sound():
    play_commands(remote_sounds_json, "top")


def topside_sound():
    play_commands(remote_sounds_json, "topside")


def touch_sound():
    play_commands(remote_sounds_json, "touch")


def towards_sound():
    play_commands(remote_sounds_json, "towards")


def track_sound():
    play_commands(remote_sounds_json, "track")


def train_sound():
    play_commands(remote_sounds_json, "train")


def transportation_sound():
    play_commands(remote_sounds_json, "transportation")


def truck_sound():
    play_commands(remote_sounds_json, "truck")


def tunnel_sound():
    play_commands(remote_sounds_json, "tunnel")


def turn_sound():
    play_commands(remote_sounds_json, "turn")


def turret_sound():
    play_commands(remote_sounds_json, "turret")


def twelve_sound():
    play_commands(remote_sounds_json, "twelve")


def twenty_sound():
    play_commands(remote_sounds_json, "twenty")


def two_sound():
    play_commands(remote_sounds_json, "two")


def unauthorized_sound():
    play_commands(remote_sounds_json, "unauthorized")


def under_sound():
    play_commands(remote_sounds_json, "under")


def uniform_sound():
    play_commands(remote_sounds_json, "uniform")


def unlocked_sound():
    play_commands(remote_sounds_json, "unlocked")


def until_sound():
    play_commands(remote_sounds_json, "until")


def up_sound():
    play_commands(remote_sounds_json, "up")


def upper_sound():
    play_commands(remote_sounds_json, "upper")


def uranium_sound():
    play_commands(remote_sounds_json, "uranium")


def us_sound():
    play_commands(remote_sounds_json, "us")


def usa_sound():
    play_commands(remote_sounds_json, "usa")


def use_sound():
    play_commands(remote_sounds_json, "use")


def used_sound():
    play_commands(remote_sounds_json, "used")


def user_sound():
    play_commands(remote_sounds_json, "user")


def vacate_sound():
    play_commands(remote_sounds_json, "vacate")


def valid_sound():
    play_commands(remote_sounds_json, "valid")


def vapor_sound():
    play_commands(remote_sounds_json, "vapor")


def vent_sound():
    play_commands(remote_sounds_json, "vent")


def ventillation_sound():
    play_commands(remote_sounds_json, "ventillation")


def victor_sound():
    play_commands(remote_sounds_json, "victor")


def violated_sound():
    play_commands(remote_sounds_json, "violated")


def violation_sound():
    play_commands(remote_sounds_json, "violation")


def voltage_sound():
    play_commands(remote_sounds_json, "voltage")


def vox_login_sound():
    play_commands(remote_sounds_json, "vox_login")


def walk_sound():
    play_commands(remote_sounds_json, "walk")


def wall_sound():
    play_commands(remote_sounds_json, "wall")


def want_sound():
    play_commands(remote_sounds_json, "want")


def wanted_sound():
    play_commands(remote_sounds_json, "wanted")


def warm_sound():
    play_commands(remote_sounds_json, "warm")


def warn_sound():
    play_commands(remote_sounds_json, "warn")


def warning_sound():
    play_commands(remote_sounds_json, "warning")


def waste_sound():
    play_commands(remote_sounds_json, "waste")


def water_sound():
    play_commands(remote_sounds_json, "water")


def we_sound():
    play_commands(remote_sounds_json, "we")


def weapon_sound():
    play_commands(remote_sounds_json, "weapon")


def west_sound():
    play_commands(remote_sounds_json, "west")


def whiskey_sound():
    play_commands(remote_sounds_json, "whiskey")


def white_sound():
    play_commands(remote_sounds_json, "white")


def wilco_sound():
    play_commands(remote_sounds_json, "wilco")


def will_sound():
    play_commands(remote_sounds_json, "will")


def with_sound():
    play_commands(remote_sounds_json, "with")


def without_sound():
    play_commands(remote_sounds_json, "without")


def woop_sound():
    play_commands(remote_sounds_json, "woop")


def xeno_sound():
    play_commands(remote_sounds_json, "xeno")


def yankee_sound():
    play_commands(remote_sounds_json, "yankee")


def yards_sound():
    play_commands(remote_sounds_json, "yards")


def year_sound():
    play_commands(remote_sounds_json, "year")


def yellow_sound():
    play_commands(remote_sounds_json, "yellow")


def yes_sound():
    play_commands(remote_sounds_json, "yes")


def you_sound():
    play_commands(remote_sounds_json, "you")


def your_sound():
    play_commands(remote_sounds_json, "your")


def yourself_sound():
    play_commands(remote_sounds_json, "yourself")


def zero_sound():
    play_commands(remote_sounds_json, "zero")


def zone_sound():
    play_commands(remote_sounds_json, "zone")


def zulu_sound():
    play_commands(remote_sounds_json, "zulu")

# =========== variety of vox announcement system sounds ===============


# TESTING
if __name__ == '__main__':
    bizwarn_sound()
    accelerating_sound()