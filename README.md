# 🧪 SauceDemo UI Testing

This project tests the [SauceDemo](https://www.saucedemo.com) website using **Pytest + Selenium WebDriver**.

## ✅ Features Covered

- Valid login
- Sorting products by name & price
- Add to cart
- Cart value validation
- Checkout process
- Logout
- Invalid login & empty fields

## 🛠 Tech Stack

- Python
- Selenium
- Pytest
- Pytest-html (for reports)
- WebDriverManager

## 🚀 Setup & Run

1. Install dependencies:

## What I learn
-Writing reliable Selenium locators and handling dynamic web elements

-Designing tests with Pytest fixtures and parameterization

-Structuring code with Page Object Model for better readability and reuse

-Generating HTML reports for easier test analysis

-Managing Python dependencies with pip and requirements.txt
## Challenges faced
-**Finding the right web elements**: Sometimes buttons or fields changed their attributes, so simple locators didn’t work. I had to try different ways like CSS selectors and XPath to make tests stable.

-**Organizing the code**: At first, all test code was mixed together. Learning to separate page details into classes (Page Object Model) helped keep tests clean and easier to update.

-**Checking test results carefully**: Making sure the tests actually check the right things (like confirming items added to cart or sorted correctly) took some trial and error.

-**Setting up reports**: Creating test reports that are easy to read and show useful info was new to me. I worked on generating HTML reports with pytest-html.
