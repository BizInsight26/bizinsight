
-- BizInsight - Synthetic Data Schema

-- Stores entity
CREATE TABLE Stores (
    StoreID INTEGER PRIMARY KEY
);

-- Daily sales entity
CREATE TABLE Sales (
    SaleID INTEGER PRIMARY KEY,
    StoreID INTEGER NOT NULL,
    Date DATE NOT NULL,
    Sales DECIMAL(10, 2),
    Customers INTEGER,
    Open INTEGER NOT NULL CHECK (Open IN (0, 1)),

    FOREIGN KEY (StoreID) REFERENCES Stores(StoreID),
    UNIQUE (StoreID, Date)
);
