# PriCo-The-Ultimate-Price-Comparator

## Note : The project is in developing Phase.
## 📌 Project Overview
Django Price Scraper is a web application that allows users to compare product prices from Flipkart and Amazon. It uses web scraping techniques with `BeautifulSoup` and `requests` to extract product details such as name, price, rating, image, and product link.

## 🚀 Features
- 🔍 **Search for products** across Flipkart and Amazon
- 📊 **Compare prices** in ascending order
- 🖼️ **Displays product images** along with name, price, and rating
- 🔗 **Direct links** to product pages for easy purchase
- ⚡ **Fast and responsive** UI with Jinja templating

## 🛠️ Technologies Used
- **Backend**: Django 5.1.1 (Python 3.12.6)
- **Web Scraping**: BeautifulSoup, requests
- **Frontend**: HTML, CSS, Jinja Templates

## 📂 Project Structure
```
Django-Price-Scraper/
│── Comparator/         # Django app for scraping       
│   ├── views.py         # Handles search and scraping
│   ├── urls.py          # URL routing
│── manage.py            # Django project manager
|── templates            # HTML templates
|    ├── results.html    # Displays search results
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
```

## 📝 To-Do List
- [ ] Improve error handling for unavailable products
- [ ] Add support for more e-commerce sites
- [ ] Implement pagination for better navigation

## 📜 License
This project is licensed under the MIT License. Feel free to contribute and improve it!

## 🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss the changes.

## 📬 Contact
For any queries, reach out at **ayushkumarkarmi30@gmail.com**

Happy Scraping! 🚀

