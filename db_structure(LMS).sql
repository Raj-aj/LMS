create database if not exists LMS; use LMS;

CREATE TABLE IF NOT EXISTS Students (
    Adm_no 	INT primary key,
    Name 	CHAR(225),
    Email_ID 	CHAR(225),
    Phone_No 	BIGINT
);


Create table if not exists Book_Borrowers( 
	borrower_no		bigint		primary key auto_increment,
	Adm_no 			int,
	Phone_No 		bigint,
	Name 			char(225),
	Email_ID 		char(225),
	Borrowed_book_id   	int,
	Borrowed_date   	TIMESTAMP  DEFAULT CURRENT_TIMESTAMP,
	submit_date   		TIMESTAMP DEFAULT 0,
	total_days      	int,
	fine_amount 		int default 0,
    fine_submit_date   		TIMESTAMP DEFAULT 0
);

Create table if not exists Books( 
	Book_ID 	bigint primary key auto_increment,
	Book_Name 	char(225), 			
	Class  		int,  				
	Subject 	char(225), 			
	Language 	char(225), 
	Available 	char(3) DEFAULT 'yes',
	Publisher 	char(225),
	Author 		char(225), 
	Book_Added_On   TIMESTAMP  DEFAULT CURRENT_TIMESTAMP,
	Last_Update_On  TIMESTAMP
) ;  			

insert into Books ( Book_ID,Book_Name, Class, Subject, Language,Author) values
( 100,"Vision 2020", 12, "Story Book", "English",'A. P. J. Abdul Kalam Y. S. Rajan'),
( 101,"Two Year Eight Months and Twenty –Eight Night", 10, "Story Book", "English",'Salman Rushdie'),
( 102,"In Search of Lost Time", 12, "novel", "English",'MARCEL PROUST'),
( 103,"My Favourite Nature Stories", 10, "Story Book", "English",'Ruskin Bond'),
( 104,"Why I Assassinated Gandhi", 10, "book", "English",'Nathuram Godse & Gopal Godse (edited by Virendra Mehra)'),
( 105,"The Story of My Experiments with Truth", 10, "book", "English",'Mohandas Karamchand Gandhi, Mahatma Gandhi'),
( 106,"Transedence", 10, "Book", "English",'APJ Abdul Kalam');

insert into Students (adm_no,name,email_id,phone_no) values 
(2659,'Rohan Kumar',		'@gmail.com',9999999999),
(2653,'MD. Toushif Akhtar', 	'@gmail.com',9999999999),
(2661,'Simmy Prasad',		'@gmail.com',9999999999),
(2663,'Rohit Kumar Guin',	'@gmail.com',9999999999),
(2685,'Ajay Kisku',		'ajayrajkisku22@gmail.com',6203282581),
(2657,'Riya Kumari',		'@gmail.com',9999999999),
(2658,'Raj Nandani Puja',	'@gmail.com',9999999999),
(2694,'Akash Kumar',		'@gmail.com', 9999999999),
(2673,'Sagar Prasad',		'@gmail.com', 9999999999),
(2656,'Saurav Kumar Nayak',	'@gmail.com',9999999999),
(2698,'Gulam Mohiuddin',	'@gmail.com',9999999999),
(2695,'Dhiraj Kumar Yadav',	'@gmail.com',9999999999),
(2708,'Anubhav Jha',		'@gmail.com',9999999999),
(2691,'Abdul Aziz',		'@gmail.com',9999999999);




