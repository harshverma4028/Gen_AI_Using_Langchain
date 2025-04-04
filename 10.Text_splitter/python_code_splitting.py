from langchain.text_splitter import RecursiveCharacterTextSplitter, Language


text = """import matplotlib.pyplot as plt

# Function to generate Fibonacci sequence
def generate_fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence

# Function to plot the Fibonacci sequence
def plot_fibonacci(fib_sequence):
    plt.plot(fib_sequence, marker='o', linestyle='-', color='b')
    plt.title("Fibonacci Sequence")
    plt.xlabel("Index")
    plt.ylabel("Fibonacci Number")
    plt.grid(True)
    plt.show()

# Main logic
num_terms = int(input("Enter the number of terms for Fibonacci sequence: "))
fib_sequence = generate_fibonacci(num_terms)
print("Fibonacci Sequence:", fib_sequence)
plot_fibonacci(fib_sequence)

"""

spliter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size = 100,
    chunk_overlap=0,
)

chunks = spliter.split_text(text)

print(len(chunks))

print(chunks[0])