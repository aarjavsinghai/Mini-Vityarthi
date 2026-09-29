import os


DATA_DIR = "data"
RESULTS_FILE = os.path.join(DATA_DIR, "results.txt")
BOOKMARK_FILE = os.path.join(DATA_DIR, "bookmarks.txt")


def ensure_files():
    # create folder and files if they dont exist
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    for path in (RESULTS_FILE, BOOKMARK_FILE):
        if not os.path.exists(path):
            with open(path, "w", encoding="utf-8") as f:
                pass


def clean(value):
    
    text = str(value)
    text = text.replace("\n", " ")
    text = text.replace("|", "/")
    return text


def save_result(source, topic, question, user_answer, correct_answer, correct, explanation):
    ensure_files()
    row = [source, topic, question, user_answer, correct_answer, correct, explanation]
    cleaned = [clean(item) for item in row]
    line = "|".join(cleaned)

    with open(RESULTS_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def read_results():
    ensure_files()
    results = []

    with open(RESULTS_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.rstrip("\n").split("|")
            if len(parts) != 7:
                continue   # skip broken lines

            record = {
                "source": parts[0],
                "topic": parts[1],
                "question": parts[2],
                "user_answer": parts[3],
                "correct_answer": parts[4],
                "correct": int(parts[5]),
                "explanation": parts[6],
            }
            results.append(record)

    return results


def add_bookmark(source, topic, question, answer):
    ensure_files()
    row = [source, topic, question, answer]
    cleaned = [clean(item) for item in row]
    line = "|".join(cleaned)

    with open(BOOKMARK_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")


def read_bookmarks():
    ensure_files()
    bookmarks = []

    with open(BOOKMARK_FILE, "r", encoding="utf-8") as f:
        for line in f:
            parts = line.rstrip("\n").split("|")
            if len(parts) == 4:
                bookmarks.append(tuple(parts))

    return bookmarks


def is_bookmarked(question):
    cleaned_question = clean(question)
    for bookmark in read_bookmarks():
        if bookmark[2] == cleaned_question:
            return True
    return False


def get_statistics():
    results = read_results()

    attempted = len(results)
    correct = 0
    for item in results:
        correct += item["correct"]
    wrong = attempted - correct

    if attempted > 0:
        accuracy = correct / attempted * 100
    else:
        accuracy = 0

    
    topic_data = {}
    for item in results:
        topic = item["topic"]
        if topic not in topic_data:
            topic_data[topic] = [0, 0]
        topic_data[topic][0] += 1
        topic_data[topic][1] += item["correct"]

    return attempted, correct, wrong, accuracy, topic_data


def reset_progress():
    ensure_files()
    # just open in write mode to clear everything
    with open(RESULTS_FILE, "w", encoding="utf-8") as f:
        pass
    with open(BOOKMARK_FILE, "w", encoding="utf-8") as f:
        pass
