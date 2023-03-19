def main():
    frac = input("Fraction: ").split("/")
    if frac[0].isdigit() and frac[1].isdigit():
        val = int(frac[0]) / int(frac[1]) * 100
        if val <= 1:
            print("E")
        else:
            print(f"{val:.0f}%")
    else:
        main()

main()