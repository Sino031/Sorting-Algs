import pygame
import random
import threading
import time
import numpy as np

pygame.init()

WIDTH = 1024
HEIGHT = 512
FPS = 60
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sorting Algorithm Visualizer")
clock = pygame.time.Clock()

current_title = "Sorting Algorithm Visualizer"

pygame.mixer.init()
pygame.mixer.music.load("Soviet-Union-Anthem-Sound-Effect.mp3")

def nearest_power_of_2(n):
    return 2 ** (n - 1).bit_length()

sample_list = [i for i in range(1, 129)]
random.shuffle(sample_list)

big_list = False if len(sample_list) < 512 else True

desired_size = nearest_power_of_2(len(sample_list))
if len(sample_list) > desired_size:
    sample_list = sample_list[:desired_size]

banner_width = 256
banner_height = 64
banner_x, banner_y = 0, 0

def draw_list(screen, list_object, highlighted_indicies=[], highlighted_color=RED, exception_indicies=[], exception_color=GREEN):
    screen.fill(BLACK)
    total_bars = len(list_object)
    bar_width = WIDTH // total_bars
    scaling_factor = HEIGHT / max(sample_list)
    current_x = 0

    for i, value in enumerate(list_object):
        if i in highlighted_indicies:
            color = highlighted_color
        elif i in exception_indicies:
            color = exception_color
        else:
            color = WHITE
        bar_height = int(value * scaling_factor)
        y_position = HEIGHT - bar_height
        
        pygame.draw.rect(screen, color, (current_x, y_position, bar_width, bar_height))
        current_x = (i + 1) * bar_width

def play_sound(value, max_value):
    frequency = 200 + (value / max_value) * 1800
    sample_rate = 44100
    duration = 0.1

    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)

    sound = np.int16(wave * 32767)
    sound = np.repeat(sound[:, np.newaxis], 2, axis=1)

    pygame.mixer.init(frequency=sample_rate, size=-16, channels=2)
    sound_obj = pygame.sndarray.make_sound(sound)
    sound_obj.play()

sorting_states = {
    'bubble_sort': False,
    'selection_sort': False,
    'insertion_sort': False,
    'merge_sort': False,
    'quick_sort': False,
    'bucket_sort': False,
    'stalin_sort': False,
    'bogo_sort': False,
    'sleep_sort': False,
    'slow_sort': False,
    'bozo_sort': False,
    'bogo_bogo_sort': False,
    'quantum_bogo_sort': False,
    'schrodinger_sort': False,
    'intelligent_design_sort': False,
    'miracle_sort': False
}

def bubble_sort(screen, list_object):
    n = len(list_object)
    for i in range(n):
        for j in range(n - i - 1):
            if list_object[j] > list_object[j + 1]:
                list_object[j], list_object[j + 1] = list_object[j + 1], list_object[j]
                draw_list(screen, list_object, [j, j + 1])
                play_sound(list_object[j + 1], max(list_object))
                pygame.time.delay(25)
    
    l = []
    for i in range(n):
        draw_list(screen, list_object, [i], exception_indicies=l)
        play_sound(list_object[i], max(list_object))
        l.append(i)
        if not big_list:
            pygame.time.delay(25)
        else:
            pygame.time.delay(3)

def selection_sort(screen, list_object):
    n = len(list_object)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if list_object[j] < list_object[min_idx]:
                min_idx = j
        list_object[i], list_object[min_idx] = list_object[min_idx], list_object[i]
        draw_list(screen, list_object, [i, min_idx])
        play_sound(list_object[min_idx], max(list_object))
        pygame.time.delay(25)

    l = []
    for i in range(n):
        draw_list(screen, list_object, [i], exception_indicies=l)
        play_sound(list_object[i], max(list_object))
        l.append(i)
        if not big_list:
            pygame.time.delay(25)
        else:
            pygame.time.delay(3)

def insertion_sort(screen, list_object):
    n = len(list_object)
    for i in range(1, n):
        j = i - 1
        key = list_object[i]
        if list_object[j] > key:
            while j >= 0 and list_object[j] > key:
                list_object[j], list_object[j + 1] = list_object[j + 1], list_object[j]
                j -= 1
        draw_list(screen, list_object, [j + 1])
        play_sound(list_object[j + 1], max(list_object))
        pygame.time.delay(25)

    l = []
    for i in range(n):
        draw_list(screen, list_object, [i], exception_indicies=l)
        play_sound(list_object[i], max(list_object))
        l.append(i)
        if not big_list:
            pygame.time.delay(25)
        else:
            pygame.time.delay(3)

def merge_sort(screen, list_object, start=0, end=None):
    if end is None:
        end = len(list_object)
    if end - start > 1:
        mid = (start + end) // 2
        left_half = list_object[start:mid]
        right_half = list_object[mid:end]

        merge_sort(screen, list_object, start, mid)
        merge_sort(screen, list_object, mid, end)

        i = start
        j = mid
        k = 0
        temp = []
        while i < mid and j < end:
            if list_object[i] < list_object[j]:
                temp.append(list_object[i])
                i += 1
            else:
                temp.append(list_object[j])
                j += 1
        
        while i < mid:
            temp.append(list_object[i])
            i += 1
        while j < len(right_half):
            temp.append(list_object[j])
            j += 1
        
        for k, value in enumerate(temp):
            list_object[start + k] = value
            draw_list(screen, list_object, [start + k])
            play_sound(list_object[start + k], max(list_object))
            pygame.time.delay(25)
    
    if start == 0 and end == len(list_object):
        l = []
        for i in range(len(list_object)):
            draw_list(screen, list_object, [i], exception_indicies=l)
            play_sound(list_object[i], max(list_object))
            l.append(i)
            if not big_list:
                pygame.time.delay(25)
            else:
                pygame.time.delay(3)

def quick_sort(screen, list_object, low=0, high=None):
    if high is None:
        high = len(list_object) - 1
    if low < high:
        pivot_index = partition(screen, list_object, low, high)

        quick_sort(screen, list_object, low, pivot_index - 1)
        quick_sort(screen, list_object, pivot_index + 1, high)
    if low == 0 and high == len(list_object) - 1:
        l = []
        for i in range(len(list_object)):
            draw_list(screen, list_object, [i], exception_indicies=l)
            play_sound(list_object[i], max(list_object))
            l.append(i)
            if not big_list:
                pygame.time.delay(25)
            else:
                pygame.time.delay(3)

def partition(screen, list_object, low, high):
    pivot = list_object[high]
    i = low - 1
    for j in range(low, high):
        draw_list(screen, list_object, [j, high])
        play_sound(list_object[j], max(list_object))
        pygame.time.delay(25)
        if list_object[j] < pivot:
            i += 1
            list_object[i], list_object[j] = list_object[j], list_object[i]
            draw_list(screen, list_object, [i, j])
            play_sound(list_object[i], max(list_object))
            pygame.time.delay(25)
    list_object[i + 1], list_object[high] = list_object[high], list_object[i + 1]
    draw_list(screen, list_object, [i + 1, high])
    play_sound(list_object[i + 1], max(list_object))
    pygame.time.delay(25)
    return i + 1

def bucket_sort(screen, list_object):
    max_value = max(list_object)
    size = len(list_object)

    buckets = [[] for _ in range(size)]

    for value in list_object:
        index = min(int(value / max_value * size), size - 1)
        buckets[index].append(value)
        draw_list(screen, list_object, [list_object.index(value)])  
        play_sound(value, max_value)
        pygame.time.delay(25)

    sorted_list = []
    for i, bucket in enumerate(buckets):
        for j in range(1, len(bucket)):
            key = bucket[j]
            k = j - 1
            while k >= 0 and key < bucket[k]:
                bucket[k + 1] = bucket[k]
                k -= 1
            bucket[k + 1] = key

        for value in bucket:
            sorted_list.append(value)
            combined_list = sorted_list + [item for sublist in buckets[i + 1:] for item in sublist]

    for i in range(len(list_object)):
        list_object[i] = sorted_list[i]
        draw_list(screen, list_object, [i])
        play_sound(list_object[i], max(list_object))
        pygame.time.delay(25)
    
    l = []
    for i in range(len(list_object)):
        draw_list(screen, list_object, [i], exception_indicies=l)
        play_sound(list_object[i], max(list_object))
        l.append(i)
        if not big_list:
            pygame.time.delay(25)
        else:
            pygame.time.delay(3)

def stalin_sort(screen, list_object):
    n = len(list_object)
    sorted_list = [list_object[0]]
    discarded_indices = []

    quotes = [
        "Sent to gulag",
        "Long live the great Soviet Union",
        "All hail the great leader",
        "The people are happy",
        "The state is strong",
        "The revolution is victorious",
        "The party is infallible",
        "The people are united",
        "The future is bright",
        "The motherland is secure",
        "The great leader is wise",
        "The people are loyal",
        "They were sent to the gulag, reason: they looked at the leader wrong",
        "They were sent to the gulag, reason: they were not happy enough",
        "They said Stalin had a stroke and was unfit for office currently and had to go to the hospital",
        "The revolution does not tolerate weakness.",
        "Comrade, you have failed the party.",
        "Only the strong shall remain.",
        "The motherland thanks you for your service.",
        "You have been found guilty of treason.",
        "Your loyalty is in question.",
        "You are too american.",
        "The KGB discovered you own jeans.",
        "You are too capitalist.",
        "You played monopoly instead of monopoly communist edition.",
        "You are too individualistic.",
        "You are too western.",
        "The party does not tolerate dissent.",
        "The KGB is watching you.",
        "You are a traitor to the revolution.",
        "You were deemed unfit for service.",
        "You were deemed a threat to the state.",
        "You were deemed a threat to the party.",
        "You were deemed a threat to the people.",
        "You were deemed a threat to the motherland.",
        "You were found guilty of being too happy.",
        """You were found guilty of being too sad.
You were found guilty of being too happy.
You were found guilty of being too neutral.
You were found guilty of being too angry.""",
        """You were found guilty of not having emotions.
You were found guilty of being too emotional.""",
        """You were found guilty of being too rational.
You were found guilty of being too irrational.""",
        """You were found guilty of being too logical.
You were found guilty of being too illogical.""",
        "You were found guilty of.. nothing at all.",
        "You were found guilty of having bad humor.",
        "You were found guilty of being too funny.",
        "You were found guilty of being too serious.",
        "You were found guilty of being too silly.",
        "You were found guilty of being too boring.",
        "You were found guilty of being too interesting.",
        "Your radio was too loud.",
        "Your radio was too quiet.",
        "Your radio was too static.",
        "Your radio was too clear.",
        "Your radio picked up western music.",
        "Your radio picked up western news."
    ]
    pygame.mixer.music.play(-1)
    for i in range(1, n):
        if list_object[i] >= sorted_list[-1]:
            sorted_list.append(list_object[i])
        else:
            discarded_indices.append(i)
            message = random.choice(quotes)
            print(message)

        draw_list(screen, list_object, discarded_indices + [len(sorted_list) - 1])
        pygame.time.delay(50)
    draw_list(screen, list_object, discarded_indices)
    pygame.mixer.music.stop()

def bogo_sort(screen, list_object):
    max_value = max(list_object)
    while not is_sorted(list_object):
        random.shuffle(list_object)
        draw_list(screen, list_object)

        random_value = random.choice(list_object)
        play_sound(random_value, max_value)
        pygame.time.delay(25)
    
    l = []
    for i in range(len(list_object)):
        draw_list(screen, list_object, [i], exception_indicies=l)
        play_sound(list_object[i], max_value)
        l.append(i)
        if not big_list:
            pygame.time.delay(25)
        else:
            pygame.time.delay(3)

def sleep_sort(screen, list_object):
    sorted_list = []

    def print_and_append(n):
        time.sleep(n)
        sorted_list.append(n)
        draw_list(screen, sorted_list + [0] * (len(list_object) - len(sorted_list)), [len(sorted_list) - 1])
        play_sound(n, max(list_object))
        pygame.time.delay(25)

    threads = [threading.Thread(target=print_and_append, args=(n,)) for n in list_object]

    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

    for i in range(len(list_object)):
        list_object[i] = sorted_list[i]
    
    l = []
    for i in range(len(list_object)):
        draw_list(screen, list_object, [i], exception_indicies=l)
        play_sound(list_object[i], max(list_object))
        l.append(i)
        if not big_list:
            pygame.time.delay(25)
        else:
            pygame.time.delay(3)

final_pass_done = False

def slow_sort(screen, list_object, start=0, end=None):
    global final_pass_done
    if end is None:
        end = len(list_object)
    
    if end - start <= 1:
        return
    if is_sorted(list_object[start:end]):
        return
    
    mid = (start + end) // 2
    slow_sort(screen, list_object, start, mid)
    slow_sort(screen, list_object, mid, end)

    if list_object[mid - 1] > list_object[mid]:
        list_object[mid - 1], list_object[mid] = list_object[mid], list_object[mid - 1]
        draw_list(screen, list_object, [mid - 1, mid])
        play_sound(list_object[mid], max(list_object))
        pygame.time.delay(25)

    if is_sorted(list_object[start:end]):
        return
    
    slow_sort(screen, list_object, start, end)

    if start == 0 and end == len(list_object) and not final_pass_done:
        l = []
        for i in range(len(list_object)):
            draw_list(screen, list_object, [i], exception_indicies=l)
            play_sound(list_object[i], max(list_object))
            l.append(i)
            if not big_list:
                pygame.time.delay(25)
            else:
                pygame.time.delay(3)
        final_pass_done = True

def bozo_sort(screen, list_object):
    while not is_sorted(list_object):
        i = random.randint(0, len(list_object) - 1)
        j = random.randint(0, len(list_object) - 1)
        while j == i:
            j = random.randint(0, len(list_object) - 1)
        list_object[i], list_object[j] = list_object[j], list_object[i]
        draw_list(screen, list_object, [i, j])
        play_sound(list_object[random.choice([i, j])], max(list_object))
        pygame.time.delay(25)
    
    l = []
    for i in range(len(list_object)):
        draw_list(screen, list_object, [i], exception_indicies=l)
        play_sound(list_object[i], max(list_object))
        l.append(i)
        if not big_list:
            pygame.time.delay(25)
        else:
            pygame.time.delay(3)

def bogo_bogo_sort(screen, list_object):
    while not is_sorted(list_object):
        for i in range(len(list_object)):
            if not is_sorted(list_object[:i + 1]):
                break
        else:
            return
        prefix = list_object[:i + 1]
        random.shuffle(prefix)
        list_object[:i + 1] = prefix
        draw_list(screen, list_object, list(range(i + 1)))
        play_sound(list_object[random.randint(1, i)], max(list_object))
        pygame.time.delay(25)
    
    l = []
    for i in range(len(list_object)):
        draw_list(screen, list_object, [i], exception_indicies=l)
        play_sound(list_object[i], max(list_object))
        l.append(i)
        if not big_list:
            pygame.time.delay(25)
        else:
            pygame.time.delay(3)

def quantum_bogo_sort(screen, list_object):
    draw_list(screen, list_object)
    pygame.time.delay(500)

    list_object.sort()
    for _ in range(10):
        play_sound(list_object[random.randint(0, len(list_object) - 1)], max(list_object))
        pygame.time.delay(50)
    
    print("Found parallel universes where the list is sorted.")

    draw_list(screen, list_object)
    pygame.time.delay(500)
    for i in range(len(list_object)):
        draw_list(screen, list_object, [i])
        play_sound(list_object[i], max(list_object))
        pygame.time.delay(25)
    
    l = []
    for i in range(len(list_object)):
        draw_list(screen, list_object, [i], exception_indicies=l)
        play_sound(list_object[i], max(list_object))
        l.append(i)
        if not big_list:
            pygame.time.delay(25)
        else:
            pygame.time.delay(3)

def schrodinger_sort(screen, list_object):
    draw_list(screen, list_object)
    pygame.time.delay(500)

    for _ in range(10):
        random.shuffle(list_object)
        draw_list(screen, list_object)
        play_sound(list_object[random.randint(0, len(list_object) - 1)], max(list_object))
        pygame.time.delay(100)
    
    if random.random() < 0.5:
        list_object.sort()
        message = "The list has collapsed into a sorted state."
    else:
        random.shuffle(list_object)
        message = "The list has collapsed into an unsorted state."

    draw_list(screen, list_object)
    pygame.time.delay(500)

    if is_sorted(list_object):
        l = []
        for i in range(len(list_object)):
            draw_list(screen, list_object, [i], exception_indicies=l)
            play_sound(list_object[i], max(list_object))
            l.append(i)
            if not big_list:
                pygame.time.delay(25)
            else:
                pygame.time.delay(3)

    print(message)

def intelligent_design_sort(screen, list_object):
    draw_list(screen, list_object)
    pygame.time.delay(500)

    for i in range(len(list_object)):
        draw_list(screen, list_object, [i])
        play_sound(list_object[i], max(list_object))
        pygame.time.delay(25)

    if is_sorted(list_object):
        message = "The list is sorted becuase it was intelligently designed to be so."
    else:
        message = "The list is sorted. If it's not sorted, it is because you are not smart enough to understand it."
    
    l = []
    for i in range(len(list_object)):
        draw_list(screen, list_object, [i], exception_indicies=l)
        play_sound(list_object[i], max(list_object))
        l.append(i)
        if not big_list:
            pygame.time.delay(25)
        else:
            pygame.time.delay(3)
    
    print(message)

def miracle_sort(screen, list_object):
    draw_list(screen, list_object)
    pygame.time.delay(500)
    while not is_sorted(list_object):
        pygame.time.delay(1000)
        miracle_messages = [
            "Praying for divine intervention...",
            "Asking for a miracle...",
            "Hoping for solar rays to align...",
            "Wishing for a miracle...",
            "Waiting for the universe to sort itself out...",
            "Maybe a miracle will happen...",
            "Still waiting... any second now..."
        ]
        message = random.choice(miracle_messages)
        print(message)
    
    for i in range(len(list_object)):
        draw_list(screen, list_object, [i])
        play_sound(list_object[i], max(list_object))
        pygame.time.delay(25)
    
    l = []
    for i in range(len(list_object)):
        draw_list(screen, list_object, [i], exception_indicies=l)
        play_sound(list_object[i], max(list_object))
        l.append(i)
        if not big_list:
            pygame.time.delay(25)
        else:
            pygame.time.delay(3)
    
    print("NO WAY! IT WORKED! A MIRACLE HAPPENED!")

def radix_sort(screen, list_object):
    max_value = max(list_object)
    exp = 1
    while max_value // exp > 0:
        counting_sort(screen, list_object, exp)
        exp *= 10
    
    l = []
    for i in range(len(list_object)):
        draw_list(screen, list_object, [i], exception_indicies=l)
        play_sound(list_object[i], max(list_object))
        l.append(i)
        if not big_list:
            pygame.time.delay(25)
        else:
            pygame.time.delay(3)

def counting_sort(screen, list_object, exp):
    n = len(list_object)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = list_object[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = list_object[i] // exp
        output[count[index % 10] - 1] = list_object[i]
        count[index % 10] -= 1

    for i in range(n):
        list_object[i] = output[i]
        draw_list(screen, list_object, [i])
        play_sound(list_object[i], max(list_object))
        pygame.time.delay(25)

def cocktail_shaker_sort(screen, list_object):
    n = len(list_object)
    start = 0
    end = n - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(start, end):
            if list_object[i] > list_object[i + 1]:
                list_object[i], list_object[i + 1] = list_object[i + 1], list_object[i]
                swapped = True
                draw_list(screen, list_object, [i, i + 1])
                play_sound(list_object[i], max(list_object))
                pygame.time.delay(25)
        if not swapped:
            break
    
        end -= 1
        swapped = False

        for i in range(end, start, -1):
            if list_object[i] < list_object[i - 1]:
                list_object[i], list_object[i - 1] = list_object[i - 1], list_object[i]
                swapped = True
                draw_list(screen, list_object, [i, i - 1])
                play_sound(list_object[i], max(list_object))
                pygame.time.delay(25)

        start += 1
    
    l = []
    for i in range(n):
        draw_list(screen, list_object, [i], exception_indicies=l)
        play_sound(list_object[i], max(list_object))
        l.append(i)
        if not big_list:
            pygame.time.delay(25)
        else:
            pygame.time.delay(3)

def is_sorted(list_object):
    for i in range(len(list_object) - 1):
        if list_object[i] > list_object[i + 1]:
            return False
    return True

def start_bubble_sort():
    sorting_states['bubble_sort'] = True
    print("Bubble Sort started")
    bubble_sort(screen, sample_list)
    sorting_states['bubble_sort'] = False
    print("Bubble Sort finished")
    draw_list(screen, sample_list)

def start_selection_sort():
    sorting_states['selection_sort'] = True
    print("Selection Sort started")
    selection_sort(screen, sample_list)
    sorting_states['selection_sort'] = False
    print("Selection Sort finished")
    draw_list(screen, sample_list)

def start_insertion_sort():
    sorting_states['insertion_sort'] = True
    print("Insertion Sort started")
    insertion_sort(screen, sample_list)
    sorting_states['insertion_sort'] = False
    print("Insertion Sort finished")
    draw_list(screen, sample_list)

def start_merge_sort():
    sorting_states['merge_sort'] = True
    print("Merge Sort started")
    merge_sort(screen, sample_list)
    sorting_states['merge_sort'] = False
    print("Merge Sort finished")
    draw_list(screen, sample_list)

def start_quick_sort():
    sorting_states['quick_sort'] = True
    print("Quick Sort started")
    quick_sort(screen, sample_list)
    sorting_states['quick_sort'] = False
    print("Quick Sort finished")
    draw_list(screen, sample_list)

def start_bucket_sort():
    global current_title
    sorting_states['bucket_sort'] = True
    print("Bucket Sort started")
    bucket_sort(screen, sample_list)
    sorting_states['bucket_sort'] = False
    print("Bucket Sort finished")
    draw_list(screen, sample_list)

def start_stalin_sort():
    sorting_states['stalin_sort'] = True
    print("Stalin Sort started")
    stalin_sort(screen, sample_list)
    sorting_states['stalin_sort'] = False
    print("LONG LIVE THE GREAT SOVIET UNION")

def start_bogo_sort():
    sorting_states['bogo_sort'] = True
    print("Bogo Sort started")
    bogo_sort(screen, sample_list)
    sorting_states['bogo_sort'] = False
    print("Bogo Sort finished")
    draw_list(screen, sample_list)

def start_sleep_sort():
    sorting_states['sleep_sort'] = True
    print("Sleep Sort started")
    sleep_sort(screen, sample_list)
    sorting_states['sleep_sort'] = False
    print("Sleep Sort finished")
    draw_list(screen, sample_list)

def start_slow_sort():
    sorting_states['slow_sort'] = True
    print("Slow Sort started")
    slow_sort(screen, sample_list)
    sorting_states['slow_sort'] = False
    print("Slow Sort finished")
    draw_list(screen, sample_list)

def start_bozo_sort():
    sorting_states['bozo_sort'] = True
    print("Bozo Sort started")
    bozo_sort(screen, sample_list)
    sorting_states['bozo_sort'] = False
    print("Bozo Sort finished")
    draw_list(screen, sample_list)

def start_bogo_bogo_sort():
    sorting_states['bogo_bogo_sort'] = True
    print("Bogo Bogo Sort started")
    bogo_bogo_sort(screen, sample_list)
    sorting_states['bogo_bogo_sort'] = False
    print("Bogo Bogo Sort finished")
    draw_list(screen, sample_list)

def start_quantum_bogo_sort():
    sorting_states['quantum_bogo_sort'] = True
    print("Quantum Bogo Sort started")
    quantum_bogo_sort(screen, sample_list)
    sorting_states['quantum_bogo_sort'] = False
    print("Quantum Bogo Sort finished")
    draw_list(screen, sample_list)

def start_schrodinger_sort():
    sorting_states['schrodinger_sort'] = True
    print("Schrodinger Sort started")
    schrodinger_sort(screen, sample_list)
    sorting_states['schrodinger_sort'] = False
    print("Schrodinger Sort finished")
    draw_list(screen, sample_list)

def start_intelligent_design_sort():
    sorting_states['intelligent_design_sort'] = True
    print("Intelligent Design Sort started")
    intelligent_design_sort(screen, sample_list)
    sorting_states['intelligent_design_sort'] = False
    print("Intelligent Design Sort finished")
    draw_list(screen, sample_list)

def start_miracle_sort():
    sorting_states['miracle_sort'] = True
    print("Miracle Sort started")
    miracle_sort(screen, sample_list)
    sorting_states['miracle_sort'] = False
    print("Miracle Sort finished")
    draw_list(screen, sample_list)

def start_radix_sort():
    sorting_states['radix_sort'] = True
    print("Radix Sort started")
    radix_sort(screen, sample_list)
    sorting_states['radix_sort'] = False
    print("Radix Sort finished")
    draw_list(screen, sample_list)

def start_cocktail_shaker_sort():
    sorting_states['cocktail_shaker_sort'] = True
    print("Cocktail Shaker Sort started")
    cocktail_shaker_sort(screen, sample_list)
    sorting_states['cocktail_shaker_sort'] = False
    print("Cocktail Shaker Sort finished")
    draw_list(screen, sample_list)

def is_any_sorting():
    return any(sorting_states.values())

def show_epilepsy_warning(screen):
    screen.fill(BLACK)
    font = pygame.font.Font(None, 36)
    warning_text = [
        "WARNING: This program contains flashing lights",
        "and rapid visual changes that may trigger",
        "photosensitive epilepsy in some individuals.",
        "",
        "Press any key to continue..."
    ]
    y_offset = HEIGHT // 2 - len(warning_text) * 20
    for line in warning_text:
        text_surface = font.render(line, True, WHITE)
        text_rect = text_surface.get_rect(center=(WIDTH // 2, y_offset))
        screen.blit(text_surface, text_rect)
        y_offset += 40

    pygame.display.update()

    # Wait for the user to press a key
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                waiting = False

sorting = False
running = True
show_epilepsy_warning(screen)
draw_list(screen, sample_list)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_b and not is_any_sorting():
                threading.Thread(target=start_bubble_sort, daemon=True).start()
            elif event.key == pygame.K_s and not is_any_sorting():
                threading.Thread(target=start_selection_sort, daemon=True).start()
            elif event.key == pygame.K_i and not is_any_sorting():
                threading.Thread(target=start_insertion_sort, daemon=True).start()
            elif event.key == pygame.K_m and not is_any_sorting():
                threading.Thread(target=start_merge_sort, daemon=True).start()
            elif event.key == pygame.K_q and not is_any_sorting():
                threading.Thread(target=start_quick_sort, daemon=True).start()
            elif event.key == pygame.K_u and not is_any_sorting():
                threading.Thread(target=start_bucket_sort, daemon=True).start()
            elif event.key == pygame.K_1 and not is_any_sorting():
                threading.Thread(target=start_stalin_sort, daemon=True).start()
            elif event.key == pygame.K_2 and not is_any_sorting():
                threading.Thread(target=start_sleep_sort, daemon=True).start()
            elif event.key == pygame.K_3 and not is_any_sorting():
                threading.Thread(target=start_slow_sort, daemon=True).start()
            elif event.key == pygame.K_4 and not is_any_sorting():
                threading.Thread(target=start_bogo_sort, daemon=True).start()
            elif event.key == pygame.K_5 and not is_any_sorting():
                threading.Thread(target=start_bozo_sort, daemon=True).start()
            elif event.key == pygame.K_6 and not is_any_sorting():
                threading.Thread(target=start_bogo_bogo_sort, daemon=True).start()
            elif event.key == pygame.K_7 and not is_any_sorting():
                threading.Thread(target=start_quantum_bogo_sort, daemon=True).start()
            elif event.key == pygame.K_8 and not is_any_sorting():
                threading.Thread(target=start_schrodinger_sort, daemon=True).start()
            elif event.key == pygame.K_9 and not is_any_sorting():
                threading.Thread(target=start_intelligent_design_sort, daemon=True).start()
            elif event.key == pygame.K_0 and not is_any_sorting():
                threading.Thread(target=start_miracle_sort, daemon=True).start()
            elif event.key == pygame.K_r and not is_any_sorting():
                threading.Thread(target=start_radix_sort, daemon=True).start()
            elif event.key == pygame.K_c and not is_any_sorting():
                threading.Thread(target=start_cocktail_shaker_sort, daemon=True).start()
            elif event.key == pygame.K_UP and not is_any_sorting() and len(sample_list) != 1024:
                n = (len(sample_list) * 2) + 1
                sample_list = [i for i in range(1, n)]
                random.shuffle(sample_list)
                draw_list(screen, sample_list)
                big_list = False if len(sample_list) < 512 else True
            elif event.key == pygame.K_DOWN and not is_any_sorting() and len(sample_list) != 2:
                n = (len(sample_list) // 2) + 1
                sample_list = [i for i in range(1, n)]
                random.shuffle(sample_list)
                draw_list(screen, sample_list)
                big_list = False if len(sample_list) < 512 else True
            elif event.key == pygame.K_TAB and not is_any_sorting():
                sample_list = sample_list[::-1]
                draw_list(screen, sample_list)
            elif (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT) and not is_any_sorting():
                for i in range(1, 6):
                    random.shuffle(sample_list)
                    draw_list(screen, sample_list)
                    pygame.display.update()
                    pygame.time.delay(100) 
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()
