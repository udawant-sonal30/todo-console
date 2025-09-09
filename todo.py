# todo.py
import json
from pathlib import Path

DB_PATH = Path("storage.json")   # data जतन होईल

# ----- Helper Functions -----
def load_tasks():
    """storage.json मधून tasks लोड करणे"""
    if DB_PATH.exists():
        try:
            return json.loads(DB_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []
    return []

def save_tasks(tasks):
    """tasks storage.json मध्ये सेव्ह करणे"""
    DB_PATH.write_text(json.dumps(tasks, ensure_ascii=False, indent=2), encoding="utf-8")

# ----- Menu Display -----
def show_menu():
    print("\n==== TO-DO LIST ====")
    print("1) Add task")
    print("2) List tasks")
    print("3) Mark task complete")
    print("4) Delete task")
    print("5) Clear all tasks")
    print("6) Exit")

# ----- Features -----
def list_tasks(tasks):
    if not tasks:
        print("No tasks yet.")
        return
    print("\n#  Status  Task")
    print("-- ------- ----------------------------")
    for i, t in enumerate(tasks, start=1):
        status = "✅" if t.get("done") else "⬜"
        print(f"{i:>2}  {status:>5}   {t.get('title')}")

def add_task(tasks):
    title = input("Task title: ").strip()
    if not title:
        print("Empty task ignored.")
        return
    tasks.append({"title": title, "done": False})
    save_tasks(tasks)
    print("Task added!")

def mark_complete(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        n = int(input("Enter task number to mark complete: ").strip())
        if 1 <= n <= len(tasks):
            tasks[n-1]["done"] = True
            save_tasks(tasks)
            print("Task marked complete!")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")

def delete_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    try:
        n = int(input("Enter task number to delete: ").strip())
        if 1 <= n <= len(tasks):
            removed = tasks.pop(n-1)
            save_tasks(tasks)
            print(f"Deleted: {removed['title']}")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a number.")

def clear_all(tasks):
    if not tasks:
        print("Nothing to clear.")
        return
    confirm = input("Are you sure? Type YES to confirm: ").strip()
    if confirm == "YES":
        tasks.clear()
        save_tasks(tasks)
        print("All tasks cleared.")
    else:
        print("Canceled.")

# ----- Main -----
def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose (1-6): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            clear_all(tasks)
        elif choice == "6":
            print("Bye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
