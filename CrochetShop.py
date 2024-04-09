yarn_storage = {
  "Cotton": {"quantity": 3, "price": 25.00},
  "Indophil": {"quantity": 3, "price": 50.00},
  "Acrylic": {"quantity": 3, "price": 20.00},
  "Velvet": {"quantity": 3, "price": 75.00},
  "Polyester": {"quantity": 3, "price": 60.00}
  }

crochet_items_storage = {
  "Bag": {"quantity": 3, "price": 300.00},
  "Plushie": {"quantity": 3, "price": 250.00},
  "Top": {"quantity": 3, "price": 500.00},
  "Blanket": {"quantity": 3, "price": 750.00},
  "Scarf": {"quantity": 3, "price": 350.00}
}

buyer_accounts = {}
buyer_inventory = {}

seller_username = "laikrochet"
seller_password = "063022"

def main_menu():
  print("\n--------------------Welcome to LaiKrochet's Shop!--------------------")

  print("(1) Display Yarns")
  print("(2) Display Crocheted Items")
  print("(3) View Products Detail")
  print("(4) Register New Buyer Account")
  print("(5) Buyer Log-in")
  print("(6) Seller Log-in")
  print("(7) Exit")

  choice = int(input("\nEnter your chosen number: "))

  if choice == 1:
    yarn_stock()
  elif choice == 2:
    crochet_items()
  elif choice == 3:
    product_details()
  elif choice == 4:
    register_new_account()
  elif choice == 5:
    buyer_login()
  elif choice == 6:
    seller_login()
  elif choice == 7:
    main_menu()

def yarn_stock():
  print("\n{:<20} {:<15} {:<15}".format("Yarn", "Quantity", "Price"))
  print("-" * 42)

  for yarn, details in yarn_storage.items():
    print("{:<23} {:<12} {:<15}".format(yarn[:15], details["quantity"], details["price"]))
  main_menu()

def crochet_items():
  print("\n{:<20} {:<15} {:<15}".format("Crocheted Items", "Quantity", "Price"))
  print("-" * 42)

  for crocheteditems, details in crochet_items_storage.items():
    print("{:<23} {:<12} {:<15}".format(crocheteditems[:15], details["quantity"], details["price"]))
  main_menu()

def product_details():
  print("\n**********Product Details**********")

  print("(1) Yarn Descriptions")
  print("(2) Crocheted Items Description and Materials")
  print("(3) Exit")

  choice = int(input("\nEnter your chosen number: "))

  if choice == 1:
    yarn_details()
  if choice == 2:
    crochet_item_details()
  if choice == 3:
    main_menu()

def yarn_details():
  print("\n**********Description**********")

  while True:
    print("\nYarn Name: cotton, indophil, acrylic, velvet, polyester")
    yarn = input("Enter Selected Yarn: ")
    if yarn == "cotton":
      print("\nCotton Yarn")
      print("Cotton yarn for crocheting is a beloved choice among crafters for its softness, breathability, and versatility. Ideal for creating lightweight and breathable crocheted items such as garments, accessories, and home decor, cotton yarn provides a comfortable feel againts the skin. Its natural fibers make it suitable for all seasons and climates, and it holds its shape well, making it perfect for intricate crochet stitches and lacework.\n")
    elif yarn == "indophil":
      print("\nIndophil Yarn")
      print("Indophil yarn for crocheting is a unique blend of indigenous Philippine fibers, adding cultural significance and texture to crocheted creations. Combining fibers like abaca, pineapple, or silk. Indophil yarn brings a touch of Filipino heritage to crochet projects. It durability and natural texture make it ideal for crafting bags, accessories, and decorative items with an artisanal flair.\n")
    elif yarn == "acrylic":
      print("\nAcrylic Yarn")
      print("Acrylic yarn fro crocheting is a budget-friendly and versatile option for various crochet projects. With a wide range of vibrant colors and texture available. Acrylic yarn offers endless possibilities for crocheters. Its softness, easy care, and resistance to fading make it suitable for creating cozy blankets, garments, amigurumi, and accessories that require frequent washing and everyday use.\n")
    elif yarn == "velvet":
      print("\nVelvet Yarn")
      print("Velvet yarn for crocheting adds a touch of luxury and elegance to crochet projects with its plush, velvety texture. Ideal for creating soft and sumptuous items such as sacrves, cowls, pillows, and blankets. Velvet yarn adds warmth and sophistication to any design. Its smooth surface glides effortlessly on crochet hooks, making it easy to work with for both beginners and experienced crocheters.\n")
    elif yarn == "polyester":
      print("\nPolyester Yarn")
      print("Polyester yarn for crocheting is a durable and easy-care option suitable for a wide range of crochet projects. Known for its strength, resilience, and resistance to wrinkles and shrinking. Polyester yarn is perfect for crafting items and require long-lasting durability, such as bags, rugs, and outdoor accessories. Its smooth texture and wide color range make it versatile choice for crochet enthusiasts.\n")
    else:
      print("\nInvalid Choice.")

    choice = input("\n(1) Do you wish to continue? or (2) Go back to product details: ")
    if choice == "2":
      product_details()
      break
    if choice != "1":
      break
  
def crochet_item_details():
  print("\n**********Description and Material**********")

  while True:
    print("\nCrocheted Items: bag, plushie, top, blanket, and scarf")
    item = input("Enter Selected Item: ")
    if item == "bag":
      print("\nCrochet Bag")
      print("A lightweigt and durable crocheted bag, perfect for daily use. Its soft cotton yarn construction offers both practicality and style, making it an ideal accessory for any outing.")
      print("Material: Cotton Yarn\n")
    elif item == "plushie":
      print("\nCrochet Plushie")
      print("An adorable plushie that brings comfort and charm to any space. It's irresistably soft and perfect for cuddling.")
      print("Material: Velvet Yarn\n")
    elif item == "top":
      print("\nCrochet Top")
      print("Elevate your style with this intricately crocheted top. Lightweight and breathable, it's perfect for both casual and formal wear.")
      print("Materials: Indophil Yarn\n")
    elif item == "blanket":
      print("\nCrochet Blanket")
      print("Snuggle up in this cozy blanket, crafted for warmth and durability. Whether draped over a sofa or spread on a bed, it's a must-have for chilly nights.")
      print("Materials: Polyester Yarn\n")
    elif item == "scarf":
      print("\nCrochet Scarf")
      print("Add flair to your outfit with this vibrant scarf. Soft, lightweight, and easy to maintain, it's a versatile accessory fro any occassion.")
      print("Materials: Acrylic Yarn\n")
    else:
      print("\nInvalid Choice.")

    choice = input("\n(1) Do you wish to continue? or (2) Go back to product details?: ")
    if choice == "2":
      product_details()
      break
    if choice != "1":
      break

def register_new_account():
  print("\n**********Register New Account**********")

  username = input("\nEnter Username: ")
  if username in buyer_accounts:
    print("Username already exists.")
  else:
    password = input("Enter Password: ")
    buyer_accounts[username] = {"password": password, "balance": 0} 
    print("Account created successfully!")
    buyer_login()

def buyer_login():
  print("\n**********Log-in**********")

  while True:
    username = input("\nEnter your username: ")
    password = input("Enter your password: ")
    balance = 0
    if username in buyer_accounts and buyer_accounts[username]["password"] == password:
      buyer_menu(username)
    else:
      print("Invalid username or password.")
      
    choice = input("Do you want to exit? (y) or Continue to log-in: ")
    if choice == "y":
      return main_menu()
      
def buyer_menu(username):
  print(f"\nHello, {username}!")
  print("-" * 30)

  print("(1) Shop")
  print("(2) My Balance")
  print("(3) Top-up")
  print("(4) Quests")
  print("(5) History")
  print("(6) Exit")

  choice = int(input("\nEnter your chosen number: "))
  
  if choice == 1:
    shop(username)
  elif choice == 2:
    buyer_balance(username)
  elif choice == 3:
    topup(username)
  elif choice == 4:
    quests(username)
  elif choice == 5:
    buyer_history(username)
  elif choice == 6:
    main_menu()

def shop(username):
  print("\n--------------------Welcome to Laikrochet!--------------------")

  while True:
    print("\n(1) Buy Yarn")
    print("(2) Buy Crocheted Items")
    print("(3) Exit")

    choice = int(input("\nEnter your chosen number: "))

    if choice == 1:
      print("\n{:<20} {:<15} {:<15}".format("Yarn", "Quantity", "Price"))
      print("-" * 42)

      for yarn, details in yarn_storage.items():
        print("{:<23} {:<12} {:<15}".format(yarn[:15], details["quantity"], details["price"]))

      yarn_type = input("\nEnter Yarn Name: ")
      if yarn_type in yarn_storage and yarn_storage[yarn_type]["quantity"] > 0:
        quantity_1= int(input("Enter Quantity: "))
        if yarn_storage[yarn_type]["quantity"] >= quantity_1:
          cost = yarn_storage[yarn_type]["price"] * quantity_1
          if buyer_accounts[username]["balance"] >= cost:
            yarn_storage[yarn_type]["quantity"] -= quantity_1
            buyer_accounts[username]["balance"] -= cost
            if username not in buyer_inventory:
              buyer_inventory[username] = {}
            if yarn_type not in buyer_inventory[username]:
              buyer_inventory[username][yarn_type] = quantity_1
            else:
              buyer_inventory[username][yarn_type] += quantity_1
            print("\nYou have purchased successfully!")
            shop(username)
          else:
            print("Not Enough Balance")
        else:
          print("Not Enough Stock")
      else:
        print("Invalid yarn type.")

    elif choice == 2:
      print("\n{:<20} {:<15} {:<15}".format("Crocheted Items", "Quantity", "Price"))
      print("-" * 42)

      for crocheteditems, details in crochet_items_storage.items():
        print("{:<23} {:<12} {:<15}".format(crocheteditems[:15], details["quantity"], details["price"]))
    
      item_name = input("\nEnter Item Name: ")
      if item_name in crochet_items_storage and crochet_items_storage[item_name]["quantity"] > 0:
        quantity_1 = int(input("Enter Quantity: "))
        if crochet_items_storage[item_name]["quantity"] >= quantity_1:
          cost = crochet_items_storage[item_name]["price"] * quantity_1
          if buyer_accounts[username]["balance"] >= cost:
            crochet_items_storage[item_name]["quantity"] -= quantity_1
            buyer_accounts[username]["balance"] -= cost
            if username not in buyer_inventory:
              buyer_inventory[username] = {}
            if item_name not in buyer_inventory[username]:
              buyer_inventory[username][item_name] = quantity_1
            else:
              buyer_inventory[username][item_name] += quantity_1
            print("\nYou have purchased successfully!")
            shop(username)
          else:
            print("Not Enough Balance")
        else:
          print("Not Enough Stock")
      else:
        print("Invalid item name.")

    elif choice == 3:
      buyer_menu(username)

def buyer_balance(username):
  print(f"\nYour current balance is {buyer_accounts[username]["balance"]}")
  print("*" * 30)
  buyer_menu(username)

def topup(username):
  amount = float(input("\nEnter amount you want to top-up: "))
  buyer_accounts[username]["balance"] += amount
  print(f"You have top-up {amount}. Your current balance is {buyer_accounts[username]["balance"]}")
  buyer_menu(username)

def quests(username):
  print("\n-------------------Welcome to LaiKrochet's Quests!-------------------")
  
  print("(1) Begin Game")
  print("(2) Exit\n")

  choice = int(input("Enter your chosen number: "))

  if choice == 1:
    game(username)
  if choice == 2:
    buyer_menu(username)

def game(username):
  print("\n**********Crochet Questions!**********")

  print("Game Instructions:\n")
  print("1. This game consists of multiple-choice questions")
  print("2. Each correct answer corresponds to Php 5.00 and will be credited to your account.")
  print("3. Everytime you finish one question you will be ask to either continue to next question (y) or to go back to the menu")

  print("\nQuestion No.1")
  print("What is the name of the tool used in crocheting to create stitches?")
  print("a. Needle")
  print("b. Hook")
  print("c. Stick")

  choice = input("\nEnter the letter of your answer: ")
  if choice == "b":
    print("CORRECT")
    point = 5.00
    buyer_accounts[username]["balance"] += point
  else:
    print("INCORRECT")

  next_question = input("\nNext Question? (y): ")
  if next_question != "y":
    return buyer_menu(username)

  print("\nQuestion No. 2")
  print("What do you call a basic stitch?")
  print("a. Double Crochet")
  print("b. Treble Crochet")
  print("c. Single Crochet")

  choice = input("\nEnter the letter of your answer: ")
  if choice == "c":
    print("CORRECT")
    point = 5.00
    buyer_accounts[username]["balance"] += point
  else:
    print("INCORRECT")

  next_question = input("\nNext Question? (y): ")
  if next_question != "y":
    return buyer_menu(username)
  
  print("\nQuestion No.3")
  print("In crochet, what does 'YO' stands for?")
  print("a. Yank Over")
  print("b. Yarn Over")
  print("c. Yarn Out")

  choice = input("\nEnter the letter of your answer: ")
  if choice == "b":
    print("CORRECT")
    point = 5.00
    buyer_accounts[username]["balance"] += point
  else:
    print("INCORRECT")

  next_question = input("\nNext Question? (y): ")
  if next_question != "y":
    return buyer_menu(username)
  
  print("\nQuestion No. 4")
  print("What is the term for the process of creating a new loop in crochet?")
  print("a. Chaining")
  print("b. Looping")
  print("c. Stitching")

  choice = input("\nEnter the letter of your answer: ")
  if choice == "a":
    print("CORRECT")
    point = 5.00
    buyer_accounts[username]["balance"] += point
  else:
    print("INCORRECT")

  next_question = input("Next Question? (y): ")
  if next_question != "y":
    return buyer_menu(username)
  
  print("\nQUestion No. 5")
  print("In crochet patters, what does 'INC' typically indicate?")
  print("a. Increase")
  print("b. Instruction")
  print("c. Incorrect")

  choice = input("\nEnter the letter of your answer: ")
  if choice == "a":
    print("CORRECT")
    point = 5.00
    buyer_accounts[username]["balance"] += point
  else:
    print("INCORRECT")

  next_question = input("Next Question? (y): ")
  if next_question != "y":
    return buyer_menu(username)
  
  print("\nQuestion No. 6")
  print("Which type of crochet projects often uses the technique of 'amigurumi'?")
  print("a. Hats")
  print("b. Blankets")
  print("c. Toys")

  choice = input("\nEnter the letter of your answer: ")
  if choice == "c":
    print("CORRECT")
    point = 5.00
    buyer_accounts[username]["balance"] += point
  else:
    print("INCORRECT")

  next_question = ("Next Question? (y): ")
  if next_question != "y":
    return buyer_menu(username)
  
  print("\nQuestion No. 7")
  print("What is the purpose of a stitch marker in crochet?")
  print("a. To add decorative elements to the project")
  print("b. To mark the beginning of a round or row")
  print("c. To create buttonholes")

  choice = input("\nEnter the letter of your answer: ")
  if choice == "b":
    print("CORRECT")
    point = 5.00
    buyer_accounts[username]["balance"] += point
  else:
    print("INCORRECT")

  next_question = input("Next Question? (y): ")
  if next_question != "y":
    return buyer_menu(username)
  
  print("\nQuestion No.8")
  print("What does it mean to 'frog' a crochet project?")
  print("a. To add decorative frog closures to a finished project")
  print("b. To create a frog-shaped motif using crochet stitches")
  print("c. To unravel or undo stitches")

  choice = input("\nEnter the letter of your answer: ")
  if choice == "c":
    print("CORRECT")
    point = 5.00
    buyer_accounts[username]["balance"] += point
  else:
    print("INCORRECT")

  next_question = input("Next Question? (y): ")
  if next_question != "y":
    return buyer_menu(username)
  
  print("\nQuestion No. 8")
  print("Which type of crochet project would most likely use the 'magic ring' technique?")
  print("a. Amigurumi toy")
  print("b. Headband")
  print("c. Top")

  choice = input("\nEnter the letter of your answer: ")
  if choice == "a":
    print("CORRECT")
    point = 5.00
    buyer_accounts[username]["balance"] += point
  else:
    print("INCORRECT")

  next_question = input("Next Question? (y): ")
  if next_question != "y":
    return buyer_menu(username)
  
  print("\nQuestion No. 10")
  print("Which abbreviation is used to denote a 'slip stitch' in crochet?")
  print("a. ss")
  print("b. sl")
  print("c. st")

  choice = input("\nEnter the letter of your answer: ")
  if choice == "b":
    print("CORRECT")
    point = 5.00
    buyer_accounts[username]["balance"] += point
  else:
    print("INCORRECT")

def buyer_history(username):
  print("\n**********Purchase History**********")
  if username in buyer_inventory:
    for item, quantity in buyer_inventory[username].items():
      print(f"Item: {item}, Quantity: {quantity}")
  else:
    print("You haven't purchased anything.\n")
  buyer_menu(username)

def seller_login():
  print("\n**********Seller Log-in**********")

  while True:
    username = input("Enter Seller Username: ")
    password = input("Enter Password: ")

    if username == seller_username and password == seller_password:
      seller_menu()
      break
    else:
      print("Invalid seller username or password")

def seller_menu():
  print("\nHello, Seller!")

  print("(1) Update Yarn Stock")
  print("(2) Update Yarn Price")
  print("(3) Update Crocheted Items Stock")
  print("(4) Update Crocheted Items Price")
  print("(5) Exit\n")

  choice = int(input("Enter your chosen number: "))

  if choice == 1:
    print("\n{:<20} {:<15} {:<15}".format("Yarn", "Quantity", "Price"))
    print("-" * 42)

    for yarn, details in yarn_storage.items():
      print("{:<23} {:<12} {:<15}".format(yarn[:15], details["quantity"], details["price"]))

    yarn_type = input("Enter Yarn Name: ")
    if yarn_type in yarn_storage:
      add_quantity = int(input("Enter Quantity: "))
      yarn_storage[yarn_type]["quantity"] += add_quantity
      print("Quantity Updated!")
      seller_menu()
    else:
      print("Invalid yarn type.")
      seller_menu()

  elif choice == 2:
    print("\n{:<20} {:<15} {:<15}".format("Yarn", "Quantity", "Price"))
    print("-" * 42)

    for yarn, details in yarn_storage.items():
      print("{:<23} {:<12} {:<15}".format(yarn[:15], details["quantity"], details["price"]))

    yarn_type = input("Enter Yarn Name: ")
    if yarn_type in yarn_storage:
      new_price = float(input("Enter New Price: "))
      yarn_storage[yarn_type]["price"] == new_price
      print("Price Updated!")
      seller_menu()
    else:
      print("Invalid yarn type.")
      seller_menu()

  elif choice == 3:
    print("\n{:<20} {:<15} {:<15}".format("Crocheted Items", "Quantity", "Price"))
    print("-" * 42)

    for crocheteditems, details in crochet_items_storage.items():
      print("{:<23} {:<12} {:<15}".format(crocheteditems[:15], details["quantity"], details["price"]))

    item_name = input("Enter Item Name: ")
    if item_name in crochet_items_storage:
      add_quantity_2 = int(input("Enter Quantity: "))
      crochet_items_storage[item_name]["quantity"] += add_quantity_2
      print("Quantity Updated!")
      seller_menu()
    else:
      print("Invalid item name.")
      seller_menu()

  elif choice == 4:
    print("\n{:<20} {:<15} {:<15}".format("Crocheted Items", "Quantity", "Price"))
    print("-" * 42)

    for crocheteditems, details in crochet_items_storage.items():
      print("{:<23} {:<12} {:<15}".format(crocheteditems[:15], details["quantity"], details["price"]))
      
    item_name = input("Enter Item Name: ")
    if item_name in crochet_items_storage:
      new_price_2 = float(input("Enter New Price: "))
      crochet_items_storage[item_name]["quantity"] == new_price_2
      print("Price Updated!")
      seller_menu()
    else:
      print("Invalid item name.")
      seller_menu()

  elif choice == 5:
    main_menu()

main_menu()