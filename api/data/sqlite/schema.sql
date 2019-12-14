PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Books" (
	"Id"		Integer NOT NULL DEFAULT 0 PRIMARY KEY AUTOINCREMENT,
	"Name"		Text NOT NULL DEFAULT '' CHECK (length(Name) <= 30),
	"ISBN"		Integer NOT NULL DEFAULT 0 UNIQUE,
	"Price"		Numeric NOT NULL DEFAULT 0,
	"Obsolete" 	Boolean NOT NULL DEFAULT 'False',
	"BookType"	Integer NOT NULL DEFAULT 0, CHECK (BookType >= 0 and BookType <= 3) 
);
COMMIT;
