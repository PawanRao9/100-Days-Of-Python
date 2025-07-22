# ENCODING AND DECODING ..........


while True:
    st = input("\nEnter a message (or type 'exit' to quit): ")

    if st.lower() == "exit":
        print("Goodbye!")
        break

    words = st.split(" ")
    coding = input("1 -> coding \n2 -> decoding: ")
    coding = True if coding == "1" else False

    r1 = "jhd"
    r2 = "odj"

    if coding:
        nwords = []
        for word in words:
            if len(word) >= 3:
                stnew = r1 + word[1:] + word[0] + r2
                nwords.append(stnew)
            else:
                nwords.append(word[::-1])
        print("Encoded message:", " ".join(nwords))
    else:
        nwords = []
        for word in words:
            if len(word) >= 3:
                if word.startswith(r1) and word.endswith(r2):
                    core = word[len(r1):-len(r2)]
                    stnew = core[-1] + core[:-1]
                    nwords.append(stnew)
                else:
                    nwords.append(word)  # fallback
            else:
                nwords.append(word[::-1])
        print("Decoded message:", " ".join(nwords))
