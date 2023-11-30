import tkinter as tk
from tkinter import simpledialog
from PIL import Image, ImageTk

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        image = Image.open("dd.jpg")
        self.background_image = ImageTk.PhotoImage(image)

        self.background_label = tk.Label(root, image=self.background_image)
        self.background_label.place(relwidth=1, relheight=1)

        self.label = tk.Label(root, text="To-Do List", font=("Helvetica", 26, "bold"))
        self.label.pack(pady=10)

        self.canvas = tk.Canvas(root, width=300, height=300, bg="white")
        self.canvas.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task, width=25)
        self.add_button.pack(side=tk.TOP, pady=(0, 10))

        self.delete_button = tk.Button(root, text="Delete Task", command=self.delete_checked_tasks, width=25)
        self.delete_button.pack(side=tk.TOP, pady=(0, 10))

        # Load the tick mark image
        self.tick_image = ImageTk.PhotoImage(Image.open("tick.png"))

        self.update_task_list()

        self.canvas.bind("<Button-3>", self.right_click_delete)
        self.canvas.bind("<ButtonRelease-3>", self.right_click_delete)

        self.exit_button = tk.Button(root, text="Exit", command=root.destroy, width=15)
        self.exit_button.pack(side=tk.BOTTOM, anchor=tk.S, pady=10)  # Place the Exit button at the bottom center

    def add_task(self):
        task_name = simpledialog.askstring("Add Task", "Enter task name:")
        if task_name:
            self.tasks.append({"name": task_name, "completed": tk.BooleanVar()})
            self.update_task_list()

    def delete_checked_tasks(self):
        indices_to_delete = [idx for idx, task in enumerate(self.tasks) if task["completed"].get()]
        for idx in reversed(indices_to_delete):
            self.tasks.pop(idx)
        self.update_task_list()

    def right_click_delete(self, event):
        selected_task_index = self.get_clicked_task_index(event)
        if selected_task_index is not None:
            self.tasks.pop(selected_task_index)
            self.update_task_list()

    def get_clicked_task_index(self, event=None):
        if event:
            x, y = event.x, event.y
            items = self.canvas.find_closest(x, y)
            if items:
                return int(self.canvas.gettags(items[0])[0])
        return None

    def toggle_completion(self, task_index):
        self.tasks[task_index]["completed"].set(not self.tasks[task_index]["completed"].get())
        self.update_task_list()

    def update_task_list(self):
        self.canvas.delete("all")
        for idx, task in enumerate(self.tasks):
            task_name = task["name"]
            completed = task["completed"].get()

            # Increase the vertical gap between checkboxes
            vertical_gap = 30

            checkbox_bg = self.canvas.create_rectangle(5, vertical_gap * idx + 5, 25, vertical_gap * idx + 25, outline="black", fill="white")

            if completed:
                # Fill the checkbox with green color
                self.canvas.itemconfig(checkbox_bg, fill="green")

            text_id = self.canvas.create_text(35, vertical_gap * idx + 15, anchor=tk.W, text=task_name, tags=str(idx))

            self.canvas.tag_bind(checkbox_bg, '<Button-1>', lambda e, idx=idx: self.toggle_completion(idx))
            self.canvas.tag_bind(text_id, '<Button-1>', lambda e, idx=idx: self.toggle_completion(idx))


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
