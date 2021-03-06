PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "Books" (
	"Id"			Integer NOT NULL DEFAULT 0 PRIMARY KEY AUTOINCREMENT,
	"Name"			Text NOT NULL DEFAULT '' CHECK (length(Name) <= 30),
	"ISBN"			Integer NOT NULL DEFAULT 0 UNIQUE,
	"Price"			Numeric NOT NULL DEFAULT 0,
	"IsObsolete" 	Boolean NOT NULL DEFAULT 0 CHECK (IsObsolete in (0, 1)), -- Stored as integer 0 or 1
	"BookType"		Integer NOT NULL DEFAULT 0 CHECK (BookType >= 1 and BookType <= 3) 
);
CREATE INDEX IDX_Books_Id ON Books(Id);
COMMIT;
