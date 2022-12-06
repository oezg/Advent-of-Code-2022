def find_n_different_consecutive_characters(text: str, n: int, offset: int = 0) -> int:
    for i in range(n + offset, len(text) + 1):
        if len(set(text[i-n:i])) == n:
            return i



def main():
    with open("input.txt", "r") as file:
        buff = file.read()

    start_of_packet_marker = find_n_different_consecutive_characters(buff, 4)
    result = find_n_different_consecutive_characters(buff, 14, offset=start_of_packet_marker)
    print(result)



if __name__ == "__main__":
    main()

