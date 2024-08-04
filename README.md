# StatNav Introduction
## Purpose and Motivation
With the proliferation of company filings and ever-growing performance indicators, modern-day businesses can often be overwhelmed by the sheer volume of financial data. It has become increasingly time-consuming for data analysts to scope-in on the relevant statistics in the face of exceedingly large datasets. Having to look through staggering amounts of textual documents, data analysts may be demotivated, distracted or even lose sight of important details. There is a need for a reliable, accurate and consistent tool that can save analysts from the mandune task of traversing countless files for certain statistics - by providing them with the data they need to write reports and formulate insights. 

With the advent of the LLM such as Chatgpt, which is an AI model that interprets and analyzes human language, the emergence of AI agents has become possible. By using LLMs on search data, not only will traditional analysis be enriched, but previously overlooked patterns and relationships can be discovered. This has a huge potential impact on strategic decisions by investors, analysts and regulators, making the project both interesting and important.

## Goals
This project aims to confront the gap in the lack of efficient tools that can reduce substantial time and effort spent by data analysts to search data themselves through the utilization of the LLM. This effectively makes report writing more convenient, quicker and easier. The goal of this project is to develop a program which retrieves, searches and filters the relevant data from company filings into concise, secure and structured forms that can be returned to the user as important statistics - so the analysts can focus on what they do best; the analysis itself.  

## Block Diagram, schematic, and modules
### Diagram and milestone breakdown
![unnamed](https://github.com/user-attachments/assets/94a90270-388d-45eb-aa7b-31984c5c19c0)

### Module Name
- Data-Retrieval:
The data-retrieval function is responsible for retrieving company filings (10-Q, 10-K) from the SEC (U.S. Securities and Exchange Commission) EDGAR database and downloading them as pdf format for a given company and filing date. The module utilizes the requests library for making HTTP requests, BeautifulSoup for parsing HTML content, and pdfkit for converting HTML to PDF.
It takes user input for company name, central index key (CIK) , requested file format (10K, 10q, etc), and date of file. Based on acquired input, it formulates a header and makes a GET request call to SEC EDGAR api. The response is stored and parsed using BeautifulSoup. Once a file or set of files is confirmed to match the requirements specified by the user, pdfkit library is used to configure wkhtmltopdf (a webkit rendering engine tool) and convert html/css of financial documents into pdf which is then downloaded.
It is important to note that this feature is incorporated to a separate web-page on the interface. This provides an opportunity for users to manually download the files and verify certain statistics while they are using the virtual analyst agent.
Quality attributes: The output of this module should be accurate, reliable (consistent without failures), and scalable when working with high volumes of request. 

- Full Text Search:
This module is designed to search for specific keywords within a PDF file and extract sentences containing those keywords. The module utilizes the PyPDF2 library for reading PDF files and regular expressions to split the text into sentences.The key terms from the user are input and they are used to identify patterns/sentences surrounding this term. Through iteration, the relevant sentences, values and phases are appended and written to file.
Quality attributes: This module should provide relevant and flexible results in addition to accuracy and speed. 

- LLM Integration:
LLMs such as GPT-4 will inherently search for all resources and data which it is trained from while trying to generate a response. However, as financial reports contain very critical and sensitive data, the goal is to ensure the model only searches for relevant company filings instead of all online resources. In order to achieve this, another layer of instruction is added in the program that explicitly tells the system to only search for relevant company filings after the model receives a user query. 
Quality attributes: Verify the numerical values provided form the model’s response is strictly matching the numbers from the company filings (10-Q/10-K)

