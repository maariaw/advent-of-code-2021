def main():
    m = 147
    s = 0
    while m > 0:
        s += m
        m -= 1

    print(f"""
    The maximum y value is {s}
    """)

if __name__ == "__main__":
    main()
