# Rocklin High Student Directory (2023–2024)

A searchable, filterable, and paginated directory of all Rocklin High School students from the 2023–24 school year — built in **Python** using **Streamlit**, with data securely hosted on **Azure Blob Storage**.

---

## Features

- **Search** by name or student ID  
- **Filters** for grade, class name, and teacher  
- **Pagination** for fast rendering  
- **Statistics dashboard** with charts  
- **Multipage layout**: Home, Stats, FAQ, About  
- **Secure cloud storage** with Azure
- **Required Login** in order to limit access to only RHS students
---

## Security

All student data is uploaded to Azure, where it is encrypted and accessed through their API. Data retreival is usually fast, but might take some time to laod. The API key is stored on Streamlit and encrypted, and never accessed locally. The cost is very cheap, less than $0.01 a month. Only way to access data is through website.

But even so, this data in PDF form is given to almost every student in yearbook. It's not *that* secretive.

---

## Versions

**Version 1.0.0** - student directory for 2023-2024, along with filters/search, statistics, and secure storage.
Version 1.0.1 - typo fixes and created "dev log"        
**Version 2.0.0** - added data for additional years, implemented security protocols
Version 2.1.0 - added multiselect features for easier selection