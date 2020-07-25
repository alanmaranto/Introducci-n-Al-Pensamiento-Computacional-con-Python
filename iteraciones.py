extern_counter = 0
intern_counter = 0

while extern_counter < 5:
    while intern_counter < 6:
        print(extern_counter, intern_counter)
        intern_counter += 1

        if intern_counter >= 3:
            break
    extern_counter += 1
    intern_counter = 0


