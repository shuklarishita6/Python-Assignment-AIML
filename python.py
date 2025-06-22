#Python Assignment Questions  

# 1.  Write a Python program to find the second largest number in a list without using the sort() method. 
def second_largest(num):
    if len(num) < 2:
        return None
    a = b = float('-inf')
    for c in num:
        if c > a:
            b = a
            a = c
        elif a > c > b:
            b = c
    return b if b != float('-inf') else None


x = [10, 50, 30, 40]
print(second_largest(x))


# Q2
def kick_dupes_and_sort(stuff):
    final = []
    for x in stuff:
        if x not in final:
            final.append(x)
    return sorted(final)

# Q3
def get_total_and_avg(mylist):
    total = sum(mylist)
    avg = total / len(mylist)
    return total, avg

# Q4
def check_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Q5
def check_chars(msg):
    v_count = c_count = d_count = s_count = 0
    for ch in msg:
        if ch.isdigit(): d_count += 1
        elif ch.isalpha():
            if ch in 'aeiouAEIOU': v_count += 1
            else: c_count += 1
        else: s_count += 1
    return v_count, c_count, d_count, s_count

# Q6
def even_from_1_to_100():
    for i in range(2, 101, 2):
        print(i)

# Q7
def table_maker(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# Q8
def common_3_5():
    return [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]

# Q9
def flip_number(num):
    return int(str(num)[::-1])

# Q10
def char_count_map(st):
    count = {}
    for ch in st:
        count[ch] = count.get(ch, 0) + 1
    return count

# Q11
def first_n_primes_list(n):
    result = []
    num = 2
    while len(result) < n:
        if check_prime(num):
            result.append(num)
        num += 1
    return result

# Q12
def is_num_palindrome(n):
    return str(n) == str(n)[::-1]

# Q13
def how_many_times(mylist, ele):
    return mylist.count(ele)

# Q14
def even_squares_till_50():
    return [x*x for x in range(2, 51, 2)]

# Q15
def get_only_uniques(arr):
    seen = set()
    newlist = []
    for item in arr:
        if item not in seen:
            seen.add(item)
            newlist.append(item)
    return newlist

# Q16
def is_even_or_odd(n):
    return 'Even' if n % 2 == 0 else 'Odd'

# Q17
def running_total(numbers):
    total = 0
    res = []
    for x in numbers:
        total += x
        res.append(total)
    return res

# Q18
def get_fact(n):
    if n == 0:
        return 1
    return n * get_fact(n - 1)

# Q19
def print_fibo_series(terms):
    x, y = 0, 1
    for _ in range(terms):
        print(x, end=' ')
        x, y = y, x + y

# Q20
def check_string_palindrome(word):
    return word == word[::-1]

# Q21
def find_big_small(mylist):
    return max(mylist), min(mylist)

# Q22
def is_pangram_check(msg):
    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(msg.lower()))

# Q23
def get_primes_in_between(start, stop):
    return [i for i in range(start, stop + 1) if check_prime(i)]

# Q24
def count_upper_lower(word):
    upper = sum(1 for ch in word if ch.isupper())
    lower = sum(1 for ch in word if ch.islower())
    return upper, lower

# Q25
def digits_sum(number):
    return sum(int(d) for d in str(number))

# Q26
def total_words(text):
    return len(text.split())

# Q27
def wipe_punct(msg):
    import string
    return ''.join(ch for ch in msg if ch not in string.punctuation)

# Q28
def get_gcd(x, y):
    while y:
        x, y = y, x % y
    return x

# Q29
def find_dupes(items):
    seen = set()
    dups = set()
    for item in items:
        if item in seen:
            dups.add(item)
        else:
            seen.add(item)
    return list(dups)

# Q30
def biggest_of_3(a, b, c):
    return max(a, b, c)

# Q31
def sort_sentence_words(msg):
    return ' '.join(sorted(msg.split()))

# Q32
def combine_2_dicts(dict1, dict2):
    return {**dict1, **dict2}

# Q33
def vowel_count_in_words(sentence):
    result = {}
    for word in sentence.split():
        result[word] = sum(1 for ch in word if ch in 'aeiouAEIOU')
    return result

# Q34
def tuple_to_list_converter(tp):
    return list(tp)

# Q35
def remove_spaces(st):
    return ''.join(st.split())

# Q36
def zip_lists_to_dict(keys, values):
    return dict(zip(keys, values))

# Q37
def get_max_key_by_val(d):
    return max(d, key=d.get)

# Q38
def word_count_dict(line):
    words = line.split()
    wordmap = {}
    for word in words:
        wordmap[word] = wordmap.get(word, 0) + 1
    return wordmap

# Q39
def check_if_key_there(dic, key):
    return key in dic

# Q40
def change_vowels_to_star(text):
    return ''.join('*' if ch in 'aeiouAEIOU' else ch for ch in text)

# Q41
def read_txt_file(path):
    with open(path, 'r') as f:
        return f.read()

# Q42
def count_words_in_file(path):
    with open(path, 'r') as f:
        return len(f.read().split())

# Q43
def copy_file_content(from_file, to_file):
    with open(from_file, 'r') as f1, open(to_file, 'w') as f2:
        f2.write(f1.read())

# Q44
def get_long_lines(file_path):
    with open(file_path, 'r') as f:
        return [line.strip() for line in f if len(line.strip()) > 50]

# Q45
def save_list_to_file(list_data, file_path):
    with open(file_path, 'w') as f:
        for line in list_data:
            f.write(line + '\n')

# Q46
def divide_two_nums(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Can't divide by zero"

# Q47
def get_user_number():
    try:
        return int(input("Enter a number: "))
    except ValueError:
        return "Invalid input"

# Q48
def safe_open_file(name):
    try:
        with open(name, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "File not found"

# Q49
def safe_index(lst, index):
    try:
        return lst[index]
    except IndexError:
        return "Invalid index"

# Q50
def try_except_demo():
    try:
        print("Trying stuff")
    except:
        print("Caught something")
    finally:
        print("Always runs finally")