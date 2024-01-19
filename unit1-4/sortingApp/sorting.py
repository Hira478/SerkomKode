def display_menu():
    """
    Displays the menu and returns the user's choice.

    :return: str -- User's choice ('1', '2', or '3').
    """
    print("MENU PILIHAN")
    print("1. Input angka")
    print("2. Tampil hasil pengurutan")
    print("3. Selesai")
    return input("Masukkan pilihan [1/2/3] : ")

def input_numbers():
    """
    Gets input from the user and returns a list of numbers.

    :return: List[int] -- List of input numbers.
    """
    try:
        num_count = int(input("Masukkan jumlah angka yang akan diinput : "))
        numbers = []
        print("Input Angka Secara Acak")
        print("-----------------------")
        for i in range(1, num_count + 1):
            num = int(input(f"Angka {i} : "))
            numbers.append(num)
        return numbers
    except ValueError:
        print("Masukkan angka yang valid.")
        return []

def bubble_sort(arr):
    """
    Sorts a list of numbers using the bubble sort algorithm.

    :param arr: List[int] -- List of numbers to be sorted.
    :return: List[int] -- Sorted list of numbers.
    """
    try:
        n = len(arr)

        # Ensure the input list is not empty or has a single element
        if n <= 1:
            return arr

        # Bubble sort algorithm
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

        return arr
    except Exception as e:
        print(f"Error during sorting: {e}")
        return []

def display_sorted_data(numbers):
    """
    Displays the sorted list of numbers.

    :param numbers: List[int] -- List of sorted numbers.
    """
    print("TAMPIL HASIL PENGURUTAN")
    if numbers:
        print(f"Nilai tugas : {', '.join(map(str, numbers))}")
    else:
        print("Data kosong atau terdapat kesalahan.")

def save_sorted_data(numbers):
    """
    Saves the sorted list of numbers to a file.

    :param numbers: List[int] -- List of sorted numbers.
    """
    try:
        with open("sorted_data.txt", "w") as file:
            for num in numbers:
                file.write(str(num) + "\n")
    except Exception as e:
        print(f"Error during saving data: {e}")

def main():
    """
    Main program logic.

    This function serves as the entry point for the program. It displays a menu,
    processes user input, and performs actions based on the chosen option.
    """
    numbers = []

    while True:
        choice = display_menu()

        if choice == '1':
            numbers = input_numbers()
            bubble_sort(numbers)
        elif choice == '2':
            display_sorted_data(numbers)
            save_sorted_data(numbers)
        elif choice == '3':
            print("Terima kasih, selesai.")
            break
        else:
            print("Pilihan tidak valid, silakan masukkan 1, 2, atau 3.")

if __name__ == "__main__":
    main()
