import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import time
import copy

def shell_sort(arr, ax):
    n = len(arr)
    gap = n // 2

    start_time = time.time()
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
                ax.clear()
                ax.bar(x, arr, color='blue')
                ax.set_title('Shell Sort Visualization')
                ax.set_xlabel('Index')
                ax.set_ylabel('Value')
                for k in range(len(arr)):
                    ax.text(k, arr[k] + 0.5, str(arr[k]), ha='center')
                plt.pause(0.1)
            arr[j] = temp
            ax.clear()
            ax.bar(x, arr, color='blue')
            ax.set_title('Shell Sort Visualization')
            ax.set_xlabel('Index')
            ax.set_ylabel('Value')
            for k in range(len(arr)):
                ax.text(k, arr[k] + 0.5, str(arr[k]), ha='center')
            plt.pause(0.1)
        gap //= 2
    end_time = time.time()
    return end_time - start_time

def shell_sort_visualization(arr):
    lst = copy.deepcopy(arr)
    global x
    x = np.arange(0, len(lst), 1)

    fig, ax = plt.subplots()
    ax.bar(x, lst, color='blue')
    ax.set_title('Shell Sort Visualization - Unsorted')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    for i in range(len(lst)):
        ax.text(i, lst[i] + 0.5, str(lst[i]), ha='center')
    plt.pause(1)

    time_taken = shell_sort(lst, ax)

    ax.clear()
    ax.bar(x, lst, color='green')
    ax.set_title('Shell Sort Visualization - Sorted')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    for i in range(len(lst)):
        ax.text(i, lst[i] + 0.5, str(lst[i]), ha='center')
    plt.show()

    return time_taken
def merge_sort(arr, left, right, ax):
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid, ax)
        merge_sort(arr, mid + 1, right, ax)
        merge(arr, left, mid, right, ax)

def merge(arr, left, mid, right, ax):
    n1 = mid - left + 1
    n2 = right - mid

    # Create temporary arrays
    L = arr[left:left + n1].copy()
    R = arr[mid + 1:mid + 1 + n2].copy()

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

    # Update plot after merging
    ax.clear()
    ax.bar(x, arr, color='violet')
    ax.set_title('Merge Sort Visualization')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    for i in range(len(arr)):
        ax.text(i, arr[i] + 0.5, str(arr[i]), ha='center')
    plt.pause(0.5)

def merge_sort_visualization(arr):
    lst = copy.deepcopy(arr)
    global x
    x = np.arange(0, len(lst), 1)

    fig, ax = plt.subplots()

    # Initial plot of the unsorted array
    ax.bar(x, lst, color='violet')
    ax.set_title('Merge Sort Visualization - Unsorted')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    for i in range(len(lst)):
        ax.text(i, lst[i] + 0.5, str(lst[i]), ha='center')
    plt.pause(1)

    start_time = time.time()
    merge_sort(lst, 0, len(lst) - 1, ax)
    end_time = time.time()

    # Final sorted plot
    ax.clear()
    ax.bar(x, lst, color='green')
    ax.set_title('Merge Sort Visualization - Sorted')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    for i in range(len(lst)):
        ax.text(i, lst[i] + 0.5, str(lst[i]), ha='center')
    plt.show()

    return end_time - start_time
# Bubble Sort Algorithm and Visualization
def bubble_sort(arr, ax):
    n = len(arr)
    start_time = time.time()
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                ax.clear()
                ax.bar(x, arr, color='orange')
                ax.set_title('Bubble Sort Visualization')
                ax.set_xlabel('Index')
                ax.set_ylabel('Value')
                for k in range(len(arr)):
                    ax.text(k, arr[k] + 0.5, str(arr[k]), ha='center')
                plt.pause(0.1)
    end_time = time.time()
    ax.clear()
    ax.bar(x, arr, color='orange')
    ax.set_title('Bubble Sort Visualization')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    for k in range(len(arr)):
        ax.text(k, arr[k] + 0.5, str(arr[k]), ha='center')
    plt.pause(0.1)
    return end_time - start_time

def bubble_sort_visualization(arr):
    lst = copy.deepcopy(arr)
    global x
    x = np.arange(0, len(lst), 1)

    fig, ax = plt.subplots()
    ax.bar(x, lst, color='orange')
    ax.set_title('Bubble Sort Visualization - Unsorted')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    for i in range(len(lst)):
        ax.text(i, lst[i] + 0.5, str(lst[i]), ha='center')
    plt.pause(1)

    time_taken = bubble_sort(lst, ax)

    ax.clear()
    ax.bar(x, lst, color='green')
    ax.set_title('Bubble Sort Visualization - Sorted')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    for i in range(len(lst)):
        ax.text(i, lst[i] + 0.5, str(lst[i]), ha='center')
    plt.show()

    return time_taken

# Insertion Sort Algorithm and Visualization
def insertion_sort(arr, ax):
    start_time = time.time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            ax.clear()
            ax.bar(x, arr, color='magenta')
            ax.set_title('Insertion Sort Visualization')
            ax.set_xlabel('Index')
            ax.set_ylabel('Value')
            for k in range(len(arr)):
                ax.text(k, arr[k] + 0.5, str(arr[k]), ha='center')
            plt.pause(0.1)
        arr[j + 1] = key
        ax.clear()
        ax.bar(x, arr, color='magenta')
        ax.set_title('Insertion Sort Visualization')
        ax.set_xlabel('Index')
        ax.set_ylabel('Value')
        for k in range(len(arr)):
            ax.text(k, arr[k] + 0.5, str(arr[k]), ha='center')
        plt.pause(0.1)
    end_time = time.time()
    return end_time - start_time

def insertion_sort_visualization(arr):
    lst = copy.deepcopy(arr)
    global x
    x = np.arange(0, len(lst), 1)

    fig, ax = plt.subplots()
    ax.bar(x, lst, color='magenta')
    ax.set_title('Insertion Sort Visualization - Unsorted')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    for i in range(len(lst)):
        ax.text(i, lst[i] + 0.5, str(lst[i]), ha='center')
    plt.pause(1)

    time_taken = insertion_sort(lst, ax)

    ax.clear()
    ax.bar(x, lst, color='green')
    ax.set_title('Insertion Sort Visualization - Sorted')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    for i in range(len(lst)):
        ax.text(i, lst[i] + 0.5, str(lst[i]), ha='center')
    plt.show()

    return time_taken

# Tkinter Interface
def main():
    # Function to start Shell Sort visualization
    def shell_sort_visualization_wrapper():
        time_taken = shell_sort_visualization(arr)
        time_label.config(text=f"Shell Sort took {time_taken:.2f} seconds")

    # Function to start Insertion Sort visualization
    def insertion_sort_visualization_wrapper():
        time_taken = insertion_sort_visualization(arr)
        time_label.config(text=f"Insertion Sort took {time_taken:.2f} seconds")

    # Function to start Bubble Sort visualization
    def bubble_sort_visualization_wrapper():
        time_taken = bubble_sort_visualization(arr)
        time_label.config(text=f"Bubble Sort took {time_taken:.2f} seconds")

    # Function to start Merge Sort visualization
    def merge_sort_visualization_wrapper():
        time_taken = merge_sort_visualization(arr)
        time_label.config(text=f"Merge Sort took {time_taken:.2f} seconds")

    # Create the main window
    root = tk.Tk()
    root.title("Sorting Algorithm Visualizer")

    # Define styling variables
    button_bg = "yellow"
    button_fg = "black"
    label_font = ("Helvetica", 14)

    # Add a label
    label = tk.Label(root, text="Choose a Sorting Algorithm to Visualize:", font=label_font)
    label.pack(pady=10)

    # Add buttons for each sorting algorithm with styled appearance
    button_styles = {"background": button_bg, "foreground": button_fg, "font": label_font}

    bubble_button = tk.Button(root, text="Bubble Sort", command=bubble_sort_visualization_wrapper, **button_styles)
    bubble_button.pack(pady=5, padx=20, ipadx=20)

    insertion_button = tk.Button(root, text="Insertion Sort", command=insertion_sort_visualization_wrapper, **button_styles)
    insertion_button.pack(pady=5, padx=20, ipadx=20)

    shell_button = tk.Button(root, text="Shell Sort", command=shell_sort_visualization_wrapper, **button_styles)
    shell_button.pack(pady=5, padx=20, ipadx=20)

    merge_button = tk.Button(root, text="Merge Sort", command=merge_sort_visualization_wrapper, **button_styles)
    merge_button.pack(pady=5, padx=20, ipadx=20)

    # Add a label to display the time taken
    global time_label
    time_label = tk.Label(root, text="", font=label_font)
    time_label.pack(pady=10)

    # Generate a single set of random values to be used by all sorting algorithms
    global arr
    arr = np.random.randint(0, 50, 15)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
