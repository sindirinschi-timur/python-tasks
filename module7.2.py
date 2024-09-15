def main():
    names = set()

    while True:
      name = input("Enter a name (Press enter to stop): ")
      if name == "":
        break
      elif name in names:
          print("Name exists.")
      else:
          names.add(name)
          print("New name.")

    for name in names:
        print(name)

if __name__ == "__main__":
    main()