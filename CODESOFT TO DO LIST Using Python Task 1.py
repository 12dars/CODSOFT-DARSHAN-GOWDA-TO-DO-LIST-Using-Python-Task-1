# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 15:33:47 2023

@author: darshan
"""

import sqlite3

class TodoList:
    def __init__(self):
        self.conn = sqlite3.connect('todolist.db')
        self.cursor = self.conn.cursor()
        self.cursor.execute('''create table if not exists tasks
                     (id integer primary key, task text, due_date text, status integer)''')

    def add_task(self, task, due_date):
        self.cursor.execute("insert into tasks (task, due_date, status) values(?, ?, ?)",
                            (task, due_date, 0))
        self.conn.commit()
 
    def view_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        rows = self.cursor.fetchall()
        for row in rows:
            print(f"{row[0]}) {row[1]} - {row[2]} - {row[3]}")

    def update_task(self, id, status):
        self.cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, id))
        self.conn.commit()

    def delete_task(self, id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (id,))
        self.conn.commit()

def menu():
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

if __name__ == "__main__":
    todolist = TodoList()
    while True:
        menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            task = input("Enter task: ")
            due_date = input("Enter due date (dd/mm/yyyy): ")
            todolist.add_task(task, due_date)
        elif choice == '2':
            todolist.view_tasks()
        elif choice == '3':
            id = int(input("Enter task id: "))
            status = int(input("Enter task status (0-Incomplete, 1-Completed): "))
            todolist.update_task(id, status)
        elif choice == '4':
            id = int(input("Enter task id: "))
            todolist.delete_task(id)
        elif choice == '5':
            break
        else:
            print("the choice is invalid.")