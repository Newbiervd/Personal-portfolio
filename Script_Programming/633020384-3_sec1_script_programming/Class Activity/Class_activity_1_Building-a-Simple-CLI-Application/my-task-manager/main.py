"""
Main Entry Point: Task Manager CLI Application
Week 7: Building a Simple CLI Application, Error Handling & Project Structure
"""

import sys
import os

# Add the 'src' directory to sys.path so modules can be imported directly
SRC_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
if SRC_PATH not in sys.path:
    sys.path.insert(0, SRC_PATH)

import task_data
import task_logic


def display_menu() -> None:
    """Displays the interactive CLI menu options."""
    print("\n" + "=" * 34)
    print("        TASK MANAGER CLI          ")
    print("=" * 34)
    print("  1. Add New Task")
    print("  2. List All Tasks")
    print("  3. List Pending Tasks")
    print("  4. List Completed Tasks")
    print("  5. Search Tasks by Keyword")
    print("  6. Mark Task as Completed")
    print("  7. Delete Task")
    print("  8. Save and Exit")
    print("=" * 34)


def prompt_task_id(prompt_text: str) -> int:
    """
    Prompts the user for a task ID with error handling.

    Args:
        prompt_text: The prompt string to display to user.

    Returns:
        int: A valid integer task ID.

    Raises:
        ValueError: If the user input is not a valid integer.
    """
    raw_input = input(prompt_text).strip()
    # Remove leading '#' if user typed e.g. '#2'
    if raw_input.startswith("#"):
        raw_input = raw_input[1:]

    # ป้องกันโปรแกรม Crash เมื่อผู้ใช้พิมพ์ตัวอักษรแทนตัวเลข ด้วยการยกเว้น ValueError
    task_id = int(raw_input)
    if task_id <= 0:
        raise ValueError("Task ID must be a positive integer.")
    return task_id


def main() -> None:
    """Main application loop."""
    print("Welcome to Task Manager CLI!")
    print("Loading existing tasks from storage...")
    tasks = task_data.load_tasks()
    print(f"Loaded {len(tasks)} task(s) successfully.")

    try:
        while True:
            display_menu()
            choice = input("Enter choice (1-8): ").strip()

            if choice == "1":
                description = input("Enter task description: ").strip()
                if not description:
                    print("[Error] Description cannot be empty.")
                    continue
                tasks = task_logic.add_task(tasks, description)
                print("[Success] Task added successfully.")

            elif choice == "2":
                print("\n--- All Tasks ---")
                task_logic.list_tasks(tasks)

            elif choice == "3":
                print("\n--- Pending Tasks ---")
                task_logic.list_tasks(tasks, status="pending")

            elif choice == "4":
                print("\n--- Completed Tasks ---")
                task_logic.list_tasks(tasks, status="completed")

            elif choice == "5":
                keyword = input("Enter search keyword: ").strip()
                if not keyword:
                    print("[Error] Search keyword cannot be empty.")
                    continue
                print(f"\n--- Search Results for '{keyword}' ---")
                task_logic.search_tasks(tasks, keyword)

            elif choice == "6":
                # ใช้ try...except ValueError เมื่อรับค่า Task ID ตามโจทย์กำหนด
                try:
                    task_id = prompt_task_id("Enter Task ID to complete: ")
                    tasks = task_logic.mark_task_completed(tasks, task_id)
                    print(f"[Success] Task #{task_id} marked as completed.")
                except ValueError as ve:
                    print(f"[Error] Invalid Input: {ve}")
                except KeyError as ke:
                    print(f"[Error] Task Not Found: {ke}")

            elif choice == "7":
                # ใช้ try...except ValueError เมื่อรับค่า Task ID ตามโจทย์กำหนด
                try:
                    task_id = prompt_task_id("Enter Task ID to delete: ")
                    tasks = task_logic.delete_task(tasks, task_id)
                    print(f"[Success] Task #{task_id} deleted successfully.")
                except ValueError as ve:
                    print(f"[Error] Invalid Input: {ve}")
                except KeyError as ke:
                    print(f"[Error] Task Not Found: {ke}")

            elif choice == "8":
                print("\nSaving tasks to storage...")
                task_data.save_tasks(tasks)
                print("Goodbye!")
                break

            else:
                print("[Error] Invalid selection. Please enter a number between 1 and 8.")

    except KeyboardInterrupt:
        # เมื่อกด Ctrl+C ให้บันทึกข้อมูล save_tasks(tasks) เสมอก่อนออกจากโปรแกรม
        print("\n\n[Warning] KeyboardInterrupt detected (Ctrl+C).")
        print("Saving tasks to storage before exiting...")
        task_data.save_tasks(tasks)
        print("Goodbye!")
        sys.exit(0)


if __name__ == "__main__":
    main()
