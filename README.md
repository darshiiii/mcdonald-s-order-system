# Multi-Page Application with Tkinter

This is a Python script using Tkinter to create a multi-page application for a McDonald's order system. The application allows the user to navigate through different pages to select food items and generate a PDF bill.

## Overview

- **Libraries Used:**
  - `tkinter`: GUI library for creating the graphical user interface.
  - `PIL` (Pillow): Python Imaging Library for working with images.
  - `reportlab.pdfgen`: Library for creating PDF documents.

- **Pages:**
  1. **Page 1 (`page1`):**
      - Displays a welcome message and an image.
      - Contains a button to start the order.

  2. **Page 2 (`page2`):**
      - Asks for the eating location (Eat In or Take Out).
      - Displays images and buttons for the choices.

  3. **Page 3 (`page3`):**
      - Displays the menu categories as buttons.
      - Includes a button to view the final bill.

  4. **Page 4 (`page4`):**
      - Lists burger items with buttons to add them.
      - Shows the total amount of burgers.

  5. **Page 5 (`page5`):**
      - Lists fries and sides with buttons to add them.
      - Shows the total amount of fries and sides.

  6. **Page 6 (`page6`):**
      - Lists chicken and fish sandwiches with buttons to add them.
      - Shows the total amount of chicken and fish sandwiches.

  7. **Page 7 (`page7`):**
      - Lists McCafe items with buttons to add them.
      - Shows the total amount of McCafe items.

  8. **Page 8 (`page8`):**
      - Lists beverages with buttons to add them.
      - Shows the total amount of beverages.

  9. **Page 9 (`page9`):**
      - Displays the total amount of the order.
      - Allows the user to generate a PDF bill.

- **Functions:**
  - `switch_page(page_number)`: Switches to the specified page.
  - `update_sum_and_switch(value, page)`: Updates the total and switches to the next page.
  - `update_total()`: Updates the total amount based on entries on each page.
  - `generate_pdf()`: Generates a PDF bill with order details.

- **Execution:**
  - Initializes the main window, pages, and a notebook to organize the pages.
  - Sets up buttons, labels, and entry widgets on each page.
  - Defines functions to handle page switching and updating totals.
  - Starts the Tkinter main event loop.

---

**Note**: Make sure to replace image paths (`image_path` and `image_path1`) with the correct paths on your system.
